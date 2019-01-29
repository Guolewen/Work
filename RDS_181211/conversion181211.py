import pandas as pd
from mysql.connector import connection
import time
import re
import numpy as np
from collections import Counter
from collections import defaultdict
from common_class import Base_Guo


class Convert(Base_Guo):

    def __init__(self):
        super().__init__()
    
    @staticmethod
    def read_own_data(own_path):
        own = pd.read_csv(own_path, engine='python', encoding='utf-8')
        return own

    @staticmethod
    def read_musashi_data(musashi_path):
        musashi = pd.read_csv(musashi_path, engine='python', encoding='utf-8')
        return musashi

    @staticmethod
    def ams_category_to_musashi_code(x, j):

        for k in j["options"]:
            if x == k:
                return j["options"][k]
        return np.NaN

    def convert_electricity_format(self, x):

        if x[0] == 'on':
            return np.NaN
        for k, v in self._area.items():
            if x[1] in v and x[0] == 'off':
                return k

    def convert_management_person_and_setback(self, x):
        # count the number of on and off raise ValueError if the number of 'on' is larger than 2
        # written by Lewen, Guo
        if Counter(x)['on'] >= 2:
            raise ValueError("More than Two 'on's are found, please check 管理人状態とセットバック")
        for i in x.index:
            if x[i] == 'on':
                return self.__equipment2category[i]

    def core_convert_equipment_items(self, own_df):

        # create an empty dataframe to store "string" value of equipment                          #written by Lewen, Guo

        equipment_df = pd.DataFrame()

        for keys, values in self._equipment.items():
            if values != 'na':
                equipment_df[self._equipment[keys]] = own_df[keys]. \
                    apply(lambda x: self._equipment[keys] if x == 'off' else np.NaN)
                own_df.drop(keys, axis=1, inplace=True)
            elif keys == 'electricit':
                equipment_df[keys] = own_df[[keys, "todoufuken"]].apply(lambda x: self.convert_electricity_format(x),
                                                                        raw=True, axis=1)
                own_df.drop(keys, axis=1, inplace=True)
            elif values == 'na':
                own_df.drop(keys, axis=1, inplace=True)
        # convert electricity
        management_person = own_df[['patrol', 'day_shift', 'resident']]
        setback = own_df[['setback', 'setback_finished']]
        # put all equipments into one column and seperate it by '/'
        own_df['設備'] = equipment_df.apply(lambda x: '/'.join(x), axis=1, raw=True)
        own_df['管理人'] = management_person.apply(lambda x: self.convert_management_person_and_setback(x), axis=1)
        own_df['セットバック面積基準'] = setback.apply(lambda x: self.convert_management_person_and_setback(x), axis=1)

        return own_df

    def core_convert_category_items(self, own_df):

        for k, v in self._category.items():
            try:
                own_df[k] = own_df[k].apply(lambda x: self.ams_category_to_musashi_code(x, v))
            except KeyError:
                raise KeyError("{} Item Has Not Been Found, Check the own_df File".format(k))
            own_df.rename(columns={k: v["key"]}, inplace=True)

        return own_df

    # Deal with Address
    @staticmethod
    def connect_to_db():
        cnx = connection.MySQLConnection(user='guo_lewen', password='uC9EsmPg',
                                         host='hyas.cmhljhxzbtx3.ap-northeast-1.rds.amazonaws.com',
                                         database='hyas')
        return cnx

    def todufuken_convert(self, x):
        for k, v in self.__todofuken.items():
            if x == k:
                return v

    @staticmethod
    def match_p(x, query_data):
        q_l = list(query_data[tuple(x.iloc[0].tolist())].values())
        return x.apply(lambda x: q_l, result_type='expand', axis=1)

    def convert_string2address_code(self, df):
        t11 = time.time()
        conn = self.connect_to_db()
        todofuken_num = Counter(df["todoufuken"])
        sikuchouson_num = Counter(df["sikuchouson"])
        todofuken_tuple = tuple(todofuken_num)
        sikuchouson_tuple = tuple(sikuchouson_num)
        # solve the problem that single-element python tuple is "(data,)" while mySQL "where" only accepts "(data)"
        # Written By Lewen, Guo
        if len(todofuken_tuple) < 2:
            todofuken_tuple = (todofuken_tuple[0], '')
        if len(sikuchouson_tuple) < 2:
            sikuchouson_tuple = (sikuchouson_tuple[0], '')

        query = (
            "SELECT DISTINCT todoufuken_cd, sikuchouson_cd, chouiki_cd, todoufuken, sikuchouson, chouiki "
            "FROM hyas.address "
            "WHERE todoufuken in {} AND sikuchouson in {}".format(todofuken_tuple, sikuchouson_tuple))
        query_data = pd.read_sql_query(query, conn)

        query_data = query_data.set_index(["todoufuken", "sikuchouson", "chouiki"])

        query_data_input = query_data.to_dict('index')

        f_address= df.groupby(["todoufuken", "sikuchouson", "chouiki"]).apply(lambda x: self.match_p(x, query_data_input)).\
            rename(columns={0: '都道府県', 1: '行政区', 2: '町丁目名'})
        conn.close()
        t22 = time.time()
        print("string2address", t22-t11)

        return f_address

    @staticmethod
    def split_chouiki_string(x):
        # find the index where string should be seperated                                         #written by Lewen, Guo
        try:
            index = re.search(r'\d', x).start()
        except AttributeError:
            return [x, '']
        except TypeError:
            return ['', '']

        return [x[:index], x[index:]]

    def core_convert_address(self, own):
        """

        :param own:
        :return:
        """
        # split own chouiki into two cols                                                       #written by Lewen, Guo

        own[['chouiki', "番地(非表示用)"]] = own['chouiki'].apply(lambda x: self.split_chouiki_string(x)).apply(pd.Series)

        # select address columns and make it a new dataframe                                    #written by Lewen, Guo
        new_df = own[["todoufuken", "sikuchouson", "chouiki"]]
        # put new_df into def self.convert_string2address_code(self, df)                        #written by Lewen, Guo

        return self.convert_string2address_code(new_df)

    def core_cols_only_change_colname(self, own):

        return own.rename(columns=self._translationdict)

    def execute(self, own_path, musashi_path):

        own = self.read_own_data(own_path)
        musashi = self.read_musashi_data(musashi_path)

        conv1 = self.core_cols_only_change_colname(own)

        conv2 = self.core_convert_equipment_items(conv1)

        conv3 = self.core_convert_category_items(conv2)

        conv3[["都道府県", "行政区", "町丁目名"]] = self.core_convert_address(conv3)


        conv3.drop(['access1', 'access2', 'access3', 'building_square_1f', 'building_square_2f', 'building_square_3f',
                    'building_square_other', 'comment', 'car_parking_num', 'complete_kind', 'fee_kind', 'jyuusho2',
                    'jyuusho3', 'junior_high_school_kind', 'kcar_parking_num', 'memo', 'object_last_price',
                    'other_regulation', 'primary_school_kind', 'tou_num', 'private_road_square_kind',
                    'patrol', 'day_shift', 'resident', 'setback', 'setback_finished', 'todoufuken', 'todoufuken_cd',
                    'sikuchouson', 'sikuchouson_cd', 'chouiki'], axis=1, inplace=True)
        # make all the remaining musashi cols as np.NaN                                           #written by Lewen, Guo
        for i in musashi.columns:
            if i not in conv3.columns:
                conv3[i] = np.NaN

        return conv3


if __name__ == '__main__':
    #own = pd.read_csv(r"C:\aiba_request\own.csv", engine='python', encoding='utf-8')
    # Convert().convert_category_items(own)
    t1 = time.time()
    # Convert().convert_address(own)
    after_conv = Convert().execute(r"C:\aiba_request\own.csv",
                                   r"C:\AMSdata\武蔵data20180717193001AMS\data20180717193001\10001\data.csv")
    t2 = time.time()
    # Convert().core_convert_equipment_items(own)
    after_conv.to_csv(r"C:\aiba_request\conv.csv", encoding='utf-8', index=False)

    print("Total Time is:", t2 - t1)

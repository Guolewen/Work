#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re


class Reins:

    def __init__(self, file, browser='ie'):
        """

        :param file: original reins text file                                                  // written by Lewen, Guo
        :param browser: browser used to extract original reins text file                       // written by Lewen, Guo
        """
        self.browser = browser
        self.file = file
        self.__reg_pattern = re.compile(r'[0-9]{12}|[0-9]{8}')
        self.type = type
        self.__reg_4_no = re.compile(r'ＮＯ')
        self.__phone_pattern = re.compile(r'\d{2,4}-\d{2,4}-\d{2,4}')
        self.__object_num = re.compile(r'\d{1}|\d{2}|100')
        self.__nengo = re.compile(r'平成\d{2}年|昭和\d{2}年')
        self.__nengo2 = re.compile(r'\d年\d{2}月')
        self.__date = re.compile(r'\d{4}/\d{2}/\d{2}')

    def read_file(self):
        """

        :return: splited list with '\t' and '\n' replaced with blank                           // written by Lewen, Guo
        """
        with open(self.file, 'r') as f:
            file_text = f.read()
            get_type = file_text.split()
            # get the type of file such as '売り戸建、成約済みマンション'                       // written by Lewen, Guo
            for k in range(len(get_type)):
                if self.__reg_4_no.fullmatch(get_type[k]) is not None:
                    self.type = get_type[k-1]
                    print(self.type)
                    break

            if self.browser == 'ie':
                return file_text.replace('\n', ' ').split(' ')

            elif self.browser == 'chrome':
                return file_text.replace('\n', ' ').replace('\t', ' ').split(' ')

    def get_col_name(self):
        """

        :return: column names of reins data                                                    // written by Lewen, Guo
        """
        split_file = self.read_file()
        # obtain the starting index and end index of column name                                // written by Lewen, Guo
        colname_range = [idx for idx in range(len(split_file)) if split_file[idx] == '物件番号' or
                         split_file[idx] == '問合せ電話番号' or split_file[idx] == '成約年月日']
        global colname_last
        colname_last = colname_range[1]
        if len(colname_range) != 2:
            raise ValueError("テキストファイルの項目は違っております。チェックしてください。")
        else:
            pass

        col_names = []
        for j in range(colname_range[0], colname_range[1] + 1):
            if split_file[j] is not '':
                for cname in split_file[j].split('/'):
                    col_names.append(cname)
        # deal with abnormal number of column names  異常処理(/)                                // written by Lewen, Guo
        if len(col_names) != 32 and len(col_names) != 30:
            raise ValueError("項目の数は誤っています、ファイルの形をチェックしてください")
        return split_file, col_names

    def compute_start_end_index(self, split_file):
        start_index = np.array([idx for idx in range(len(split_file)) if
                                self.__reg_pattern.fullmatch(split_file[idx]) is not None])
        if self.type.startswith('売り'):
            """
            Search the end of each object by "問い合わせ電話番号"　
            which is "self.__phone_pattern = re.compile('\d{2,4}-\d{2,4}-\d{4}')"
            in this code. Set the end index as the index of "問い合わせ電話番号" 
            """
            end_index = np.array([j for j in range(len(split_file)) if
                                 self.__phone_pattern.fullmatch(split_file[j]) is not None])
        elif self.type.startswith('成約売り'):
            """
            Search the date by regex "1900/10/10" first, since there should be only two dates (更新年月日と成約年月日) 
            in each object and "成約年月日" would be the last data for each object. Set the end index for each 
            "成約売り" object as the index of "成約年月日". 
            """

            date_lists = [self.__date.fullmatch(split_file[idx]) for idx in range(len(split_file))]
            end_index = [idx for idx, values in enumerate(date_lists) if values is not None][1::2]

        for idx in end_index:
            if self.__date.fullmatch(split_file[idx]) is None:
                if self.__phone_pattern.fullmatch(split_file[idx]) is None:
                    raise ValueError("ファイルの形が間違っていた。")
        return start_index, end_index

    def clean_abnormal_case(self, split_file):
        """
        Deal with '平成12年12月' '平成12年 1月' '平成 1年12月' '平成 1年 2月' and 異常処理
        :param split_file:
        :return:
        """
        k = 0
        while k < len(split_file):
            if self.__nengo.fullmatch(split_file[k]):
                # print("Add 1 time", k)
                split_file[k:k + 2] = [''.join(split_file[k:k + 2])]
            elif split_file[k] == '平成' or split_file[k] == '昭和':
                if self.__nengo2.fullmatch(split_file[k + 1]):
                    split_file[k:k + 2] = [''.join(split_file[k:k + 2])]
                else:
                    split_file[k:k + 3] = [''.join(split_file[k:k + 3])]
            elif split_file[k] == '中古マン':
                if split_file[k + 1] == '－':
                    print("中古マンの後に　「－」をついています。 ")
                    split_file.insert(k + 1, '')
                else:
                    pass
            else:
                pass
            k += 1
        return split_file

    def get_col_data(self):
        split_file, col_names = self.get_col_name()
        split_file = self.clean_abnormal_case(split_file)
        start_index, end_index = self.compute_start_end_index(split_file)
        if self.browser == 'ie':
            if self.type == '売り・土地':
                d_array_index = np.array([start_index, start_index + 2, start_index + 4, start_index + 8,
                                          start_index + 11, start_index + 11, start_index + 13, start_index + 16,
                                          start_index + 18, start_index + 20, start_index + 21, start_index + 21,
                                          start_index + 23, start_index + 27, start_index + 29, start_index + 32,
                                          start_index + 34, start_index + 36, start_index + 40, start_index + 42,
                                          start_index + 45, start_index + 48, start_index + 50, start_index + 52,
                                          start_index + 54, start_index + 56, start_index + 57, start_index + 58,
                                          start_index + 60, start_index + 61, start_index + 61, start_index + 62
                                          ])
            elif self.type == '売り・戸建て':
                d_array_index = np.array([start_index, start_index + 2, start_index + 4, start_index + 6,
                                          start_index + 9, start_index + 9, start_index + 11, start_index + 14,
                                          start_index + 16, start_index + 18, start_index + 19, start_index + 19,
                                          start_index + 21, start_index + 25, start_index + 27, start_index + 30,
                                          start_index + 32, start_index + 34, start_index + 38, start_index + 39,
                                          start_index + 41, start_index + 44, start_index + 46, start_index + 48,
                                          start_index + 50, start_index + 52, start_index + 53, start_index + 54,
                                          start_index + 56, start_index + 57, start_index + 57, start_index + 58
                                          ])
            elif self.type == '売り・マンション':
                d_array_index = np.array([start_index, start_index + 2, start_index + 4, start_index + 6,
                                          start_index + 9, start_index + 11, start_index + 14, start_index + 16,
                                          start_index + 18, start_index + 19, start_index + 21, start_index + 25,
                                          start_index + 27, start_index + 30, start_index + 33, start_index + 36,
                                          start_index + 40, start_index + 41, start_index + 42, start_index + 44,
                                          start_index + 46, start_index + 48, start_index + 50, start_index + 52,
                                          start_index + 53, start_index + 54, start_index + 56, start_index + 57,
                                          start_index + 57, start_index + 58
                                          ])
            elif self.type == '成約売り・土地':
                d_array_index = np.array([start_index, start_index + 2, start_index + 4, start_index + 8,
                                          start_index + 11, start_index + 11, start_index + 13, start_index + 16,
                                          start_index + 18, start_index + 20, start_index + 21, start_index + 21,
                                          start_index + 23, start_index + 27, start_index + 29, start_index + 32,
                                          start_index + 34, start_index + 36, start_index + 37, start_index + 39,
                                          start_index + 42, start_index + 45, start_index + 47, start_index + 49,
                                          start_index + 50, start_index + 51, start_index + 53, start_index + 54,
                                          start_index + 55, start_index + 56, start_index + 58, start_index + 59
                                          ])
            elif self.type == '成約売り・戸建て':
                d_array_index = np.array([start_index, start_index + 2, start_index + 4, start_index + 6,
                                          start_index + 9, start_index + 9, start_index + 11,  start_index + 14,
                                          start_index + 16, start_index + 18, start_index + 19, start_index + 19,
                                          start_index + 21, start_index + 25, start_index + 27, start_index + 30,
                                          start_index + 32, start_index + 34, start_index + 35, start_index + 36,
                                          start_index + 38, start_index + 41, start_index + 43, start_index + 45,
                                          start_index + 46, start_index + 47, start_index + 49, start_index + 50,
                                          start_index + 51, start_index + 53, start_index + 54, start_index + 55
                                          ])
            elif self.type == '成約売り・マンション':
                d_array_index = np.array([start_index, start_index + 2, start_index + 4, start_index + 6,
                                          start_index + 9, start_index + 11, start_index + 14,  start_index + 16,
                                          start_index + 18, start_index + 19, start_index + 21, start_index + 25,
                                          start_index + 27, start_index + 30, start_index + 33, start_index + 36,
                                          start_index + 37, start_index + 38, start_index + 39, start_index + 41,
                                          start_index + 43, start_index + 45, start_index + 46, start_index + 47,
                                          start_index + 49, start_index + 50, start_index + 51, start_index + 53,
                                          start_index + 54, start_index + 55
                                          ])
        elif self.browser == 'chrome':
            if self.type == '売り・土地' or self.type == '売り・戸建て':
                d_array_index = np.array([start_index, start_index + 2, start_index + 3, start_index + 5,
                                          start_index + 6, start_index + 6, start_index + 8, start_index + 9,
                                          start_index + 11, start_index + 12, start_index + 13, start_index + 13,
                                          start_index + 15, start_index + 17, start_index + 19, start_index + 20,
                                          start_index + 21, start_index + 23, start_index + 25, start_index + 27,
                                          start_index + 28, start_index + 29, start_index + 30, start_index + 31,
                                          start_index + 33, start_index + 35, start_index + 36, start_index + 37,
                                          start_index + 38, start_index + 39, start_index + 39, start_index + 40
                                          ])
            elif self.type == '売り・マンション':
                d_array_index = np.array([start_index, start_index + 2, start_index + 3, start_index + 5,
                                          start_index + 6, start_index + 8, start_index + 9, start_index + 11,
                                          start_index + 12, start_index + 13, start_index + 15, start_index + 17,
                                          start_index + 19, start_index + 20, start_index + 21, start_index + 22,
                                          start_index + 24, start_index + 25, start_index + 26, start_index + 28,
                                          start_index + 29, start_index + 30, start_index + 32, start_index + 34,
                                          start_index + 35, start_index + 36, start_index + 37, start_index + 38,
                                          start_index + 38, start_index + 39
                                          ])
            elif self.type == '成約売り・土地' or self.type == '成約売り・戸建て':
                d_array_index = np.array([start_index, start_index + 2, start_index + 3, start_index + 5,
                                          start_index + 6, start_index + 6, start_index + 8, start_index + 9,
                                          start_index + 11, start_index + 12, start_index + 13, start_index + 13,
                                          start_index + 15, start_index + 17, start_index + 19, start_index + 20,
                                          start_index + 21, start_index + 22, start_index + 23, start_index + 25,
                                          start_index + 26, start_index + 27, start_index + 28, start_index + 29,
                                          start_index + 30, start_index + 31, start_index + 33, start_index + 34,
                                          start_index + 35, start_index + 36, start_index + 37, start_index + 38
                                          ])
            elif self.type == '成約売り・マンション':
                d_array_index = np.array([start_index, start_index + 2, start_index + 3, start_index + 5,
                                          start_index + 6, start_index + 8, start_index + 9, start_index + 11,
                                          start_index + 12, start_index + 13, start_index + 15, start_index + 17,
                                          start_index + 19, start_index + 20, start_index + 21, start_index + 22,
                                          start_index + 23, start_index + 24, start_index + 25, start_index + 27,
                                          start_index + 28, start_index + 29, start_index + 30, start_index + 31,
                                          start_index + 33, start_index + 34, start_index + 35, start_index + 36,
                                          start_index + 37, start_index + 38
                                          ])
        final_list = []
        """
        Take care of this part, it may be difficult to understand.
        Use prev and curr to decide those have the same d_array_index, the same index here is to deal with
        ' 一方/東 '　and '一般/分かれ'
        
        Algorithm Details:
        1. Iterate the columns of d_array_index(n x k), n represents number of 物件 in the file, k 
         represents number of row(物件項目) taken from raw file in each 物件. 
         Each column(物件) contains k rows(物件項目).
        2. Construct two variables, prev and curr. Current represents current 
        value(index) of the row(物件項目). Prev represents the value(index) of previous row of current row.
        3. Create a empty new list 'new_list' to store the cleaned data.
        4. Iterate over the k rows(物件項目), do a if-else. If Prev is not equal to  Curr, we first replace '/' with '' 
        bacause there is data such as '徒歩7分/'　and then take the data out of split_file based on the value(index) of 
        Curr. If the value(index) of current row equals the value(index) of previous row, we encounter ' 一方/東 '　
        and '一般/分かれ'. In this case, for the first appearance of such data, we deal it as normal
        (replace '/' with ''). However, for the second appearance 
        (we set it manually. see the d_array_index construction)
        We delete the previous data which, for most case is '一方東' or '一般分かれ' and add two new data which is the 
        first and second element of splited data '一方' and '東'. If the data is missing, use a try-except to add a None 
        to new_list.
        5. Finally, Combine colnames and new_list and convert it as a python Dict.
        
        """
        for n in range(d_array_index.shape[1]):
            new_list = []
            prev = None
            for curr in d_array_index[:, n]:
                if prev == curr:
                    new_list.pop()
                    try:
                        new_list.append(split_file[prev].split('/')[0])
                        new_list.append(split_file[curr].split('/')[1])
                    except IndexError:
                        new_list.append('')
                        raise TypeError("異常な物件項目またはエラーがあり、ファイルをチェックしてください。")
                else:
                    new_list.append(split_file[curr].replace('/', ''))
                prev = curr
            final_list.append(dict(zip(col_names, new_list)))
        print(final_list)
        #check



        return final_list




if __name__ == '__main__':
    import time
    # Test IE Tochi

    #ie_tochi= Reins(r"C:\AMSdata\newreins\ie\土地_IE_レインズデータ.txt").get_col_data()

    #pd.DataFrame.from_dict(ie_tochi).to_csv(r"C:\AMSdata\kikin_data_sample\ie_uri_tochi.csv", encoding='cp932'                              index=False)

    # IE 成約　Tochi

    #ie_tochi = Reins(r"C:\AMSdata\newreins\ie\成約土地_IE_近畿レインズデータ.txt").get_col_data()
    ie_seiyaku = Reins(r"C:\Reins\IE-20190116T021730Z-001\IE\IE 成約済土地①.txt").get_col_data()
    # IE kodate
    #ie_kodate = Reins(r"C:\AMSdata\newreins\ie\戸建_IE_近畿レインズデータ.txt").get_col_data()
    # IE 成約 kodate
    #ie_seiyaku_kodate = Reins(r"C:\AMSdata\newreins\ie\成約戸建_IE_近畿レインズデータ.txt").get_col_data()
    # IE mansion
    #ie_mansion = Reins(r"C:\Reins\IE-20190116T003151Z-001\IE\IE 販売中マンション①.txt").get_col_data()
    #ie_mansion = Reins(r"C:\Reins\IE-20190116T003151Z-001\IE\IE 販売中マンション②.txt").get_col_data()
    #IE 成約 mansion
    # ie_seiyaku_mansion = Reins(r"C:\AMSdata\newreins\ie\成約マンション_IE_近畿レインズデータ.txt").get_col_data()
    # Chrome
    #chrome_tochi = Reins(r"C:\AMSdata\newreins\chrome\土地_GC_レインズデータ.txt", browser='chrome').get_col_data()
    #chrome_kodate = Reins(r"C:\AMSdata\newreins\chrome\戸建_GC_近畿レインズデータ.txt", browser='chrome').get_col_data()

    #chrome_mansion = Reins(r"C:\AMSdata\newreins\chrome\マンション_GC_近畿レインズデータ.txt", browser='chrome').get_col_data()

    #Chrome 成約

    #chrome_seiyaku_tochi = Reins(r"C:\AMSdata\newreins\chrome\成約土地_GC_近畿レインズデータ.txt", browser='chrome').get_col_data()
    #chrome_seiyaku_kodate = Reins(r"C:\AMSdata\newreins\chrome\成約戸建_GC_近畿レインズデータ.txt", browser='chrome').get_col_data()



    import os

    chrome_list = os.listdir(r"C:\Reins\Chrome-20190116T003307Z-001\Chrome")
    chrome_list2 = os.listdir(r"C:\Reins\Chrome-20190116T021752Z-001\Chrome")
    ie_list = os.listdir(r"C:\Reins\IE-20190116T003151Z-001\IE")
    ie_list2 = os.listdir(r"C:\Reins\IE-20190116T021730Z-001\IE")
    # Chrome test
    for i, v in enumerate(chrome_list):
        t1 = time.time()
        Reins(os.path.join(r"C:\Reins\Chrome-20190116T003307Z-001\Chrome", v), browser='chrome').get_col_data()
        t2 = time.time()
        print(t2 - t1)



    # Chrome test
    for i, v in enumerate(chrome_list):
        t1 = time.time()
        Reins(os.path.join(r"C:\Reins\Chrome-20190116T003307Z-001\Chrome", v), browser='chrome').get_col_data()
        t2 = time.time()
        print(t2 - t1)
    # chrome seiyaku
    for i, v in enumerate(chrome_list2):
        t1 = time.time()
        Reins(os.path.join(r"C:\Reins\Chrome-20190116T021752Z-001\Chrome", v), browser='chrome').get_col_data()
        t2 = time.time()
        print(t2 - t1)
    # ie
    for i, v in enumerate(ie_list2):
        print(v)
        t1 = time.time()
        Reins(os.path.join(r"C:\Reins\IE-20190116T021730Z-001\IE", v), browser='ie').get_col_data()
        t2 = time.time()

        print(t2 - t1)

    for i, v in enumerate(ie_list):
        t1 = time.time()
        Reins(os.path.join(r"C:\Reins\IE-20190116T003151Z-001\IE", v), browser='ie').get_col_data()
        t2 = time.time()
        print(t2 - t1)

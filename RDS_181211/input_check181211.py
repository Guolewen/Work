from dateutil.parser import parse
from common_class import Base_Guo
class ObjectSummary(Base_Guo):

    def __init__(self):
        super().__init__()

    def check_input(self, input):
        """
        core part of checking process
        :param input: dicts where keys are the subset of AMS_key, values are the input values which should be checked
        //Written by Lewen, Guo
        :return:
        """

        for k in input.keys():
            print(k)
            if self.AMS_keys[k]['type'] == 'options':
                if input[k] in self.AMS_keys[k]['options'].keys():
                    print(k, self.AMS_keys[k]['key'], "pass")
                else:
                    raise ValueError("入力項目 '{}' が誤っている、入力のテキストを直してください。"
                                     .format(self.AMS_keys[k]['key']))
            elif self.AMS_keys[k]['type'] == 'text':
                print(k, "{}はテキストです。".format(self.AMS_keys[k]['key']))


            elif self.AMS_keys[k]['type'] == 'number' and self.AMS_keys[k]['step'] == 1:
                if input[k] == '':
                    pass
                    print("入力項目 '{}'が空白です".format(self.AMS_keys[i]['key']))
                try:
                    int(input[k])
                    print("pass", "入力項目'{}'は整数です".format(self.AMS_keys[k]['key']))
                except ValueError:
                    raise ValueError("入力項目 '{}' が誤っている、整数だけを入力してください。"
                                         .format(self.AMS_keys[k]['key']))

            elif not (not (self.AMS_keys[k]['type'] == 'number' and self.AMS_keys[k]['step'] == 0.1) and not (
                    self.AMS_keys[k]['step'] == 0.01)):
                if input[k] == '':
                    pass
                    print("入力項目 '{}'が空白です".format(self.AMS_keys[i]['key']))
                try:
                    int(input[k])
                    print("pass", "入力項目'{}'は整数です".format(self.AMS_keys[k]['key']))
                except ValueError:
                    try:
                        float(input[k])
                        print("pass", "入力項目'{}'は数字です".format(self.AMS_keys[k]['key']))
                    except ValueError:
                        raise ValueError("入力項目 '{}' が誤っている、数字だけを入力してください。"
                                         .format(self.AMS_keys[k]['key']))


if __name__ == '__main__':
    ObjectSummary().check_input({"object_kind_detail":"497", "contract_date": "", 'object_no':'231321'})
    #ObjectSummary().check_input({"obj_status":"2"})
#    ObjectSummary().check_input({"object_kind_detail": "423"})
    ObjectSummary().check_input({'object_price': '2', 'road_square2': '0.12', 'room_layout': '1'})
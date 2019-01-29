import numpy as np
class Base_Guo(object):
    def __init__(self):
        self._translationdict = {'access1_line_cd': '沿線1', 'access1_station_cd': '駅1',
                                  'access2_line_cd': '沿線2', 'access2_station_cd': '駅2',
                                  'access3_line_cd': '沿線3', 'access3_station_cd': '駅3',
                                  'balcony': 'バルコニー面積', 'building_kakunin_no': '建築確認番号',
                                  'building_square_total': '建物面積', 'building_structure_detail': '建物構造その他',
                                  'building_structure_ground': '地上',
                                  'building_structure_underground': '地下', 'building_to_land_ratio': '建ぺい率１',
                                  'construction_company': '施工会社',
                                  'fee_ratio': '手数料率', 'fee_price': '手数料',
                                  'floor': '所在階', 'floor_area_ratio': '容積率１',
                                  'intermediary_agent_fax': '業者FAX',
                                  'intermediary_agent_jyuusho': '業者住所???', 'intermediary_agent_name': '業者名',
                                  'intermediary_agent_person': '担当者名', 'intermediary_agent_tel': '業者電話番号',
                                  'junior_high_school': '中学校名',
                                  'land_square': '土地面積',
                                  'leased_land_kind': '借地期間',
                                  'leased_land_m': '借地月??', 'leased_land_y': '借地年??', 'leased_land_price': '借地料',
                                  'management_company': '管理会社名',
                                  'management_cost': '管理費',
                                  'object_name': '物件名',
                                  'object_price': '価格',
                                  'parking_cost': '駐車場月額',
                                  'primary_school': '小学校',
                                  'private_road_square': '私道面積',
                                  'repair_cost': '修繕積立金',
                                  'road_frontage_square1': '接道道路幅１',
                                  'road_frontage_square2': '接道道路幅２', 'road_frontage_square3': '接道道路幅３',
                                  'road_square1': '接道幅員１', 'road_square2': '接道幅員２',
                                  'road_square3': '接道幅員３',
                                  'room_layout': '間取り部屋数',
                                  'room_no': '部屋番号',
                                  'room_num': '総戸数', 'setback_square': 'セットバック面積',
                                  'square': '専有面積', 'square_kind': '専有面積基準',
                                  'store_no': '店舗ID',
                                  'vacate_fixed_date': '引渡し年月',
                                  'walk1': '徒歩１', 'walk2': '徒歩2', 'walk3': '徒歩3',
                                  }
        self._equipment = {'aircondition': 'エアコン', 'all_electric': 'オール電化',
                            'appearance_tile': '外観タイル張り', 'auto_lock': 'オートロック',
                            'barrier_free': 'バリアフリー', 'basement': '地下室',
                            'bathroom_dryer': '浴室乾燥機',
                            'bicycle_parking': '駐輪場', 'bidet': '温水洗浄便座',
                            'bus_1tsubo_over': '浴室1坪以上', 'dimple_key': 'na',
                            'cable_broadcast': '有線放送', 'car_parking': 'na', 'bs': 'na', 'bed': 'na',
                            'catv': 'CATV', 'ceiling_storage': 'na',
                            'city_gas': 'ガス：都市', 'closet': 'ウォークインクロゼット',
                            'cooling': '冷房', 'corner_room': '角部屋', 'counter_kitchen': '対面式キッチン',
                            'cs': 'CSアンテナ', 'delivery_box': '宅配ボックス',
                            'disposer': 'ディスポーザー', 'divide': '分割可',
                            'double_glass': '複層ガラス', 'elevator': 'エレベータ',
                            'floor_heat': '床暖房', 'furiwake': 'na', 'gesuidou': 'na',
                            'grenier': 'グルニエ', 'heating': '暖房', 'hori_gotatsu': '掘ごたつ',
                            'hot_water_supply': '給湯', 'ih_cooking_heater': 'IHコンロ',
                            'indoor_wash': '室内洗濯機置場', 'instrument': '楽器相談',
                            'interphone': 'TVドアホン', 'jyoukasou_kobetsu': '排水：浄化槽',
                            'jyoukasou_shuuchuu': '排水：浄化槽', 'kumitori': '排水：汲取',
                            'kcar_parking': 'na', 'refrigerator': 'na',
                            'loft': 'ロフト', 'maisonette': 'メゾネット',
                            'office_use': '事務所利用可', 'oidaki': '追い炊き',
                            'parking_1box': 'na', 'pet': 'ペット相談',
                            'private_garden': 'na', 'propane_gas_concentration': 'ガス：集中ＬＰＧ',
                            'propane_gas_separate': 'ガス：個別ＬＰＧ', 'purpose_benefit': 'na',
                            'purpose_resort': 'na', 'quiet_residential_area': '閑静な住宅地', 'resort': 'リゾート向き',
                            'roof_balcony': 'ルーフバルコニー', 'security_24h': '24時間セキュリティ',
                            'shampoo_dresser': 'シャンプードレッサー', 'shower': 'na',
                            'sokkou': '排水：側溝', 'sunny': '陽当り良好', 'system_kitchen': 'システムキッチン',
                            'tableware_wash': '食器洗乾燥機', 'terrace': 'na', 'storage_space': 'na',
                            'three_parking': '駐車3台以上可', 'three_side_balcony': '3面バルコニー',
                            'top_floor': '最上階', 'trunk_room': 'トランクルーム',
                            'two_family': '2世帯住宅', 'two_parking': '駐車2台可',
                            'two_side_balcony': '2面バルコニー', 'two_toilet': 'トイレ2\ヶ所',
                            'under_floor_storage': '床下収納', 'ventilation_24h': '24時間換気システム',
                            'vacate_fixed_date_later': 'na', 'well': '井戸', 'waterwork': 'na'}
        self._category = {"architectural_condition":
                               {"key": "建築条件",
                                "options": {"指定なし": np.NaN, "建築条件付": 1
                                    , "更地渡し(建築条件なし)": 0
                                    , "現況渡し(建築条件なし)": 0, "無": 0
                                            }}, "city_planning": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "都市計画"
            , "options": {
                "不明": np.NaN
                , "市街化区域": 1
                , "調整区域": 2
                , "非線引区域": 3
                , "区域外": 4
                , "準都市区域": 5
                , "市街化調整区域": 2
                , "都市計画区域外": 4  # Not included in excel sheet
            }}, "management_form": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "管理形態"
            , "options": {
                "指定なし": np.NaN
                , "自主管理": 3
                , "委託管理": 1
                , "全部委託": 2
            }}, "media_trade_status": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "取引態様"
            , "options": {
                "指定なし": np.NaN
                , "売主": 1
                , "代理": 2
                , "専任": 4
                , "一般": 5
                , "専属専任": 3
                , "媒介": 6
            }}, "room_layout_kind": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "間取りタイプ"
            , "options": {
                "指定なし": np.NaN
                , "DK": 3
                , "LDK": 5
                , "R": 1
                , "K": 2
                , "SK": 6
                , "SDK": 7
                , "LK": 5
                , "SLK": 8
                , "SLDK": 9
            }}, "use_district": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "用途地域"
            , "options": {
                "不明": np.NaN
                , "近隣商業": 4
                , "商業": 5
                , "準工業": 6
                , "工業": 7
                , "工専": 8
                , "指定無": 99
                , "1種低層": 1
                , "2種低層": 10
                , "1種中高": 11
                , "2種中高": 2
                , "1種住居": 12
                , "2種住居": 3
                , "準住居": 13
                , "無指定": 99
            }}, "land_square_kind": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "土地面積計測方式"
            , "options": {
                "指定なし": np.NaN
                , "公簿": 1
                , "実測": 2
            }}, "road_houi1": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "接道方向１"
            , "options": {
                "指定なし": np.NaN
                , "北": 1
                , "南": 5
                , "東": 3
                , "西": 7
                , "北西": 8
                , "北東": 2
                , "南西": 6
                , "南東": 4
            }}, "road_houi2": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "接道方向２"
            , "options": {
                "指定なし": np.NaN
                , "北": 1
                , "南": 5
                , "東": 3
                , "西": 7
                , "北西": 8
                , "北東": 2
                , "南西": 6
                , "南東": 4
            }}, "road_houi3": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "接道方向３"
            , "options": {
                "指定なし": np.NaN
                , "北": 1
                , "南": 5
                , "東": 3
                , "西": 7
                , "北西": 8
                , "北東": 2
                , "南西": 6
                , "南東": 4
            }}, "road_kind1": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "接道種別1"
            , "options": {
                "指定なし": np.NaN
                , "公道": 1
                , "私道": 2
            }}, "road_kind2": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "接道種別2"
            , "options": {
                "指定なし": np.NaN
                , "公道": 1
                , "私道": 2
            }}, "road_kind3": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "接道種別3"
            , "options": {
                "指定なし": np.NaN
                , "公道": 1
                , "私道": 2
            }}, "fee_format": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "仲介手数料区分"
            , "options": {
                "指定なし": np.NaN
                , "分かれ": 1
                , "なし": 2
                , "3%+6万": 3
                , "率のみ": 6
                , "金額": 7
                , "率+金": 8
            }}, "current_state": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "現況"
            , "options": {
                "指定なし": np.NaN
                , "更地": 12
                , "上物有": 12
                , "その他": 12
                , "居住中": 1
                , "空": 2
                , "賃貸中": 3
                , "建築中": 10
                , "完成済": 7
                , "未着工": 8
                , "未完成": 4
                , "使用中": 9  # no such option in js source code
                , "田": 12
            }}, "balcony_houi": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "バルコニー方向（主要採光方向）"
            , "options": {
                "指定なし": np.NaN
                , "北": 1
                , "南": 5
                , "東": 3
                , "西": 7
                , "北西": 8
                , "北東": 2
                , "南西": 6
                , "南東": 4
            }}, "building_structure": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "建物構造"
            , "options": {
                "指定なし": np.NaN
                , "木造": 1
                , "ブロック": 2
                , "鉄骨": 3
                , "RC": 4
                , "SRC": 5
                , "PC": 6
                , "HPC": 7
                , "軽量鉄骨": 8
                , "ALC": 0
                , "重量鉄骨": 3
                , "その他": 9
            }}, "chimoku": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "地目"
            , "options": {
                "不明": np.NaN
                , "宅地": 1
                , "田": 2
                , "畑": 3
                , "山林": 4
                , "雑種地": 5
                , "運河用地": 6
                , "塩田": 7
                , "境内地": 8
                , "原野": 9
                , "公園": 10
                , "公衆用道路": 11
                , "鉱泉地": 12
                , "水道用地": 13
                , "井溝": 14
                , "ため池": 15
                , "池沼": 16
                , "堤": 17
                , "保安林": 18
                , "牧場": 19
                , "墓地": 20
                , "用悪水路": 21
                , "旧既存宅地": 22
                , "その他": 22
            }}, "garage": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "駐車場"
            , "options": {
                "指定なし": np.NaN
                , "空有": 1
                , "空無": 2
                , "近隣確保": 3
                , "無し": 4
                , "有": 1
            }}, "land_auth": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "土地権利"
            , "options": {
                "指定なし": np.NaN
                , "所有権": 1
                , "地上権": 4
                , "貸借権": 6
                , "普通地上権": 4
                , "定期地上権": 5
                , "普通貸借権": 6
                , "定期貸借権": 7
                , "旧法賃借": 3
            }}, "optimum_use": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "最適用途"
            , "options": {
                "指定なし": np.NaN
                , "住宅用地": 1
                , "マンション用地": 2
                , "ビル用地": 3
                , "店舗用地": 4
                , "工業用地": 5
                , "配送センター": 6
                , "営業所": 7
                , "保養所": 8
                , "事務所用地": 10
                , "別荘用地": 11
                , "倉庫用地": 12
                , "資材置場用地": 13
                , "家庭菜園用地": 14
                , "アパート用地": 15
                , "社宅社員寮": 16
                , "病院診療所": 17
                , "畑・農地": 18
                , "事業用地": 19
                , "駐車場用地": 20
                , "リゾート向き": 55
            }}, "vacate_kind": {
            "tag": "SELECT"
            , "type": "options"
            , "key": "明渡種別(即・期日指定等)"
            , "options": {
                "指定なし": np.NaN
                , "未記入": 2
                , "即": 1
                , "相談": 2
                , "期日指定": 3
            }}
                           }
        self._area = {'電気：北海道': ['北海道'], '電気：東北': ['青森県', '岩手県', '宮城県', '秋田県', '山形県',
                                                    '福島県'], '電気：北陸': ['新潟県', '富山県', '石川県', '福井県'], '電気：東京': ['茨城県',
                                                                                                             '栃木県',
                                                                                                             '群馬県',
                                                                                                             '埼玉県',
                                                                                                             '千葉県',
                                                                                                             '東京都',
                                                                                                             '神奈川県'],
                       '電気：中部': ['長野県', '山梨県',
                                 '岐阜県', '静岡県', '愛知県'], '電気：関西': ['三重県', '滋賀県', '京都府', '大阪府', '兵庫県',
                                                                 '奈良県', '和歌山県'],
                       '電気：中国': ['鳥取県', '島根県', '岡山県', '広島県', '山口県'],
                       '電気：四国': ['徳島県', '香川県', '愛媛県', '高知県'], '電気：九州': ['福岡県', '佐賀県',
                                                                        '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県'],
                       '電気：沖縄': ['沖縄県']
                       }

        self._todofuken = {"北海道": 1
            , "青森県": 2
            , "岩手県": 3
            , "宮城県": 4
            , "秋田県": 5
            , "山形県": 6
            , "福島県": 7
            , "茨城県": 8
            , "栃木県": 9
            , "群馬県": 10
            , "埼玉県": 11
            , "千葉県": 12
            , "東京都": 13
            , "神奈川県": 14
            , "新潟県": 15
            , "富山県": 16
            , "石川県": 17
            , "福井県": 18
            , "山梨県": 19
            , "長野県": 20
            , "岐阜県": 21
            , "静岡県": 22
            , "愛知県": 23
            , "三重県": 24
            , "滋賀県": 25
            , "京都府": 26
            , "大阪府": 27
            , "兵庫県": 28
            , "奈良県": 29
            , "和歌山県": 30
            , "鳥取県": 31
            , "島根県": 32
            , "岡山県": 33
            , "広島県": 34
            , "山口県": 35
            , "徳島県": 36
            , "香川県": 37
            , "愛媛県": 38
            , "高知県": 39
            , "福岡県": 40
            , "佐賀県": 41
            , "長崎県": 42
            , "熊本県": 43
            , "大分県": 44
            , "宮崎県": 45
            , "鹿児島県": 46
            , "沖縄県": 47
                            }
        self._equipment2category = {'patrol': 3, 'day_shift': 4, 'resident': 2, 'setback': 1, 'setback_finished': 2}


        self.AMS_keys = {'object_name': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "物件名称"
            , "preset_value": ""
            , "placeholder": "例:品川区上大崎 5LDK"
            , "help": "これは物件名称のヘルプ用のテキストです"
            , "table_key": "object_summary"
            , "unselectable": True
        }, 'object_kind_detail': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "物件種別"
            , "options": {
                "496": "売地"
                , "497": "売地　借地権譲渡"
                , "498": "売地　底地権譲渡"
                , "499": "戸建"
                , "500": "テラスハウス"
                , "501": "マンション"
                , "502": "公団"
                , "503": "公社"
                , "504": "タウンハウス"
                , "505": "リゾートマンション"
                , "506": "店舗"
                , "507": "店舗付住宅"
                , "508": "住宅付店舗"
                , "509": "事務所"
                , "510": "店舗・事務所"
                , "511": "ビル"
                , "512": "工場"
                , "513": "マンション"
                , "514": "倉庫"
                , "515": "アパート"
                , "516": "寮"
                , "517": "旅館"
                , "518": "ホテル"
                , "519": "別荘"
                , "520": "リゾートマンション"
                , "521": "モーテル"
                , "522": "医院"
                , "523": "ガソリンスタンド"
                , "524": "特殊浴場"
                , "525": "サウナ"
                , "526": "保養所"
                , "527": "作業所"
                , "528": "駐車場"
                , "529": "その他"
                , "8625": "その他"
                , "8626": "その他"
                , "8627": "その他"
                , "8628": "その他"
                , "": "指定なし"
            }
            , "preset_value": "496"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
            , "unselectable": True
        }, 'object_kind': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "物件種目"
            , "options": {
                "165": "指定なし"
                , "166": "土地"
                , "167": "戸建"
                , "168": "マンション"
                , "169": "事業用"
                , "4376": "その他"
            }
            , "preset_value": "165"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
            , "unselectable": True
        }, 'object_no': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "物件番号"
            , "preset_value": ""
            , "placeholder": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
            , "unselectable": True
        }, 'obj_status': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "ステータス"
            , "options": {
                "1": "公開中"
                , "2": "商談中"
                , "3": "成約済"
                , "4": "売止め"
                , "5": "削除済"
            }
            , "preset_value": "1"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
            , "unselectable": True
        }, 'object_price': {
            "tag": "INPUT"
            , "type": "number"
            , "key": "物件価格"
            , "preset_value": ""
            , "placeholder": "3000"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "万円"
            }
            , "step": 0.1
            , "table_key": "object_summary"
            , "unselectable": True
        }, 'seiyaku_price': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.1
            , "key": "成約価格"
            , "preset_value": ""
            , "placeholder": "3000"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "万円"
                , "attr": {
                }
            }
            , "table_key": "object_summary"
            , "unselectable": True
        }, 'contract_date': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "成約日"
            , "preset_value": ""
            , "placeholder": "2019-01-01"
            , "help": "これはヘルプ用のテキストです"
            , "calendar": {}
            , "table_key": "object_summary"
            , "unselectable": True
        }, 'new_build_price': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.1
            , "key": "新築時価格"
            , "preset_value": ""
            , "placeholder": "3000"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "万円"
                , "attr": {
                }
            }
            , "table_key": "object_summary"
            , "unselectable": True
        }, 'room_layout': {
            "tag": "INPUT"
            , "type": "number"
            , "key": "部屋数"
            , "step": 1
            , "preset_value": ""
            , "placeholder": "3"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "部屋"
                , "attr": {
                }
            }
            , "table_key": "object_summary"
        }, 'room_layout_kind': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "間取り"
            , "options": {
                "196": "指定なし"
                , "197": "DK"
                , "198": "LDK"
                , "199": "R"
                , "200": "K"
                , "201": "SK"
                , "202": "SDK"
                , "203": "LK"
                , "204": "SLK"
                , "205": "SLDK"
            }
            , "help": "これはヘルプ用のテキストです"
            , "preset_value": "196"
            , "table_key": "object_summary"
        }, 'todoufuken': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "都道府県"
            , "options": {
                "北海道": "北海道"
                , "青森県": "青森県"
                , "岩手県": "岩手県"
                , "宮城県": "宮城県"
                , "秋田県": "秋田県"
                , "山形県": "山形県"
                , "福島県": "福島県"
                , "茨城県": "茨城県"
                , "栃木県": "栃木県"
                , "群馬県": "群馬県"
                , "埼玉県": "埼玉県"
                , "千葉県": "千葉県"
                , "東京都": "東京都"
                , "神奈川県": "神奈川県"
                , "新潟県": "新潟県"
                , "富山県": "富山県"
                , "石川県": "石川県"
                , "福井県": "福井県"
                , "山梨県": "山梨県"
                , "長野県": "長野県"
                , "岐阜県": "岐阜県"
                , "静岡県": "静岡県"
                , "愛知県": "愛知県"
                , "三重県": "三重県"
                , "滋賀県": "滋賀県"
                , "京都府": "京都府"
                , "大阪府": "大阪府"
                , "兵庫県": "兵庫県"
                , "奈良県": "奈良県"
                , "和歌山県": "和歌山県"
                , "鳥取県": "鳥取県"
                , "島根県": "島根県"
                , "岡山県": "岡山県"
                , "広島県": "広島県"
                , "山口県": "山口県"
                , "徳島県": "徳島県"
                , "香川県": "香川県"
                , "愛媛県": "愛媛県"
                , "高知県": "高知県"
                , "福岡県": "福岡県"
                , "佐賀県": "佐賀県"
                , "長崎県": "長崎県"
                , "熊本県": "熊本県"
                , "大分県": "大分県"
                , "宮崎県": "宮崎県"
                , "鹿児島県": "鹿児島県"
                , "沖縄県": "沖縄県"
            }
            , "options_attr": {
                "北海道": {"pref_code": "1"}
                , "青森県": {"pref_code": "2"}
                , "岩手県": {"pref_code": "3"}
                , "宮城県": {"pref_code": "4"}
                , "秋田県": {"pref_code": "5"}
                , "山形県": {"pref_code": "6"}
                , "福島県": {"pref_code": "7"}
                , "茨城県": {"pref_code": "8"}
                , "栃木県": {"pref_code": "9"}
                , "群馬県": {"pref_code": "10"}
                , "埼玉県": {"pref_code": "11"}
                , "千葉県": {"pref_code": "12"}
                , "東京都": {"pref_code": "13"}
                , "神奈川県": {"pref_code": "14"}
                , "新潟県": {"pref_code": "15"}
                , "富山県": {"pref_code": "16"}
                , "石川県": {"pref_code": "17"}
                , "福井県": {"pref_code": "18"}
                , "山梨県": {"pref_code": "19"}
                , "長野県": {"pref_code": "20"}
                , "岐阜県": {"pref_code": "21"}
                , "静岡県": {"pref_code": "22"}
                , "愛知県": {"pref_code": "23"}
                , "三重県": {"pref_code": "24"}
                , "滋賀県": {"pref_code": "25"}
                , "京都府": {"pref_code": "26"}
                , "大阪府": {"pref_code": "27"}
                , "兵庫県": {"pref_code": "28"}
                , "奈良県": {"pref_code": "29"}
                , "和歌山県": {"pref_code": "30"}
                , "鳥取県": {"pref_code": "31"}
                , "島根県": {"pref_code": "32"}
                , "岡山県": {"pref_code": "33"}
                , "広島県": {"pref_code": "34"}
                , "山口県": {"pref_code": "35"}
                , "徳島県": {"pref_code": "36"}
                , "香川県": {"pref_code": "37"}
                , "愛媛県": {"pref_code": "38"}
                , "高知県": {"pref_code": "39"}
                , "福岡県": {"pref_code": "40"}
                , "佐賀県": {"pref_code": "41"}
                , "長崎県": {"pref_code": "42"}
                , "熊本県": {"pref_code": "43"}
                , "大分県": {"pref_code": "44"}
                , "宮崎県": {"pref_code": "45"}
                , "鹿児島県": {"pref_code": "46"}
                , "沖縄県": {"pref_code2": "47"}
            }
            , "event": {

            }
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'sikuchouson': {
            "tag": "SELECT"
            , "type": "options"
            , "options": {
                "": "指定なし"
            }
            , "key": "市区町村"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'chouiki': {

            "tag": "INPUT"
            , "type": "text"
            , "key": "町丁目"
            , "preset_value": ""
            , "placeholder": "上大崎"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'chome': {

            "tag": "INPUT"
            , "type": "text"
            , "key": "丁目"
            , "preset_value": ""
            , "placeholder": "一丁目"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'banchi': {

            "tag": "INPUT"
            , "type": "text"
            , "key": "番地以降"
            , "preset_value": ""
            , "placeholder": "1-1"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'lat': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "緯度"
            , "preset_value": ""
            , "table_key": "object_summary"
        }, 'lng': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "経度"
            , "preset_value": ""
            , "table_key": "object_summary"
        }, 'land_square_kind': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "公簿/実測"
            , "options": {
                "475": "指定なし"
                , "476": "公簿"
                , "477": "実測"
            }
            , "preset_value": "475"
            , "table_key": "object_summary"
        }, 'land_square': {
            "tag": "INPUT"
            , "type": "number"
            , "step" : 0.01
            , "key": "土地面積"
            , "preset_value": ""
            , "placeholder": "50.00"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {
                }
            }
            , "table_key": "object_summary"
        }, 'building_square_total': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "延床面積"
            , "preset_value": ""
            , "placeholder": "50.00"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'building_square_1f': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "1階部分床面積"
            , "preset_value": ""
            , "placeholder": "50.00"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'building_square_2f': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "2階部分床面積"
            , "preset_value": ""
            , "placeholder": "50.00"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'building_square_3f': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "3階部分床面積"
            , "preset_value": ""
            , "placeholder": "50.00"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'building_square_other': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "その他床面積"
            , "preset_value": ""
            , "placeholder": "50.00"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'square_kind': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "壁芯/公簿"
            , "options": {
                "556": "指定なし"
                , "557": "壁芯"
                , "4380": "公簿"
            }
            , "preset_value": "556"
            , "table_key": "object_summary"
        }, 'square': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "専有面積"
            , "preset_value": ""
            , "placeholder": "50.00"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'primary_school': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "小学校名"
            , "preset_value": ""
            , "placeholder": "ハイアス小学校"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'junior_high_school': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "中学校名"
            , "preset_value": ""
            , "placeholder": "ハイアス中学校"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'new_kind': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "新築/中古"
            , "options": {
                "190": "指定なし"
                , "191": "新築"
                , "192": "中古"
            }
            , "preset_value": "190"
            , "table_key": "object_summary"
        }, 'original_no': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "自社番号"
            , "preset_value": ""
            , "placeholder": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'access1': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "路線1"
            , "options": {
                "": "指定なし"
            }
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "event": {

            }
            , "table_key": "object_summary"
        }, 'access1_name': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "鉄道駅1"
            , "options": {
                "": "指定なし"
            }
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'walk1': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "鉄道駅徒歩時間1"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "分"
                , "attr": {
                }
            }
            , "table_key": "object_summary"
        }, 'bus1': {
            "tag": "INPUT"
            , "type": "number"
            , "key": "バス乗車時間"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "分"
                , "attr": {
                }
            }
            , "table_key": "object_summary"
        }, 'bus_stop1': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "バス停名1"
            , "preset_value": ""
            , "placeholder": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'bus_walk1': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "バス停徒歩時間1"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "分"
                , "attr": {
                }
            }
            , "table_key": "object_summary"
        }, 'access2': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "路線2"
            , "options": {
                "": "指定なし"
            }
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "event": {
            }
            , "table_key": "object_summary"
        }, 'access2_name': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "鉄道駅2"
            , "options": {
                "": "指定なし"
            }
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'walk2': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "鉄道徒歩時間2"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "分"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'bus2': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "バス乗車時間"
            , "preset_value": ""
            , "placeholder": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'bus_stop2': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "バス停名2"
            , "preset_value": ""
            , "placeholder": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'bus_walk2': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "バス停徒歩時間"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "分"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'access3': {

            "tag": "SELECT"
            , "type": "options"
            , "key": "路線3"
            , "options": {
                "": "指定なし"
            }
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "event": {

            }
            , "table_key": "object_summary"
        }, 'access3_name': {

            "tag": "SELECT"
            , "type": "options"
            , "key": "鉄道駅3"
            , "options": {
                "": "指定なし"
            }
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'walk3': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "鉄道徒歩時間3"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "分"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'bus3': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "バス乗車時間3"
            , "preset_value": ""
            , "placeholder": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'bus_stop3': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "バス停名3"
            , "preset_value": ""
            , "placeholder": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_summary"
        }, 'bus_walk3': {
            "tag": "INPUT"
            , "type": "number"
            , "step" : 1
            , "key": "バス停徒歩時間3"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "分"
                , "attr": {

                }
            }
            , "table_key": "object_summary"
        }, 'data_kind': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "取込種別"
            , "options": {
                "1": "新規"
                , "2": "変更"
                , "3": "掲載終了"
                , "4": "復活"
                , "": "指定なし"
            }
            , "preset_value": ""
            , "table_key": "object_summary"
        }, 'housepoint_hide_flg': {
            "tag": "INPUT"
            , "type": "checkbox"
            , "key": "ハウスポイントに表示しない"
            , "preset_value": "1"
            , "table_key": "object_summary"
        }, 'private_road_square_kind': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "私道あり/なし"
            , "options": {
                "403": "指定なし"
                , "404": "無"
                , "405": "別"
                , "406": "含"
            }
            , "preset_value": "403"
            , "table_key": "object_land"
        }, 'private_road_square': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "私道面積"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_land"
        }, 'road_houi1': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "接道方位1"
            , "options": {
                "547": "指定なし"
                , "548": "北"
                , "549": "南"
                , "550": "東"
                , "551": "西"
                , "552": "北西"
                , "553": "北東"
                , "554": "南西"
                , "555": "南東"
            }
            , "preset_value": "547"
            , "table_key": "object_land"
        }, 'road_kind1': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "公道/私道1(接道)"
            , "options": {
                "486": "指定なし"
                , "487": "公道"
                , "488": "私道"
            }
            , "preset_value": "486"
            , "table_key": "object_land"
        }, 'road_square1': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "幅員1(接道)"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_land"
        }, 'road_frontage_square1': {
            "tag": "INPUT"
            , "type": "number"
            , "key": "間口1(接道)"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_land"
        }, 'road_houi2': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "接道方位2"
            , "options": {
                "547": "指定なし"
                , "548": "北"
                , "549": "南"
                , "550": "東"
                , "551": "西"
                , "552": "北西"
                , "553": "北東"
                , "554": "南西"
                , "555": "南東"
            }
            , "preset_value": "547"
            , "table_key": "object_land"
        }, 'road_kind2': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "公道/私道2(接道)"
            , "options": {
                "486": "指定なし"
                , "487": "公道"
                , "488": "私道"
            }
            , "preset_value": "486"
            , "table_key": "object_land"
        }, 'road_square2': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "幅員2(接道)"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }

            , "table_key": "object_land"
        }, 'road_frontage_square2': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "間口2(接道)"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_land"
        }, 'road_houi3': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "接道方位3"
            , "options": {
                "547": "指定なし"
                , "548": "北"
                , "549": "南"
                , "550": "東"
                , "551": "西"
                , "552": "北西"
                , "553": "北東"
                , "554": "南西"
                , "555": "南東"
            }
            , "preset_value": "547"
            , "table_key": "object_land"
        }, 'road_kind3': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "公道/私道3(接道)"
            , "options": {
                "486": "指定なし"
                , "487": "公道"
                , "488": "私道"
            }
            , "preset_value": "486"
            , "table_key": "object_land"
        }, 'road_square3': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "幅員3(接道)"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }

            , "table_key": "object_land"
        }, 'road_frontage_square3': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "間口3(接道)"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "㎡"
                , "attr": {

                }
            }
            , "table_key": "object_land"
        }, 'land_auth': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "土地権利"
            , "options": {
                "478": "指定なし"
                , "479": "所有権"
                , "480": "地上権"
                , "481": "貸借権"
                , "482": "普通地上権"
                , "483": "定期地上権"
                , "484": "普通貸借権"
                , "485": "定期貸借権"
                , "4377": "旧法賃借"
            }
            , "preset_value": "478"
            , "table_key": "object_land"
        }, 'kenrikin': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "権利金"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_land"
        }, 'kenrikin_zeikubun': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "権利金税区分"
            , "options": {
                "10567": "指定なし"
                , "10568": "税込"
                , "10569": "税無"
            }
            , "preset_value": "10567"
            , "table_key": "object_land"
        }, 'leased_land_cond': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "借地期間条件"
            , "options": {
                "10573": "指定なし"
                , "10574": "新規契約期間"
                , "10575": "残存期間"
            }
            , "preset_value": "10573"
            , "table_key": "object_land"
        }, 'teisyaku_kubun': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "定借譲渡可否区分"
            , "options": {
                "10576": "指定なし"
                , "10577": "可"
                , "10578": "不可"
            }
            , "preset_value": "10576"
            , "table_key": "object_land"
        }, 'leased_land_price': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "借地料"
            , "preset_value": ""
            , "placeholder": "10.25"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "万円"
                , "attr": {

                }
            }

            , "table_key": "object_land"
        }, 'leased_land_kind': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "種別(借地期間or期日指定)"
            , "options": {
                "209": "指定なし"
                , "210": "借地期間"
                , "211": "期日指定"
            }
            , "preset_value": "209"
            , "table_key": "object_land"
        }, 'leased_land_y': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "借地期間(年数)"
            , "preset_value": ""
            , "table_key": "object_land"
        }, 'leased_land_m': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "借地期間(月数)"
            , "preset_value": ""
            , "table_key": "object_land"
        }, 'leased_land_date': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "期日"
            , "preset_value": ""
            , "calendar": {}
            , "table_key": "object_land"
        }, 'building_to_land_ratio': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "建蔽率"
            , "preset_value": ""
            , "placeholder": "40"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "%"
                , "attr": {

                }
            }

            , "table_key": "object_land"
        }, 'floor_area_ratio': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "容積率"
            , "preset_value": ""
            , "placeholder": "300"
            , "help": "これはヘルプ用のテキストです"
            , "unit": {
                "txt": "%"
                , "attr": {

                }
            }

            , "table_key": "object_land"
        }, 'use_district': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "用途地域"
            , "options": {
                "559": "不明"
                , "560": "近隣商業"
                , "561": "商業"
                , "562": "準工業"
                , "563": "工業"
                , "564": "工専"
                , "565": "指定無"
                , "566": "1種低層"
                , "567": "2種低層"
                , "568": "1種中高"
                , "569": "2種中高"
                , "570": "1種住居"
                , "571": "2種住居"
                , "572": "準住居"
                , "4387": "無指定"
            }
            , "preset_value": "559"
            , "table_key": "object_land"
        }, 'use_district2': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "用途地域2"
            , "options": {
                "559": "不明"
                , "560": "近隣商業"
                , "561": "商業"
                , "562": "準工業"
                , "563": "工業"
                , "564": "工専"
                , "565": "指定無"
                , "566": "1種低層"
                , "567": "2種低層"
                , "568": "1種中高"
                , "569": "2種中高"
                , "570": "1種住居"
                , "571": "2種住居"
                , "572": "準住居"
                , "4387": "無指定"
            }
            , "preset_value": "559"
            , "table_key": "object_land"
        }, 'chimoku': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "地目"
            , "options": {
                "442": "不明"
                , "443": "宅地"
                , "444": "田"
                , "445": "畑"
                , "446": "山林"
                , "447": "雑種地"
                , "448": "運河用地"
                , "449": "塩田"
                , "450": "境内地"
                , "451": "原野"
                , "452": "公園"
                , "453": "公衆用道路"
                , "454": "鉱泉地"
                , "455": "水道用地"
                , "456": "井溝"
                , "457": "ため池"
                , "458": "池沼"
                , "459": "堤"
                , "460": "保安林"
                , "461": "牧場"
                , "462": "墓地"
                , "463": "用悪水路"
                , "464": "旧既存宅地"
                , "4381": "その他"
            }
            , "preset_value": "442"
            , "table_key": "object_land"
        }, 'chimoku2': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "地目2"
            , "options": {
                "442": "不明"
                , "443": "宅地"
                , "444": "田"
                , "445": "畑"
                , "446": "山林"
                , "447": "雑種地"
                , "448": "運河用地"
                , "449": "塩田"
                , "450": "境内地"
                , "451": "原野"
                , "452": "公園"
                , "453": "公衆用道路"
                , "454": "鉱泉地"
                , "455": "水道用地"
                , "456": "井溝"
                , "457": "ため池"
                , "458": "池沼"
                , "459": "堤"
                , "460": "保安林"
                , "461": "牧場"
                , "462": "墓地"
                , "463": "用悪水路"
                , "464": "旧既存宅地"
                , "4381": "その他"
            }
            , "preset_value": "442"
            , "table_key": "object_land"
        }, 'other_regulation': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "その他規制(自由記述)"
            , "preset_value": ""
            , "placeholder": ""
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_land"
        }, 'city_planning': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "都市計画"
            , "options": {
                "469": "不明"
                , "470": "市街化区域"
                , "471": "調整区域"
                , "472": "非線引区域"
                , "473": "区域外"
                , "474": "準都市区域"
                , "4385": "市街化調整区域"
                , "4386": "都市計画区域外"
            }
            , "preset_value": "469"
            , "table_key": "object_land"
        }, 'current_state': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "現況"
            , "options": {
                "364": "指定なし"
                , "365": "更地"
                , "366": "上物有"
                , "367": "その他"
                , "368": "居住中"
                , "369": "空"
                , "370": "賃貸中"
                , "371": "建築中"
                , "372": "完成済"
                , "373": "未着工"
                , "374": "居住中"
                , "375": "空"
                , "376": "賃貸中"
                , "377": "未完成"
                , "378": "完成済"
                , "19625": "田"
            }
            , "preset_value": "364"
            , "table_key": "object_land"
        }, 'current_state_note': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "現況備考欄"
            , "preset_value": ""
            , "placeholder": "10"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_land"
        }, 'architectural_condition': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "建築条件"
            , "options": {
                "341": "指定なし"
                , "342": "建築条件付"
                , "343": "更地渡し(建築条件なし)"
                , "344": "現況渡し(建築条件なし)"
                , "4388": "無"
            }
            , "preset_value": "341"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_land"
        }, 'architectural_reason': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "建築許可理由"
            , "options": {
                "10579": "指定なし"
                , "10580": "開発許可等による分譲地内"
                , "10581": "都市計画法施行令36条1項３号ロに該当"
                , "10582": "調整区域につき建築許可要"
                , "10583": "調整区域につき建築許可要。建築主の許可要件あり"
            }
            , "preset_value": "10579"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_land"
        }, 'kokudo_report': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "国土法届出要否"
            , "options": {
                "10584": "指定なし"
                , "10585": "不要"
                , "10586": "必要"
                , "10587": "事前届出が必要"
                , "10588": "事前確認前"
                , "10589": "事前確認審査中"
                , "10590": "事前確認済"
            }
            , "preset_value": "10584"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_land"
        }, 'complete_ym': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "完成年月日"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": ""
            , "table_key": "object_building"
        }, 'complete_kind': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "完成予定/済"
            , "options": {
                "250": "指定なし"
                , "251": "完成予定"
                , "252": "完成済み"
            }
            , "preset_value": "250"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_building"
        }, 'building_structure': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "構造"
            , "options": {
                "347": "指定なし"
                , "348": "木造"
                , "349": "ブロック"
                , "350": "鉄骨"
                , "351": "RC"
                , "352": "SRC"
                , "353": "PC"
                , "354": "HPC"
                , "355": "軽量鉄骨"
                , "356": "ALC"
                , "4389": "重量鉄骨"
                , "4390": "その他"
            }
            , "preset_value": "347"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_building"
        }, 'building_structure_detail': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "詳細"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
        }, 'building_structure_ground': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "地上階数"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": ""
            , "table_key": "object_building"
        }, 'building_structure_underground': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "地下階数"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": ""
            , "table_key": "object_building"
        }, 'balcony_houi': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "バルコニー方位"
            , "options": {
                "547": "指定なし"
                , "548": "北"
                , "549": "南"
                , "550": "東"
                , "551": "西"
                , "552": "北西"
                , "553": "北東"
                , "554": "南西"
                , "555": "南東"
            }
            , "preset_value": "547"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_building"
        }, 'balcony': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "バルコニー面積"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": ""
            , "table_key": "object_building"
        }, 'floor': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "所在階"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": ""
            , "table_key": "object_building"
        }, 'room_no': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "号室"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "510"
            , "unit": {
                "txt": "号室"
                , "attr": {

                }
            }

            , "table_key": "object_building"
        }, 'tou_num': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "建物棟数"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "5"
            , "unit": {
                "txt": "棟"
                , "attr": {

                }
            }

            , "table_key": "object_building"
        }, 'room_num': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "総戸数"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "100"
            , "unit": {
                "txt": "戸"
                , "attr": {

                }
            }

            , "table_key": "object_building"
        }, 'management_cost': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "管理費"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "10.80"
            , "unit": {
                "txt": "万円"
                , "attr": {

                }
            }

            , "table_key": "object_building"
        }, 'repair_cost': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "修繕積立金"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "1080"
            , "unit": {
                "txt": "円"
                , "attr": {

                }
            }

            , "table_key": "object_building"
        }, 'garage': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "付属建物等"
            , "options": {
                "4": "指定なし"
                , "5": "空有"
                , "6": "空無"
                , "7": "近隣確保"
                , "8": "無し"
                , "4391": "有"
            }
            , "preset_value": "4"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_building"
        }, 'parking_cost': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 1
            , "key": "駐車場費（月額）"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "10.80"
            , "unit": {
                "txt": "万円"
                , "attr": {

                }
            }

            , "table_key": "object_building"
        }, 'parking_distance': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "駐車場距離"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "10"
            , "unit": {
                "txt": "m"
                , "attr": {

                }
            }
            , "table_key": "object_building"
        }, 'parking_site_kubun': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "敷地内外"
            , "options": {
                "10570": "指定なし"
                , "10571": "敷地内"
                , "10572": "敷地外"
            }
            , "preset_value": "10570"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_building"
        }, 'construction_company': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "施工会社"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "株式会社あああ"
            , "table_key": "object_building"
        }, 'management_company': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "管理会社"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "株式会社あああ"
            , "table_key": "object_building"
        }, 'building_kakunin_no': {
            "tag": "INPUT"
            , "type": "text"
            , "key": "建築確認番号"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "10"
            , "table_key": "object_building"
        }, 'management_form': {
            "tag": "SELECT"
            , "type": "options"
            , "key": "管理形態"
            , "options": {
                "253": "指定なし"
                , "254": "自主管理"
                , "255": "委託管理"
                , "256": "全部委託"
            }
            , "preset_value": "253"
            , "help": "これはヘルプ用のテキストです"
            , "table_key": "object_building"
        }, 'resident': {
            "tag": "INPUT"
            , "type": "checkbox"
            , "key": "常駐"
            , "preset_value": "1"
            , "table_key": "object_building"
        }, 'day_shift': {
            "tag": "INPUT"
            , "type": "checkbox"
            , "key": "日勤"
            , "preset_value": "1"
            , "table_key": "object_building"
        }, 'patrol': {
            "tag": "INPUT"
            , "type": "checkbox"
            , "key": "巡回"
            , "preset_value": "1"
            , "table_key": "object_building"
        }, 'setback': {
            "tag": "INPUT"
            , "type": "checkbox"
            , "key": "セットバック要否"
            , "preset_value": "1"
            , "table_key": "object_land"
        }, 'setback_square': {
            "tag": "INPUT"
            , "type": "number"
            , "step": 0.01
            , "key": "セットバック面積"
            , "preset_value": ""
            , "help": "これはヘルプ用のテキストです"
            , "placeholder": "10"
            ,  "attr": {}
        },
            'setback_finished': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "セットバック済"
                , "preset_value": "1"
                , "table_key": "object_land"
            }, 'two_parking': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "駐車場2台以上"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'top_floor': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "最上階"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'corner_room': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "角部屋"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'is_renovation': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "リフォーム"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'corner_lot': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "角地"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'two_road_surface': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "二面道路"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'barrier_free': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "バリアフリー"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'bus_1tsubo_over': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "バス1坪以上"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'maisonette': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "メゾネット"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'pet': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "ペット相談"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'instrument': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "楽器相談"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'appearance_tile': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "外観タイル張り"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'two_family': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "二世帯向き"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'sunny': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "日当たり良好"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'quiet_residential_area': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "閑静な住宅街"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'ventilation_24h': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "24時間換気システム"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'security_24h': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "24時間セキュリティ"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'office_use': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "事務所使用可"
                , "preset_value": "1"
                , "table_key": "object_equipment"
            }, 'key_box': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "キーボックス"
                , "preset_value": ""
                , "table_key": "object_equipment"
            }, 'vacate_kind': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "明渡種別(即・期日指定等)"
                , "options": {
                    "212": "指定なし"
                    , "213": "未記入"
                    , "214": "即"
                    , "215": "相談"
                    , "216": "期日指定"
                }
                , "preset_value": "212"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_summary"
            }, 'vacate_fixed_date': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "明渡期日"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "calendar": {}
                , "table_key": "object_summary"
            }, 'vacate_fixed_date_later': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "以降"
                , "preset_value": "1"
                , "table_key": "object_summary"
            }, 'comment': {
                "tag": "TEXTAREA"
                , "key": "備考"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": "その他の記載事項がある場合は記載してください。"
                , "table_key": "object_summary"
            }, 'ad': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "広告掲載確認"
                , "preset_value": "1"
                , "table_key": "object_publish"
            }, 'hp': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "HP掲載"
                , "preset_value": "1"
                , "table_key": "object_publish"
            }, 'homes': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "HOME'S掲載"
                , "preset_value": "1"
                , "table_key": "object_publish"
            }, 'athome': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "athome掲載"
                , "preset_value": "1"
                , "table_key": "object_publish"
            }, 'suumo': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "SUUMO掲載"
                , "preset_value": "1"
                , "table_key": "object_publish"
            }, 'publish_access': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "交通広告"
                , "options": {
                    "257": "指定なし"
                    , "258": "鉄道"
                    , "259": "バス"
                }
                , "preset_value": "257"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_publish"
            }, 'musashi_conv_homes': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "HOME'S"
                , "preset_value": "1"
                , "table_key": "object_publish"
            }, 'musashi_conv_athome': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "athome"
                , "preset_value": "1"
                , "table_key": "object_publish"
            }, 'musashi_conv_suumo': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "SUUMO"
                , "preset_value": "1"
                , "table_key": "object_publish"
            }, 'incompany_comment': {
                "tag": "TEXTAREA"
                , "key": "社内共有用"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": "社内用のメモがある場合、記載してください。"
                , "table_key": "object_publish"
            }, 'site_comment': {
                "tag": "TEXTAREA"
                , "key": "HP用コメント"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'undefined': {
                "tag": "INPUT"
                , "type": "button"
                , "key": "「SUUMO用設備登録」ボタン"
                , "preset_value": "設備登録"
                , "table_key": "object_catch"
            }, 'suumo_comment': {
                "tag": "TEXTAREA"
                , "key": "SUUMOネット専用コメント"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'athome_comment1': {
                "tag": "TEXTAREA"
                , "key": "アットホーム備考①"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'athome_comment2': {
                "tag": "TEXTAREA"
                , "key": "アットホーム備考②"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'athome_comment3': {
                "tag": "TEXTAREA"
                , "key": "athome用プロのコメント"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'athome_staff_id': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "athome用スタッフID"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'homes_comment': {
                "tag": "TEXTAREA"
                , "key": "HOME'S用 物件の特徴"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'catch_large1': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "マイソクキャッチ1"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'catch_large2': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "マイソクキャッチ2"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'catch_medium1': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "マイソクキャッチ3"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_catch"
            }, 'catch_medium2': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "メモ1"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'catch_small1': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "メモ2"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'catch_small2': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "メモ3"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'catch_small3': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "メモ4"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'catch_small4': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "メモ5"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'catch_small5': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "メモ6"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'flyer_interest': {
                "tag": "INPUT"
                , "type": "number"
                , "step": 0.01
                , "key": "金利"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": "8"
                , "unit": {
                    "txt": "%"
                    , "attr": {

                    }
                }
                , "table_key": "object_summary"
            }, 'flyer_repayment_year': {
                "tag": "INPUT"
                , "type": "number"
                , "step": 1
                , "key": "返済年数"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": "36"
                , "unit": {
                    "txt": "年"
                    , "attr": {
                    }
                }
                , "table_key": "object_summary"
            }, 'flyer_other_cost': {
                "tag": "INPUT"
                , "type": "number"
                , "step": 1
                , "key": "その他費用"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": "10"
                , "unit": {
                    "txt": "万円"
                    , "attr": {

                    }
                }
                , "table_key": "object_building"
            }, 'extraction_media': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "掲載元情報"
                , "options": {
                    "588": "指定なし"
                    , "589": "ふれんず"
                    , "590": "レインズ"
                    , "591": "HOME'S"
                    , "592": "yahoo不動産"
                    , "593": "スーモ"
                    , "594": "新聞等"
                    , "595": "住友不動産"
                    , "596": "三井のリハウス"
                    , "597": "西鉄の仲介"
                    , "598": "不動産ジャパン"
                    , "599": "goo不動産"
                    , "600": "at home"
                    , "5002": "三和土地"
                    , "5003": "リビングアート"
                    , "5749": "うちなーらいふ"
                    , "6633": "住まいる岡山"
                    , "6634": "不動産ニュース香川"
                    , "6635": "カサブランカ"
                    , "6703": "たっけんネットながさき"
                    , "7785": "WEBリブインあおもり"
                    , "7786": "マンモス"
                    , "8915": "不動産ネット福井"
                    , "9994": "広島スマイミー"
                    , "11005": "すまいず"
                    , "12120": "株式会社日住サービス"
                    , "12496": "平和不動産販売"
                    , "14260": "自社コード"
                    , "17530": "Read"
                    , "17606": "山陰不動産ナビ"
                    , "17757": "健美家"
                    , "17908": "41-23よい不動産.com"
                    , "18363": "一栄不動産開発"
                    , "18364": "ウチダレック"
                    , "18365": "ハウスドゥ 米子"
                    , "18366": "(有)不動産情報マイホーム"
                    , "18367": "ケンズホーム"
                    , "18368": "センチュリー21 米子"
                    , "18369": "ホームメイト 米子"
                    , "18370": "アイエステート"
                    , "18524": "ノムコム"
                    , "18525": "東急リバブル"
                    , "22506": "不動産連合隊"
                    , "23845": "HOMES(nifty不動産)"
                    , "24024": "朋友商事"
                    , "24025": "木本商事"
                    , "24026": "ファノス"
                    , "27417": "Goohome(グーホーム)"
                }
                , "preset_value": "588"
                , "table_key": "object_incompany"
            }, 'extraction_media_url': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "URL"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_incompany"
            }, 'insert_user_name': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "登録者"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_incompany"
            }, 'extraction_media_no': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "掲載元物件番号"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_incompany"
            }, 'extraction_media_date': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "抽出日"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "calendar": {}
                , "table_key": "object_incompany"
            }, 'extraction_media_kind': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "種別(新規/価改/更新)"
                , "options": {
                    "465": "指定なし"
                    , "466": "新規"
                    , "467": "価改"
                    , "468": "更新"
                }
                , "preset_value": "465"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_incompany"
            }, 'rank': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "物件評価ランク"
                , "options": {
                    "240": "指定なし"
                    , "241": "AAA"
                    , "242": "AA"
                    , "243": "A"
                }
                , "preset_value": "240"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_incompany"
            }, 'incompany_status': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "進捗"
                , "options": {
                    "407": "指定なし"
                    , "408": "新規登録"
                    , "409": "連絡待ち（売主）"
                    , "410": "連絡待ち（業者）"
                    , "411": "資料待ち"
                    , "412": "画像待ち"
                    , "413": "連携サイト入力待ち"
                    , "414": "連携サイト部屋入力待ち"
                    , "415": "連携サイト入力済"
                    , "416": "削除済"
                    , "19097": "ダイレクト登録"
                }
                , "preset_value": "407"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_incompany"
            }, 'confirm_date': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "物件確認日"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "calendar": {}
                , "table_key": "object_incompany"
            }, 'confirm_person': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "物件確認担当者"
                , "options": {
                    "26604": "指定なし"
                    , "26605": "担当者1"
                    , "26606": "担当者2"
                    , "26607": "担当者3"
                    , "26608": "担当者4"
                }
                , "preset_value": "26604"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_incompany"
            }, 'introduction': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "自社紹介"
                , "options": {
                    "1": "指定なし"
                    , "2": "○"
                    , "3": "×"
                }
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_incompany"
            }, 'request_arrival_date': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "物件資料到着日"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "calendar": {}
                , "table_key": "object_incompany"
            }, 'temaki': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "てまき"
                , "options": {
                    "1": "指定なし"
                    , "2": "○"
                    , "3": "×"
                }
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_publish"
            }, 'paper': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "紙"
                , "options": {
                    "1": "指定なし"
                    , "2": "○"
                    , "3": "×"
                }
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_publish"
            }, 'portal': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "ポータル掲載"
                , "options": {
                    "1": "指定なし"
                    , "2": "○"
                    , "3": "×"
                }
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_publish"
            }, 'own_ad_hp': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "自社HP掲載"
                , "options": {
                    "1": "指定なし"
                    , "2": "○"
                    , "3": "×"
                }
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_publish"
            }, 'my_hp': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "自社HPに掲載する"
                , "options": {
                    "1": "指定なし"
                    , "2": "○"
                    , "3": "×"
                }
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_publish"
            }, 'my_photo': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "自社写真"
                , "options": {
                    "1": "指定なし"
                    , "2": "○"
                    , "3": "×"
                }
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_incompany"
            }, 'intermediary_agent_name': {
                "tag": "TEXTAREA"
                , "key": "元付業者"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_incompany"
            }, 'intermediary_agent_tel': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "元付電話番号"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_incompany"
            }, 'intermediary_agent_person': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "元付担当者"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "table_key": "object_incompany"
            }, 'bikou_input_no': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "備考・登録No"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_incompany"
            }, 'city_gas': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "都市ガス"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'propane_gas_concentration': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "プロパンガス（集中）"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'propane_gas_separate': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "プロパンガス（個別）"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'well': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "井戸"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'waterwork': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "上水道"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
            }, 'gesuidou': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "下水道"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'electricit': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "電気"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'jyoukasou_shuuchuu': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "浄化槽（集中）"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'jyoukasou_kobetsu': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "浄化槽（個別）"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'sokkou': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "側溝"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'kumitori': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "汲取"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'ceiling_storage': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "天井収納"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'catv': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "CATV"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'all_electric': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "オール電化"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'cs': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "CS"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'roof_balcony': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "ルーフバルコニー"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'floor_heat': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "床暖房"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'hori_gotatsu': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "掘りごたつ"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'system_kitchen': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "システムキッチン"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'counter_kitchen': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "カウンターキッチン"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'ih_cooking_heater': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "IHクッキングヒーター"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'tableware_wash': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "食器洗浄乾燥機"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'shampoo_dresser': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "シャンプードレッサー"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'bathroom_dryer': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "浴室乾燥機"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'interphone': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "モニタ付インターホン"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'bidet': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "ウォシュレット"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'closet': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "ウォークインクローゼット"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'under_floor_storage': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "床下収納"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'grenier': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "グルニエ（屋根裏部屋）"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'double_glass': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "複層ガラス"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'elevator': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "エレベーター"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'aircondition': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "エアコン"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'cooling': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "冷房"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'heating': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "暖房"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'hot_water_supply': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "給湯"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'storage_space': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "収納スペース"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'cable_broadcast': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "有線放送"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'oidaki': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "追焚機能"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'indoor_wash': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "室内洗濯機置場"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'loft': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "ロフト"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'terrace': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "テラス"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'private_garden': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "専用庭"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'auto_lock': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "オートロック"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'trunk_room': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "トランクルーム"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'delivery_box': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "宅配BOX"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'bicycle_parking': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "駐輪場"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'disposer': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "ディスポーザー"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'two_side_balcony': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "2面バルコニー"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'three_side_balcony': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "3面バルコニー"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'two_toilet': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "トイレ2ヶ所"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'basement': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "地下室"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'parking_1box': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "1BOX駐車可"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_equipment"
            }, 'ownership': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "所有種別(自社/他社)"
                , "options": {
                    "439": "指定なし"
                    , "440": "自社"
                    , "441": "他社"
                }
                , "preset_value": "439"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_trader"
            }, 'trade_status': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "取引態様1"
                , "options": {
                    "429": "指定なし"
                    , "430": "売主"
                    , "431": "代理"
                    , "432": "専任"
                    , "433": "一般"
                    , "434": "専属専任"
                    , "435": "媒介"
                }
                , "preset_value": "429"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_trader"
            }, 'own_trade_status': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "自社取引態様"
                , "options": {
                    "429": "指定なし"
                    , "430": "売主"
                    , "431": "代理"
                    , "432": "専任"
                    , "433": "一般"
                    , "434": "専属専任"
                    , "435": "媒介"
                }
                , "preset_value": "429"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_trader"
            }, 'salesperson': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "情報取得者(自社)"
                , "options": {
                    "26601": "指定なし"
                    , "26602": "営業担当1"
                    , "26603": "営業担当2"
                }
                , "preset_value": "26601"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_trader"
            }, 'fee_format': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "元付式"
                , "options": {
                    "357": "指定なし"
                    , "358": "分かれ"
                    , "359": "なし"
                    , "360": "3%+6万"
                    , "361": "率のみ"
                    , "362": "金額"
                    , "363": "率+金"
                }
                , "preset_value": "357"
                , "help": "これはヘルプ用のテキストです"
                , "table_key": "object_trader"
            }, 'fee_ratio': {
                "tag": "INPUT"
                , "type": "number"
                , "step": 0.01
                , "key": "元付率"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "unit": {
                    "txt": "%"
                    , "attr": {

                    }
                }
                , "table_key": "object_trader"
            }, 'fee_price': {
                "tag": "INPUT"
                , "type": "number"
                , "step": 0.01
                , "key": "元付額"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": "1.5"
                , "unit": {
                    "txt": "万円"
                    , "attr": {

                    }
                }

                , "table_key": "object_trader"
            }, 'address_name': {
                "tag": "INPUT"
                , "type": "text"
                , "key": ""
                , "preset_value": ""
                , "placeholder": ""
                , "help": "これはヘルプ用のテキストです"
            }, 'gmap_zoom_lvl': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "ズーム"
                , "options": {
                    "10": "Lv10:10km"
                    , "11": "Lv11:5km"
                    , "12": "Lv12:2km"
                    , "13": "Lv13:1km"
                    , "14": "Lv14:500m"
                    , "15": "Lv15:200m"
                    , "16": "Lv16:200m"
                    , "17": "Lv17:100m"
                    , "18": "Lv18:50m"
                    , "19": "Lv19:20m"
                    , "": "指定なし"
                }
                , "preset_value": ""
            }, 'bundle_kind': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "一括一部"
                , "options": {
                    "244": "指定なし"
                    , "245": "一括"
                    , "246": "一部"
                }
                , "preset_value": "244"
            }, 'building_no': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "建物番号"
                , "preset_value": ""
                , "placeholder": ""
                , "help": "これはヘルプ用のテキストです"
            }, 'optimum_use': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "最適用途"
                , "options": {
                    "382": "指定なし"
                    , "383": "住宅用地"
                    , "384": "マンション用地"
                    , "385": "ビル用地"
                    , "386": "店舗用地"
                    , "387": "工業用地"
                    , "388": "配送センター"
                    , "389": "営業所"
                    , "390": "保養所"
                    , "391": "事務所用地"
                    , "392": "別荘用地"
                    , "393": "倉庫用地"
                    , "394": "資材置場用地"
                    , "395": "家庭菜園用地"
                    , "396": "アパート用地"
                    , "397": "社宅社員寮"
                    , "398": "病院診療所"
                    , "399": "畑・農地"
                    , "400": "事業用地"
                    , "401": "駐車場用地"
                    , "402": "リゾート向き"
                }
                , "preset_value": "382"
            }, 'optimum_use2': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "最適用途2"
                , "options": {
                    "382": "指定なし"
                    , "383": "住宅用地"
                    , "384": "マンション用地"
                    , "385": "ビル用地"
                    , "386": "店舗用地"
                    , "387": "工業用地"
                    , "388": "配送センター"
                    , "389": "営業所"
                    , "390": "保養所"
                    , "391": "事務所用地"
                    , "392": "別荘用地"
                    , "393": "倉庫用地"
                    , "394": "資材置場用地"
                    , "395": "家庭菜園用地"
                    , "396": "アパート用地"
                    , "397": "社宅社員寮"
                    , "398": "病院診療所"
                    , "399": "畑・農地"
                    , "400": "事業用地"
                    , "401": "駐車場用地"
                    , "402": "リゾート向き"
                }
                , "preset_value": "382"
                , "help": "これはヘルプ用のテキストです"
            }, 'divide': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "分割可"
                , "preset_value": "1"
            }, 'three_parking': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "駐車場3台分"
                , "preset_value": "1"
            }, 'resort': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "リゾート向き"
                , "preset_value": "1"
            }, 'material': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "参考資料"
                , "preset_value": "1"
            }, 'purpose_resort': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "リゾート物件"
                , "preset_value": "1"
            }, 'purpose_benefit': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "収益物件"
                , "preset_value": "1"
            }, 'login': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "非掲載"
                , "preset_value": "1"
            }, 'memo': {
                "tag": "TEXTAREA"
                , "key": "メモ"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": "これはメモです。"
            }, 'open_flg': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "公開"
                , "options": {
                    "379": "指定なし"
                    , "380": "公開"
                    , "381": "終了"
                }
                , "preset_value": "379"
                , "help": "これはヘルプ用のテキストです"
            }, 'publish_end': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "掲載終了日"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "calendar": {}
            }, 'intermediary_agent_num': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "媒介業者番号"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'intermediary_agent_jyuusho': {
                "tag": "TEXTAREA"
                , "key": "媒介業者住所"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'intermediary_agent_fax': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "媒介業者FAX"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'request1': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "1回目"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'request1_person': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "1回目"
                , "options": {
                    "26604": "指定なし"
                    , "26605": "担当者1"
                    , "26606": "担当者2"
                    , "26607": "担当者3"
                    , "26608": "担当者4"
                }
                , "preset_value": "26604"
                , "help": "これはヘルプ用のテキストです"
            }, 'request2': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "2回目"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'request2_person': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "2回目"
                , "options": {
                    "26604": "指定なし"
                    , "26605": "担当者1"
                    , "26606": "担当者2"
                    , "26607": "担当者3"
                    , "26608": "担当者4"
                }
                , "preset_value": "26604"
                , "help": "これはヘルプ用のテキストです"
            }, 'request3': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "3回目"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'request3_person': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "3回目"
                , "options": {
                    "26604": "指定なし"
                    , "26605": "担当者1"
                    , "26606": "担当者2"
                    , "26607": "担当者3"
                    , "26608": "担当者4"
                }
                , "preset_value": "26604"
                , "help": "これはヘルプ用のテキストです"
            }, 'ad_ok': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "広告可能"
                , "options": {
                    "1": "指定なし"
                    , "2": "○"
                    , "3": "×"
                }
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""

            }, 'ad1': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "広告1回目"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'ad2': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "広告2回目"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'ad3': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "広告3回目"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'photo': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "広告（写真）"
                , "options": {
                    "1": "指定なし"
                    , "2": "○"
                    , "3": "×"
                }
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
            }, 'ad_partner': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "相手"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
            }, 'car_parking': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "普通車可台"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
            }, 'car_parking_num': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "普通車駐車可能台数"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "unit": {
                    "txt": "台"
                    , "attr": {

                    }
                }

            }, 'kcar_parking': {
                "tag": "INPUT"
                , "type": "checkbox"
                , "key": "軽自動車可台"
                , "preset_value": "1"
                , "help": "これはヘルプ用のテキストです"
            }, 'kcar_parking_num': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "軽自動車駐車可能台数"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
                , "unit": {
                    "txt": "台"
                    , "attr": {

                    }
                }

            }, 'media_trade_status': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "取引態様"
                , "options": {
                    "489": "指定なし"
                    , "490": "売主"
                    , "491": "代理"
                    , "492": "専任"
                    , "493": "一般"
                    , "494": "専属専任"
                    , "495": "媒介"
                }
                , "preset_value": "489"
                , "help": "これはヘルプ用のテキストです"
            }, 'seller_report': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "売主報告"
                , "options": {
                    "543": "指定なし"
                    , "544": "メール"
                    , "545": "郵送"
                    , "546": "持参"
                }
                , "preset_value": "543"
                , "help": "これはヘルプ用のテキストです"
            }, 'seller_num': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "売主番号"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'seller_name': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "売主名称"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'seller_tel': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "売主電話"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "placeholder": ""
            }, 'fee_kind': {
                "tag": "SELECT"
                , "type": "options"
                , "key": "手数料種別"
                , "options": {
                    "217": "指定なし"
                    , "218": "元付（自社物）"
                    , "219": "客付（業物）"
                }
                , "preset_value": "217"
                , "help": "これはヘルプ用のテキストです"
            }, 'insert_time': {
                "tag": "INPUT"
                , "type": "text"
                , "key": "入力日"
                , "preset_value": ""
                , "help": "これはヘルプ用のテキストです"
                , "calendar": {}
            }}



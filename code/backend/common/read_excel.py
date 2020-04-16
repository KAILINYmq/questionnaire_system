import os 
import common.验证
from config import wfjr_col
from common.验证 import float_to_str


def excel_JY(data, excel_path, jwt_name):
    """
    获取eccel表值进行验证
    :return:
    """
    # 1.数据格式化
    excel1 = data.sheet_by_index(0)
    excel2 = data.sheet_by_index(1)
    excel1_data = []
    excel2_data = []
    excel1_data_dict = {}
    excel2_data_dict = {}
    try:
        # 1.获取人工成本表
        # for i in range(1, excel1.nrows):
        for i in range(1, 15):
            excel1_data += list(filter(None, excel1.row_values(rowx=i)))
        # 企 业 从 业 人 员 平 均 人 数
        key = list(filter(None, excel1.row_values(rowx=13)))[0]
        data = list(filter(None, excel1.row_values(rowx=13)))[1]
        excel1_data_dict.setdefault(key, data)
        # 在岗人数
        key = list(filter(None, excel1.row_values(rowx=14)))[0]
        data = list(filter(None, excel1.row_values(rowx=14)))[1]
        excel1_data_dict.setdefault(key, data)
        # 企业主要经济指标及企业人工成本指标
        for i in range(20, 35):
            key = list(filter(None, excel1.row_values(rowx=i)))[0]
            data = ''
            try:
                data = list(filter(None, excel1.row_values(rowx=i)))[3]
            except Exception as e:
                data = 1
            excel1_data_dict.setdefault(key, data)
        # 获取{}
        for i in range(0, len(excel1_data), 2):
            excel1_data_dict[excel1_data[i]] = excel1_data[i + 1]
        # 2.获取从业人员表
        for i in range(3, excel2.nrows):
            page_data = {}
            data1 = []
            excel2_data = list(filter(None, excel2.row_values(rowx=i)))
            for j in range(0, 16):
                key = str(list(filter(None, excel2.row_values(rowx=1)))[j]).replace("\n", "")
                try:
                    data1 = excel2_data[j]
                except Exception as e:
                    data1 = 0
                page_data[key] = data1
            excel2_data_dict[str(i)] = page_data
    except Exception as e:
        os.remove(excel_path)
        excel1_data_dict = None
        excel2_data_dict = None
        return excel1_data_dict, excel2_data_dict, None

    try:
        # 3.校验人工成本表数据
        if jwt_name != str(excel1_data_dict["01 统一社会信用代码："]):
            os.remove(excel_path)

            return None, None, f"上传的统一社会信用代码与登录的账户不符, 期待{jwt_name}, 得到{excel1_data_dict['01 统一社会信用代码：']}"
        common.验证.验证_法人单位名称_错误(excel1_data_dict["02 法人单位名称："])
        common.验证.验证_法定代表人_单位负责人_错误(excel1_data_dict["03 法定代表人 （单位负责人）："])
        common.验证.验证_固话_错误(excel1_data_dict["04 联系方式：固定电话："])
        common.验证.验证_手机_错误(excel1_data_dict["移动电话："])
        common.验证.验证_组织机构代码_错误(excel1_data_dict["组织机构代码："])
        common.验证.验证_企业所在地行政区划代码_错误(excel1_data_dict["05 企业所在地行政区划代码："])
        common.验证.验证_单位隶属关系_错误(excel1_data_dict["06 单位隶属关系(仅限国有单位填写)："])
        common.验证.验证_行业类别代码_错误(excel1_data_dict["07 行业类别代码："])
        common.验证.验证_企业规模_错误(excel1_data_dict["08 企业规模："])
        common.验证.验证_登记注册类型_错误(excel1_data_dict["09 登记注册类型："])
        common.验证.验证_平均人数_错误(excel1_data_dict["10 企 业 从 业 人 员 平 均 人 数："])
        common.验证.验证_在岗人数_错误(excel1_data_dict["      ，其中：（1）在岗职工："])
        common.验证.验证_销售_营业_收入_错误(excel1_data_dict["销售（营业）收入"])
        common.验证.验证_利润总额_错误(excel1_data_dict["利润总额"])
        common.验证.验证_固定资产折旧_错误(excel1_data_dict["固定资产折旧"])
        common.验证.验证_主营业务税金及附加_错误(excel1_data_dict["主营业务税金及附加"])
        common.验证.验证_人工成本总计_错误(excel1_data_dict["人工成本总计"])
        common.验证.验证_从业人员工资总额_错误(excel1_data_dict["从业人员工资总额"])
        common.验证.验证_在岗职工工资总额_错误(excel1_data_dict["    其中：在岗职工工资总额"])
        common.验证.验证_劳务派遣人员工资总额_错误(excel1_data_dict["         劳务派遣人员工资总额"])
        common.验证.验证_福利费用_错误(excel1_data_dict["福利费用"])
        common.验证.验证_教育经费_错误(excel1_data_dict["教育经费"])
        common.验证.验证_保险费用_错误(excel1_data_dict["保险费用"])
        common.验证.验证_劳动保护费用_错误(excel1_data_dict["劳动保护费用"])
        common.验证.验证_住房费用_错误(excel1_data_dict["住房费用"])
        common.验证.验证_其他人工成本_错误(excel1_data_dict["其他人工成本"])
        # 4. 校验从业人员表数据
        for i in range(3, excel2.nrows):
            common.验证.验证_职工代码_错误(excel2_data_dict[str(i)]['职工代码'])
            common.验证.验证_性别_错误(excel2_data_dict[str(i)]['性别'])
            common.验证.验证_出生年份_错误(int(excel2_data_dict[str(i)]['出生年份']))
            common.验证.验证_学历_错误(excel2_data_dict[str(i)]['学历'])
            common.验证.验证_参加工作年份_错误(int(excel2_data_dict[str(i)]['参加工作年份']))
            common.验证.验证_职业_错误(excel2_data_dict[str(i)]['职业'])
            common.验证.验证_管理岗位_专业技术职称_职业技能等级_错误(excel2_data_dict[str(i)]['管理岗位/专业技术职称/职业技能等级'])
            common.验证.验证_用工形式_错误(excel2_data_dict[str(i)]['用工形式'])
            common.验证.验证_劳动合同类型_错误(excel2_data_dict[str(i)]['劳动合同类型'])
            common.验证.验证_全年周平均工作小时数_错误(int(excel2_data_dict[str(i)]['全年周平均工作小时数']))
            common.验证.验证_是否工会会员_错误(excel2_data_dict[str(i)]['是否工会会员'])
            common.验证.验证_全年工资报酬合计_错误(int(excel2_data_dict[str(i)]['全年工资报酬合计']))
            common.验证.验证_基本工资_错误(int(excel2_data_dict[str(i)]['基本工资（类）']))
            common.验证.验证_绩效工资_错误(int(excel2_data_dict[str(i)]['绩效工资（类)']))
            common.验证.验证_津补贴_错误(int(excel2_data_dict[str(i)]['津补贴（类）']))
            common.验证.验证_加班加点工资_错误(int(excel2_data_dict[str(i)]['加班加点工资']))
    except Exception as e:
        excel1_data_dict = None
        excel2_data_dict = None
        return excel1_data_dict, excel2_data_dict, str(e.args)

    # 3.返回数据
    os.remove(excel_path)
    return excel1_data_dict, excel2_data_dict, None

def excel_data_save(excel1_data_dict, excel2_data_dict, jwt_name):
    """
    获取eccel数据入库
    :return:
    """
    # 1.保存数据
    print(excel1_data_dict, excel2_data_dict, jwt_name)
    try:
        wfjr_col.replace_one(
            {"统一社会信用代码": jwt_name},
            {
                "统一社会信用代码": float_to_str(excel1_data_dict['01 统一社会信用代码：']),
                "组织机构代码": float_to_str(excel1_data_dict['组织机构代码：']),
                "法人单位名称": float_to_str(excel1_data_dict['02 法人单位名称：']),
                "法定代表人 （单位负责人）": float_to_str(excel1_data_dict['03 法定代表人 （单位负责人）：']),
                "联系方式": {
                    "固话": float_to_str(excel1_data_dict['04 联系方式：固定电话：']),
                    "手机": float_to_str(excel1_data_dict['移动电话：'])
                },
                "企业所在地行政区划代码": str(excel1_data_dict['05 企业所在地行政区划代码：']),
                "单位隶属关系": str(excel1_data_dict['06 单位隶属关系(仅限国有单位填写)：']),
                "行业类别代码": str(excel1_data_dict['07 行业类别代码：']),
                "企业规模": str(excel1_data_dict['08 企业规模：']),
                "登记注册类型": str(excel1_data_dict['09 登记注册类型：']),
                "企业从业人员平均人数": int(excel1_data_dict['10 企 业 从 业 人 员 平 均 人 数：']),
                "销售（营业）收入": str(excel1_data_dict['销售（营业）收入']),
                "利润总额": str(excel1_data_dict['利润总额']),
                "固定资产折旧": str(excel1_data_dict['固定资产折旧']),
                "主营业务税金及附加": str(excel1_data_dict['主营业务税金及附加']),
                "成本费用总额": str(excel1_data_dict['成本费用总额']),
                "人工成本总计": str(excel1_data_dict['人工成本总计']),
                "从业人员工资总额": str(excel1_data_dict['从业人员工资总额']),
                "福利费用": str(excel1_data_dict['福利费用']),
                "劳务派遣人员工资总额": str(excel1_data_dict['         劳务派遣人员工资总额']),
                "在岗职工工资总额": int(excel1_data_dict['    其中：在岗职工工资总额']),
                "教育经费": str(excel1_data_dict['教育经费']),
                "保险费用": str(excel1_data_dict['保险费用']),
                "劳动保护费用": str(excel1_data_dict['劳动保护费用']),
                "住房费用": str(excel1_data_dict['住房费用']),
                "其他人工成本": str(excel1_data_dict['其他人工成本']),
                "从业人员工资报酬": excel2_data_dict,
            },
            upsert=True
        )
    except Exception as e:
        print(e)
        return False

    # 2.返回数据
    return True
import pytest
from static_data import data


def 长度判定(
    x: str,
    field_name: str,
    max_len: int = None,
    min_len: int = None,
    max_open = True,
    min_open = True,
):
    if max_len is not None:
        if ((not len(x) < max_len) if max_open else (not len(x) <= max_len)):
            exception_text = "{0}的长度必须小于{2}{1}".format(
                field_name, max_len, "等于" if not max_open else ""
            )
            raise Exception(exception_text)
    if min_len is not None:
        if ((not len(x) > min_len) if min_open else (not len(x) >= min_len)):
            exception_text = "{0}的长度必须大于{2}{1}".format(
                field_name, min_len, "等于" if not min_open else ""
            )
            raise Exception(exception_text)

def 等长判定(
    x: str,
    field_name: str,
    length_first: int,
    length_second: int = None
):
    if length_second is None:
        if ((not len(x) == length_first)):
            exception_text = "{0}的长度必须等于{1}".format(
                field_name, length_first
            )
            raise Exception(exception_text)

    if length_second is not None:
        if ((len(x) != length_first) & (len(x) != length_second)):
            exception_text = "{0}的长度必须等于{1}或者{2}".format(
                field_name, length_first,length_second
            )
            raise Exception(exception_text)

def 值判定(
    x: int,
    field_name: str,
    max_len: int = None,
    min_len: int = None,
    max_open = True,
    min_open = True
):
    if (min_len is not None) & (max_len is not None):
        if (not (x >= min_len) & (x <= max_len)):
            exception_text = "{0}必须在{1}和{2}之间".format(
                field_name, min_len, max_len
            )
            raise Exception(exception_text)
    if max_len is not None:
        if ((not x < max_len) if max_open else (not x <= max_len)):
            exception_text = "{0}必须小于{2}{1}".format(
                field_name, max_len, "等于" if not max_open else ""
            )
            raise Exception(exception_text)
    if min_len is not None:
        if ((not x > min_len) if min_open else (not x >= min_len)):
            exception_text = "{0}必须大于{2}{1}".format(
                field_name, min_len, "等于" if not min_open else ""
            )
            raise Exception(exception_text)
   
       
  
def 非空判定(
    x: str,
    field_name: str
):
    if x == "":
        exception_text = "{0}不可为空".format(field_name)
        raise Exception(exception_text)
def 存在性判定(
    x: str,
    belong_name: str,
    field_name: str
):
    assert belong_name in data
    if x not in data[belong_name]:
        exception_text = "{0}必须在{1}列表中".format(
            field_name, belong_name
        )
        raise Exception(exception_text)


def 验证_固话_错误(x: str):
    长度判定(
        x,
        field_name="固定电话",
        min_len=7,
        max_len=7+5,
        max_open=False,
        min_open=False
    )
    
def 验证_手机_错误(x: str):
    等长判定(
        x,
        field_name="手机号码",
        length_first=11
    )

def 验证_平均人数_错误(x: int):
    值判定(
        x,
        field_name="平均人数",
        min_len=0
    )

def 验证_在岗人数_错误(x: int):
    值判定(
        x,
        field_name="在岗人数",
        min_len=0
    )

def 验证_劳务派遣人数_错误(x: int):
    值判定(
        x,
        field_name="劳务派遣人数",
        min_len=0,
        min_open=False
    )

def 验证_从业人员工资总额_错误(x: int):
    值判定(
        x,
        field_name="从业人员工资总额",
        min_len=0,
    )

def 验证_在岗职工工资总额_错误(x: int):
    值判定(
        x,
        field_name="在岗职工工资总额",
        min_len=0,
    )

def 验证_劳务派遣人员工资总额_错误(x: int):
    值判定(
        x,
        field_name="劳务派遣人员工资总额",
        min_len=0,
        min_open=False
    )

def 验证_统一社会信用代码_错误(x: str):
    等长判定(
        x,
        field_name="统一社会信用代码",
        length_first=18,
        length_second=9
    )

def 验证_组织机构代码_错误(x: str):
    等长判定(
        x,
        field_name="组织机构代码",
        length_first=9
    )

def 验证_法人单位名称_错误(x: str):
    非空判定(
        x,
        field_name="法人单位名称",
    )

def 验证_法定代表人_单位负责人_错误(x: str):
    非空判定(
        x,
        field_name="法定代表人（单位负责人）",
    )

def 验证_企业所在地行政区划代码_错误(x: str):
    存在性判定(
        x,
        field_name="企业所在地行政区划代码",
        belong_name="企业所在地行政区划代码s"
    )

def 验证_单位隶属关系_错误(x: str):
    存在性判定(
        x,
        field_name="单位隶属关系",
        belong_name="单位隶属关系s"
    )

def 验证_行业类别代码_错误(x: str):
    存在性判定(
        x,
        field_name="行业类别代码",
        belong_name="行业类别代码s"
    )

def 验证_企业规模_错误(x: str):
    存在性判定(
        x,
        field_name="企业规模",
        belong_name="企业规模s"
    )

def 验证_登记注册类型_错误(x: str):
    存在性判定(
        x,
        field_name="登记注册类型",
        belong_name="登记注册类型s"
    )

def 验证_销售_营业_收入_错误(x: int):
    值判定(
        x,
        field_name="销售（营业）收入",
        min_len=0,
    )

def 验证_利润总额_错误(x: int):
    值判定(
        x,
        field_name="利润总额",
        min_len=0,
    )

def 验证_固定资产折旧_错误(x: int):
    值判定(
        x,
        field_name="固定资产折旧",
        min_len=0,
        min_open=False
    )

def 验证_主营业务税金及附加_错误(x: int):
    值判定(
        x,
        field_name="主营业务税金及附加",
        min_len=0,
        min_open=False
    )

def 验证_人工成本总计_错误(x: int):
    值判定(
        x,
        field_name="人工成本总计",
        min_len=0
    )

def 验证_福利费用_错误(x: int):
    if x != None:
        值判定(
            x,
            field_name="福利费用",
            min_len=0
        )

def 验证_保险费用_错误(x: int):
    值判定(
        x,
        field_name="保险费用",
        min_len=0
    )

def 验证_职工代码_错误(x: str):
    非空判定(
        x,
        field_name="职工代码",
    )

def 验证_性别_错误(x: str):
    存在性判定(
        x,
        field_name="性别",
        belong_name="性别s"
    )

def 验证_出生年份_错误(x: int):
    值判定(
        x,
        field_name="出生年份",
        min_len=1956,
        max_len=2006,
        max_open=False,
        min_open=False
    )

def 验证_学历_错误(x: str):
    存在性判定(
        x,
        field_name="学历",
        belong_name="学历s"
    )

def 验证_参加工作年份_错误(x: int):
    值判定(
        x,
        field_name="参加工作年份",
        min_len=1965,
        max_len=2017,
        max_open=False,
        min_open=False
    )

def 验证_职业_错误(x: str):
    存在性判定(
        x,
        field_name="职业",
        belong_name="职业s"
    )

def 验证_管理岗位_专业技术职称_职业技能等级_错误(x: str):
    存在性判定(
        x,
        field_name="管理岗位/专业技术职称/职业技能等级",
        belong_name="管理岗位/专业技术职称/职业技能等级s"
    )

def 验证_用工形式_错误(x: str):
    存在性判定(
        x,
        field_name="用工形式",
        belong_name="用工形式s"
    )

def 验证_劳动合同类型_错误(x: str):
    存在性判定(
        x,
        field_name="劳动合同类型",
        belong_name="劳动合同类型s"
    )

def 验证_全年周平均工作小时数_错误(x: int):
    值判定(
        x,
        field_name="全年周平均工作小时数",
        min_len=21,
        max_len=112,
        max_open=False,
        min_open=False
    )

def 验证_是否工会会员_错误(x: str):
    非空判定(
        x,
        field_name="是否工会会员",
    )

def 验证_全年工资报酬合计_错误(x: int):
    值判定(
        x,
        field_name="全年工资报酬合计",
        min_len=12000,
        max_len=5000000,
        max_open=False,
        min_open=False
    )

def 检验(value: str, data_type: str):
    func_map = [
        "固话", 
        "手机",
        "平均人数",
        "在岗人数",
        "劳务派遣人数",
        "从业人员工资总额",
        "在岗职工工资总额",
        "劳务派遣人员工资总额",
        "统一社会信用代码",
        "组织机构代码",
        "法人单位名称",
        "法定代表人_单位负责人",
        "企业所在地行政区划代码",
        "单位隶属关系",
        "行业类别代码",
        "企业规模",
        "登记注册类型",
        "销售_营业_收入",
        "利润总额",
        "固定资产折旧",
        "主营业务税金及附加",
        "人工成本总计",
        "福利费用",
        "保险费用",
        "职工代码",
        "性别",
        "出生年份",
        "学历",
        "参加工作年份",
        "职业",
        "管理岗位_专业技术职称_职业技能等级",
        "用工形式",
        "劳动合同类型",
        "全年周平均工作小时数",
        "是否工会会员",
        "全年工资报酬合计",
        "基本工资"
    ]
    assert data_type in func_map

    ret = {
        "错误": "",
        "警告": ""
    }
    for check_type in ["错误"]:
        try:

            func_name = f"验证_{data_type}_{check_type}"
            func = eval(func_name)
            if func:
                func(value)
        except Exception as e:
            if check_type == '警告':
                e = f"请确认{str(e)}吗?"
                e = e.replace('必须', '真的')
            ret[check_type] = str(e)

    return ret

def test_手机():
    ret = 检验("18051770039", "手机")
    assert ret['错误'] == ''

    ret = 检验("1805177003", "手机")
    assert ret['错误'] == '手机号码的长度必须等于11'

def test_固话():
    ret = 检验("5741769", "固话")
    assert ret['错误'] == ''

    ret = 检验("57417691", "固话")
    assert ret['错误'] == ''

    ret = 检验("1231235741769", "固话")
    assert ret['错误'] == '固定电话的长度必须小于等于12'

def test_平均人数():
    ret = 检验(12345, "平均人数")
    assert ret['错误'] == ''

    ret = 检验(0, "平均人数")
    assert ret['错误'] == '平均人数必须大于0'

def test_在岗人数():
    ret = 检验(12345, "在岗人数")
    assert ret['错误'] == ''

    ret = 检验(0, "在岗人数")
    assert ret['错误'] == '在岗人数必须大于0'

def test_劳务派遣人数():
    ret = 检验(12345, "劳务派遣人数")
    assert ret['错误'] == ''

    ret = 检验(0, "劳务派遣人数")
    assert ret['错误'] == ''

    ret = 检验(-1, "劳务派遣人数")
    assert ret['错误'] == '劳务派遣人数必须大于等于0'

def test_从业人员工资总额():
    ret = 检验(12345, "从业人员工资总额")
    assert ret['错误'] == ''

    ret = 检验(0, "从业人员工资总额")
    assert ret['错误'] == '从业人员工资总额必须大于0'

def test_在岗职工工资总额():
    ret = 检验(12345, "在岗职工工资总额")
    assert ret['错误'] == ''

    ret = 检验(0, "在岗职工工资总额")
    assert ret['错误'] == '在岗职工工资总额必须大于0'

def test_劳务派遣人员工资总额():
    ret = 检验(12345, "劳务派遣人员工资总额")
    assert ret['错误'] == ''

    ret = 检验(0, "劳务派遣人员工资总额")
    assert ret['错误'] == ''

    ret = 检验(-1, "劳务派遣人员工资总额")
    assert ret['错误'] == '劳务派遣人员工资总额必须大于等于0'

def test_统一社会信用代码():
    ret = 检验("123456485159482637", "统一社会信用代码")
    assert ret['错误'] == ''

    ret = 检验("123456485", "统一社会信用代码")
    assert ret['错误'] == ''

    ret = 检验("1805177003", "统一社会信用代码")
    assert ret['错误'] == '统一社会信用代码的长度必须等于18或者9'

def test_组织机构代码():
    ret = 检验("123456485", "组织机构代码")
    assert ret['错误'] == ''

    ret = 检验("1805177003", "组织机构代码")
    assert ret['错误'] == '组织机构代码的长度必须等于9'

def test_法人单位名称():
    ret = 检验("123456485", "法人单位名称")
    assert ret['错误'] == ''

    ret = 检验("", "法人单位名称")
    assert ret['错误'] == '法人单位名称不可为空'

def test_法定代表人_单位负责人(): 
    ret = 检验("123456485", "法定代表人_单位负责人")
    assert ret['错误'] == ''

    ret = 检验("", "法定代表人_单位负责人")
    assert ret['错误'] == '法定代表人（单位负责人）不可为空'

def test_企业所在地行政区划代码():
    ret = 检验("常熟市", "企业所在地行政区划代码")
    assert ret['错误'] == ''

    ret = 检验("", "企业所在地行政区划代码")
    assert ret['错误'] == '企业所在地行政区划代码必须在企业所在地行政区划代码s列表中'

def test_单位隶属关系():
    ret = 检验("中央", "单位隶属关系")
    assert ret['错误'] == ''

    ret = 检验("", "单位隶属关系")
    assert ret['错误'] == '单位隶属关系必须在单位隶属关系s列表中'

def test_行业类别代码():
    ret = 检验("谷物种植", "行业类别代码")
    assert ret['错误'] == ''

    ret = 检验("", "行业类别代码")
    assert ret['错误'] == '行业类别代码必须在行业类别代码s列表中'

def test_企业规模():
    ret = 检验("中型企业", "企业规模")
    assert ret['错误'] == ''

    ret = 检验("", "企业规模")
    assert ret['错误'] == '企业规模必须在企业规模s列表中'

def test_登记注册类型():
    ret = 检验("国有企业（不含国有独资公司）", "登记注册类型")
    assert ret['错误'] == ''

    ret = 检验("", "登记注册类型")
    assert ret['错误'] == '登记注册类型必须在登记注册类型s列表中'

def test_销售_营业_收入():
    ret = 检验(12345, "销售_营业_收入")
    assert ret['错误'] == ''

    ret = 检验(0, "销售_营业_收入")
    assert ret['错误'] == '销售（营业）收入必须大于0'

def test_利润总额():
    ret = 检验(12345, "利润总额")
    assert ret['错误'] == ''

    ret = 检验(0, "利润总额")
    assert ret['错误'] == '利润总额必须大于0'

def test_固定资产折旧():
    ret = 检验(12345, "固定资产折旧")
    assert ret['错误'] == ''

    ret = 检验(0, "固定资产折旧")
    assert ret['错误'] == ''

    ret = 检验(-1, "固定资产折旧")
    assert ret['错误'] == '固定资产折旧必须大于等于0'

def test_主营业务税金及附加():
    ret = 检验(12345, "主营业务税金及附加")
    assert ret['错误'] == ''

    ret = 检验(0, "主营业务税金及附加")
    assert ret['错误'] == ''

    ret = 检验(-2, "主营业务税金及附加")
    assert ret['错误'] == '主营业务税金及附加必须大于等于0'

def test_人工成本总计():
    ret = 检验(12345, "人工成本总计")
    assert ret['错误'] == ''

    ret = 检验(0, "人工成本总计")
    assert ret['错误'] == '人工成本总计必须大于0'

def test_福利费用():
    ret = 检验(12345, "福利费用")
    assert ret['错误'] == ''

    ret = 检验(0, "福利费用")
    assert ret['错误'] == '福利费用必须大于0'

def test_保险费用():
    ret = 检验(12345, "保险费用")
    assert ret['错误'] == ''

    ret = 检验(0, "保险费用")
    assert ret['错误'] == '保险费用必须大于0'

def test_职工代码():
    ret = 检验("asdsfsgr", "职工代码")
    assert ret['错误'] == ''

    ret = 检验("", "职工代码")
    assert ret['错误'] == '职工代码不可为空'

def test_性别():
    ret = 检验("男", "性别")
    assert ret['错误'] == ''

    ret = 检验("", "性别")
    assert ret['错误'] == '性别必须在性别s列表中'

def test_出生年份():
    ret = 检验(2006, "出生年份")
    assert ret['错误'] == ''

    ret = 检验(1955, "出生年份")
    assert ret['错误'] == '出生年份必须在1956和2006之间'

    ret = 检验(2007, "出生年份")
    assert ret['错误'] == '出生年份必须在1956和2006之间'

def test_学历():
    ret = 检验("初中及以下", "学历")
    assert ret['错误'] == ''

    ret = 检验("", "学历")
    assert ret['错误'] == '学历必须在学历s列表中'

def test_参加工作年份():
    ret = 检验(2006, "参加工作年份")
    assert ret['错误'] == ''

    ret = 检验(1955, "参加工作年份")
    assert ret['错误'] == '参加工作年份必须在1965和2017之间'

    ret = 检验(2020, "参加工作年份")
    assert ret['错误'] == '参加工作年份必须在1965和2017之间'

def test_职业():
    ret = 检验("1060200-企业总经理", "职业")
    assert ret['错误'] == ''

    ret = 检验("", "职业")
    assert ret['错误'] == '职业必须在职业s列表中'

def test_管理岗位_专业技术职称_职业技能等级():
    ret = 检验("中层管理岗（一级部门管理岗）", "管理岗位_专业技术职称_职业技能等级")
    assert ret['错误'] == ''

    ret = 检验("", "管理岗位_专业技术职称_职业技能等级")
    assert ret['错误'] == '管理岗位/专业技术职称/职业技能等级必须在管理岗位/专业技术职称/职业技能等级s列表中'

def test_用工形式():
    ret = 检验("合同制用工", "用工形式")
    assert ret['错误'] == ''

    ret = 检验("", "用工形式")
    assert ret['错误'] == '用工形式必须在用工形式s列表中'

def test_劳动合同类型():
    ret = 检验("固定期限", "劳动合同类型")
    assert ret['错误'] == ''

    ret = 检验("", "劳动合同类型")
    assert ret['错误'] == '劳动合同类型必须在劳动合同类型s列表中'

def test_全年周平均工作小时数():
    ret = 检验(21, "全年周平均工作小时数")
    assert ret['错误'] == ''

    ret = 检验(5, "全年周平均工作小时数")
    assert ret['错误'] == '全年周平均工作小时数必须在21和112之间'

    ret = 检验(113, "全年周平均工作小时数")
    assert ret['错误'] == '全年周平均工作小时数必须在21和112之间'


def test_是否工会会员():
    ret = 检验("是", "是否工会会员")
    assert ret['错误'] == ''

    ret = 检验("", "是否工会会员")
    assert ret['错误'] == '是否工会会员不可为空'

def test_全年工资报酬合计():
    ret = 检验(5000000, "全年工资报酬合计")
    assert ret['错误'] == ''

    ret = 检验(53, "全年工资报酬合计")
    assert ret['错误'] == '全年工资报酬合计必须在12000和5000000之间'

    ret = 检验(500000000, "全年工资报酬合计")
    assert ret['错误'] == '全年工资报酬合计必须在12000和5000000之间'

if __name__ == "__main__":
    pytest.main([__file__])

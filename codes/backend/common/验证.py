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
    长度判定(
        x,
        field_name="手机号码",
        min_len=11,
        max_len=11,
        max_open=False,
        min_open=False
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
        "登记注册类型"
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
    assert ret['错误'] == '手机号码的长度必须大于等于11'

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

if __name__ == "__main__":
    pytest.main([__file__])

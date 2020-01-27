import pytest
from static_data import data


def 长度判定(
    x: str, 
    max_len: int = None,
    min_len: int = None,
    max_open = True,
    min_open = True,
):
    if max_len is not None:
        if ((not len(x) < max_len) if max_open else (not len(x) <= max_len)):
            exception_text = "{0}的长度必须小于{2}{1}".format(
                x, max_len, "等于" if not max_open else ""
            )
            raise Exception(exception_text)
    if min_len is not None:
        if ((not len(x) > min_len) if min_open else (not len(x) >= min_len)):
            exception_text = "{0}的长度必须大于{2}{1}".format(
                x, min_len, "等于" if not min_open else ""
            )
            raise Exception(exception_text)

def 值判定(
    x: int, 
    max_len: int = None,
    min_len: int = None,
    max_open = True,
    min_open = True,
):
    if max_len is not None:
        if ((not x < max_len) if max_open else (not x <= max_len)):
            exception_text = "{0}必须小于{2}{1}".format(
                x, max_len, "等于" if not max_len else ""
            )
            raise Exception(exception_text)
    if min_len is not None:
        if ((not x > min_len) if min_len else (not x >= min_len)):
            exception_text = "{0}必须小于{2}{1}".format(
                x, min_len, "等于" if not max_len else ""
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
        min_len=7,
        max_len=7+5,
        max_open=False,
        min_open=False
    )
    
def 验证_手机_错误(x: str):
    长度判定(
        x,
        min_len=11,
        max_len=11,
        max_open=False,
        min_open=False
    )

def 检验(value: str, data_type: str):
    func_map = [
        "固话", 
        "手机"
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
    assert ret['错误'] == '1805177003的长度必须大于等于11'
def test_固话():
    ret = 检验("5741769", "固话")
    assert ret['错误'] == ''

    ret = 检验("57417691", "固话")
    assert ret['错误'] == ''

    ret = 检验("1231235741769", "固话")
    assert ret['错误'] == '1231235741769的长度必须小于等于12'


if __name__ == "__main__":
    pytest.main([__file__])

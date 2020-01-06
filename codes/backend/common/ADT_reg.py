from __future__ import annotations
from typing import List, Dict, Union, Any, Tuple, Callable
from decimal import Decimal
import copy
from bson import ObjectId

from common.static_data import data
import re

FixDecimal = Decimal

base_type = {
    'bool': False,
    'int': 0,
    'str': '',
    'FixDecimal': FixDecimal(0),
    'ObjectId': ObjectId()
}


class Field:
    field_name: str = ''
    value: Any = None
    constraints: List


class Object:

    def __init__(self):
        self.members: Dict[str, List[Any, Any]] = {}
        #             key            type value
        self.name: str = ""
        self.parent: List[Union[str, Object]] = []

    def add_member(self, key: str, type_text):
        global objects
        key = key.strip()
        if type_text in base_type.keys():
            value = None
            type_text = eval(type_text)
        else:

            if '[' in type_text and ']' in type_text:
                # List[]那种
                assert type_text.strip().startswith('List')
                inner_type = re.findall(r'(?<=[[])\w+(?=[]])', type_text)
                assert len(inner_type) == 1, '不允许复合类型'
                inner_type = inner_type[0]
                assert inner_type in objects.keys()
                value = None
                type_text = List[type(objects[inner_type])]
            else:
                # 看看是不是结构体吧
                if type_text in objects:
                    # 是记录在册的结构体
                    type_text = objects[type_text]
                    value = None
                else:
                    if type_text.endswith('s'):
                        # 是属于某集合之一的
                        value = None
                    else:
                        raise Exception(f"类型不支持: {type_text}")

        self.members[key] = [type_text, value]

    def add_parent(self, text: str = None, object: Object = None):
        global objects
        assert text or object
        if text:
            assert text in objects
            object = objects[text]
        elif object:
            assert object.name in objects

        self.parent.append(object)
        self.members.update(object.members)

    def set(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.members:
                self.members[key][1] = value

    def show_info(self):
        return f'{self.name=}', f'{self.parent=}', f'{self.members=}'

    def to_dict(self):
        ret_dict = {}
        for key, (type_, value) in self.members.items():

            if type_ not in map(eval, base_type):
                # 不是基本类型
                if hasattr(type_, '_name') and type_._name == 'List':
                    # 是个list
                    ret_dict[key] = copy.deepcopy(value)
                else:
                    # 不是list之一就是结构体
                    if type_ == Any:
                        # 未指定类型, 是属于某集合之一的
                        ret_dict[key] = value
                    else:
                        # 是个结构体
                        ret_dict[key] = value.to_dict()
            else:
                ret_dict[key] = value

        return ret_dict


objects: Dict[str, Object] = {}


def new(obj: Object):
    global objects

    new_obj = Object()
    new_obj.has_new = True
    new_obj.name = obj.name
    new_obj.parent = obj.parent

    for mem_name in obj.members:
        type_, value = obj.members[mem_name]
        assert not isinstance(type, str)

        if type_ not in map(eval, base_type):
            # 不是基本类型
            if hasattr(type_, '_name') and type_._name == 'List':
                # 是个list
                new_obj.members[mem_name] = [type_, []]
            else:
                # 不是list之一就是结构体
                if hasattr(type_, 'endswith') and type_.endswith('s'):
                    # 是属于某集合之一的
                    value = None
                    new_obj.members[mem_name] = [Any, None]
                else:
                    # 是个结构体
                    # print(mem_name, type_, value)
                    type_.show_info()
                    new_obj.members[mem_name] = [type_, new(type_)]
        else:
            new_obj.members[mem_name] = [type_, value]
    return new_obj


def test_parse():
    with open('ADT.js', encoding='utf-8') as f:
        test_text = f.read()

    classes = re.findall(r'class\s+\w+.*?[{].+?[}]', test_text, re.DOTALL)
    for class_ in classes:
        print(f'{class_=}')

        object = Object()

        object_name_and_parents: list = re.findall('(?<=class).+(?={)', class_)
        if len(object_name_and_parents) == 1:
            object_name_and_parents: str = object_name_and_parents[0].strip()
            object_name, *object_parents = [i.strip() for i in object_name_and_parents.split(':')]
            object.name = object_name
            [object.add_parent(i) for i in object_parents]
        else:
            raise Exception('object_name_and_parents未匹配成功')
        print(f'{object_name_and_parents=}')

        object_body = re.search(r'((?<=[{]).+(?=[}]))', class_, re.DOTALL)
        object_body = object_body.groups() and object_body.groups()[0]
        print(f'{object_body=}')

        object_fields = re.findall(r'(?P<filed>\w+)\s*:\s*(?P<type>\w+[[]*\w*[]]*)', object_body)
        print(object_fields)
        for field_text, type_ in object_fields:
            object.add_member(field_text, type_)

        objects[object.name] = object
        print(f'{object.name=}', f'{object.parent=}', f'{object.members=}')

    obj = new(objects['CompanyInfo'])
    obj.set(统一社会信用代码=123)
    assert obj.to_dict() == {'统一社会信用代码': 123, '组织机构代码': None, '法人单位名称': None, '联系方式': {'固话': None, '手机': None},
                             '企业所在地行政区划代码': None, '单位隶属关系': None, '行业类别代码': None, '企业规模': None, '登记注册类型': None,
                             '企业从业人员信息': {'平均人数': None, '在岗人数': None, '劳务派遣人数': None},
                             '企业主要经济指标及企业人工成本指标': {
                                 '利润总额': None, '固定资产折旧': None, '主营业务税金及附加': None, '成本费用总额': None,
                                 '人工成本总计': None,
                                 '从业人员工资总额': {
                                     '从业人员工资总额': None, '在岗职工工资总额': None, '劳务派遣人员工资总额': None
                                 },
                                 '福利费用': None, '教育经费': None, '保险费用': None, '劳动保护费用': None,
                                 '住房费用': None, '其他人工成本': None
                             },
                             '从业人员工资报酬信息': [],
                             'had_commited': None}
    print(obj.to_dict())


test_parse()

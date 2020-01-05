from __future__ import annotations
from typing import List, Dict, Union, Any, Tuple, Callable
from decimal import Decimal
from common.static_data import data
import re

FixDecimal = Decimal


class Field:
    field_name: str = ''
    value: Any = None
    constraints: List

class Object:
    members: Dict[str, Tuple[Any, Any]] = {}
    #             key       type value
    name: str = ""
    parent: List[Union[str, Object]] = []


    def add_member(self, key, type_text):
        base_type = {
            bool: False,
            int: 0,
            str: '',
            FixDecimal: FixDecimal(0)
        }
        if type_text in map(str, base_type.keys()):
            type_text = eval(type_text)
            value = base_type.get(type_text, '')
        else:

            if '[' in type_text and ']' in type_text:
                assert type_text.strip().startswith('List')
                inner_type = re.findall(r'(?<=[[])\w+(?=[]])', type_text)
                assert len(inner_type) == 1, '不允许复合类型'
                inner_type = inner_type[0]
                assert inner_type in objects.keys()
                value = []
                type_text = List[objects[inner_type]]
            else:
                raise Exception("类型不支持")

        self.members[key] = (type_text, value)

    def add_parent(self, text: str=None, object: Object=None):
        global objects
        assert text or object
        if text:
            assert text in objects
            object = objects[text]
        elif object:
            assert object.name in objects
            
        self.parent.append(object)
        self.members.update(object.members)

objects: Dict[str, Object] = {}

test_text = '''
  class A : B {
      a: int
      b: List[23]
      c: str
  }
'''


def test_parse():
    test_text = '''
    class B {
        a: int
        b: List[23]
        c: str
    }

    class A : B {
        d:List[int]
    }
    class DD: A {
e: int
    }
    '''

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
        # print(f'{object_name_and_parents=}')

        object_body = re.search(r'((?<=[{]).+(?=[}]))', class_, re.DOTALL)
        object_body = object_body.groups() and object_body.groups()[0]
        # print(f'{object_body=}')

        object_fields = re.findall(r'(?P<filed>\w+)\s*:\s*(?P<type>\w+[[]*\w*[]]*)', object_body)
        # print(object_fields)
        for field in object_fields:
            object.add_member(field[0], field[1])

        objects[object.name] = object
        print(f'{object.name=}', f'{object.parent=}', f'{object.members=}')


test_parse()

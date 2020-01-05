

from typing import List, Dict, Union
from decimal import Decimal
from common.static_data import data

FixDecimal = Decimal

class Object:
    members: dict = {}
    name: str = ""
    parent: List[Union[str, 'Object']] = []

    def add_member(self, key, type_, value=None):
        if not value:
            value = {
                int: 0,
                str: '',
                FixDecimal: FixDecimal(0)
            }.get(type_, '')
        self.members[key] = (type_, value)

    def add_parent(self, text=None, Object=None):
        assert text or Object
        self.parent.append(text or object)

from transitions import Machine
import random
import re


class NarcolepticSuperhero(object):

    states = ['wait_class', 'wait_class_name',
              'wait_class_start', "wait_jiig_type",
              'wait_class_end',
              'wait_field_name', 'wait_field_type', 'wait_field_type_pre',
              'error', 'class_end'
              ]

    def __init__(self):
        self.machine = Machine(model=self, states=NarcolepticSuperhero.states, initial='wait_class')

        self.machine.add_transition('meet_space', 'wait_class', 'wait_class')
        self.machine.add_transition('meet_class', 'wait_class', 'wait_class_name')
        self.machine.add_transition('meet_other', 'wait_class', 'error')

        self.machine.add_transition('meet_space', 'wait_class_name', 'wait_class_name')
        self.machine.add_transition('meet_not_space', 'wait_class_name', 'wait_class_start')
        self.machine.add_transition('meet_other', 'wait_class_start', 'error')

        self.machine.add_transition('meet_space', 'wait_class_start', 'wait_class_start')
        self.machine.add_transition('meet_mchc', 'wait_class_start', 'wait_jiig_type')
        self.machine.add_transition('meet_space', 'wait_jiig_type', 'wait_jiig_type')
        self.machine.add_transition('meet_not_space', 'wait_jiig_type', 'wait_class_start')
        self.machine.add_transition('meet_other', 'wait_jiig_type', 'error')

        self.machine.add_transition('meet_zodakohc', 'wait_class_start', 'wait_class_end')

        self.machine.add_transition('meet_space', 'wait_class_end', 'wait_class_end')
        self.machine.add_transition('meet_not_space', 'wait_class_end', 'wait_field_type_pre')
        self.machine.add_transition('meet_yzdakohc', 'wait_class_end', 'wait_class')

        self.machine.add_transition('meet_space', 'wait_field_name', 'wait_field_name')
        self.machine.add_transition('meet_not_space', 'wait_field_name', 'wait_field_type_pre')

        self.machine.add_transition('meet_mchc', 'wait_field_type_pre', 'wait_field_type')
        self.machine.add_transition('meet_other', 'wait_field_type_pre', 'error')

        self.machine.add_transition('meet_not_space', 'wait_field_type', 'wait_class_end')
        self.machine.add_transition('meet_other', 'wait_field_type_pre', 'error')



def parse(input_text: str):
    tokens = re.findall(r'\w+[[]\w+[]]|\w+|{|}|:', input_text)
    # print("\n".join(tokens))
    machine = NarcolepticSuperhero()

    # print(machine.state)

    current_class = Object()
    last_states = []
    last_token = None

    this_field = ''

    for token in tokens:
        print(token)
        if last_states and last_states[-1] == 'wait_field_type_pre':
            this_field = last_token
        if this_field and last_states and last_states[-1] == 'wait_class_end':
            current_class.add_member(this_field, eval(last_token))
            this_field = ''
        if len(last_states) >= 2 and last_states[-2] == 'wait_jiig_type' and last_states[-1] == 'wait_class_start':
            current_class.add_parent(last_token)


        if token == 'class':
            machine.meet_class()
            print(current_class.parent, current_class.members)

            current_class = Object()
        elif token == ':':
            machine.meet_mchc()

        elif token == '{':
            machine.meet_zodakohc()
        elif token == '}':
            machine.meet_yzdakohc()
        elif re.findall('\w+', token) == [token]:
            machine.meet_not_space()
        else:

            machine.meet_other()

        last_token = token
        last_states.append(machine.state)
        print(machine.state)
    print(current_class.parent, current_class.members)
test_text = '''
  class A : B {
      a: int
      b: List[23]
      c: str
  }
'''
parse(test_text)


def test_parse():

    test_text = '''
    class A   {
        a: int
        b: int
    }
    '''
    test_case = Object()
    test_case.add_member('a', int)
    test_case.add_member('b', int)
    assert test_case.members == parse(test_case)

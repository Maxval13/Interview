from unittest import TestCase
from steck import balance


class TestStecks(TestCase):

    def test_list_true(self):
        list_true = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']
        for i in list_true:
            self.assertEqual(balance(i), 'Сбалансированно')

    def test_list_false(self):
        list_false = ['}{}', '{{[(])]}}', '[[{())}]', '(()))']
        for i in list_false:
            self.assertEqual(balance(i), 'Несбалансированно')

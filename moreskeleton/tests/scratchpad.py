import unittest


class ScratchPad(unittest.TestCase):

    def test_string_is_upper(self, string):
        self.assertTrue(string.upper() == string, True)

    def test_generic_test(self, expression, evaluation):
        self.assertTrue(eval(expression), evaluation)
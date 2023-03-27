import unittest

class TestStringFunctions(unittest.TestCase):

    def TestToUpper(self):
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertEqual(to_upper("WORLD"), "WORLD")
        self.assertEqual(to_upper("123"), "123")
        self.assertEqual(to_upper(""), "")

    def TestToLower(self):
        self.assertEqual(to_lower("hello"), "hello")
        self.assertEqual(to_lower("WORLD"), "world")
        self.assertEqual(to_lower("123"), "123")
        self.assertEqual(to_lower(""), "")

    def TestCapitalize(self):
        self.assertEqual(capitalize("hello world"), "Hello world")
        self.assertEqual(capitalize("WORLD"), "World")
        self.assertEqual(capitalize("123"), "123")
        self.assertEqual(capitalize(""), "")

if name == 'main':
    unittest.main()
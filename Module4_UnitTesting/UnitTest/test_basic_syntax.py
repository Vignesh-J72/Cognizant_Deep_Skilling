import unittest

class tester(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.islower())
    
    def test_split(self):
        word="Hello world"
        self.assertEqual(word.split(),['Hello', 'world'])

        with self.assertRaises(TypeError):
            word.split(2)

if __name__=="__main__":
    unittest.main()
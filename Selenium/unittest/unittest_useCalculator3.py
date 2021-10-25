import unittest
from test_Calculator import Calculator

#根据书本的建议一个测试类对应一个被测试功能
class TestAdd(unittest.TestCase):
    """add()测试方法"""
    def test_add_integer(self):
        """整数相加测试"""
        c = Calculator(3,5)
        self.assertEqual(c.add(),8)

    def test_add_decimals(self):
        """小数相加测试"""
        c = Calculator(1.6,6.3)
        self.assertEqual(c.add(),7.9)

    def test_add_string(self):
        """字符串相加测试"""
        c = Calculator("7","9")
        self.assertEqual(c.add(),16)

    
class TestSub(unittest.TestCase):
    """sub()方法测试"""
    def test_add_integer(self):
        """整数相减测试"""
        c = Calculator(3,5)
        self.assertEqual(c.sub(),-2)
    pass

if __name__ == '__main__':
    unittest.main()
import unittest

from test_Calculator import Calculator

#TestCase 基类，我们创建的测试类需要继承该基类
# 它可以用来创建新的测试用例
class TestCaculator(unittest.TestCase):

    #测试用例前置动作
    def setUp(self) -> None:
        print("test start:")

    #测试用例后置动作
    def tearDown(self) -> None:
        print('test end')

    #使用unitest单元测试重新编写测试用例
    def test_add(self):
        c = Calculator(5,3)
        result = c.add()
        self.assertEqual(result,8)

    def test_sub(self):
        c = Calculator(8,5)
        result = c.sub()
        self.assertEqual(result,1)

    def test_mul(self):
        c = Calculator(3,5)
        result = c.mul()
        self.assertEqual(result,15)

    def test_div(self):
        c = Calculator(10,5)
        result = c.div()
        self.assertEqual(result,2)

if __name__ == '__main__':
    #创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(TestCaculator("test_add"))
    suit.addTest(TestCaculator("test_sub"))
    suit.addTest(TestCaculator("test_mul"))
    suit.addTest(TestCaculator("test_div"))

    #创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)

    
"""
我们可以把 Fixture 看作夹心饼干外层的两片饼干，这两片饼干就是 setUp/tearDown，
中间的奶油就是测试用例。除此之外， unittest 还提供了更大范围的 Fixture，如测试类和模
块的 Fixture。
"""
"""
setUpModule/tearDownModule：在整个模块的开始与结束时被执行。
setUpClass/tearDownClass：在测试类的开始与结束时被执行。
setUp/tearDown：在测试用例的开始与结束时被执行。
"""
import unittest
def setUpModel():
    print("test model start>>>>>>>>>>>>>>>>>")

def tearDownModel():
    print("test model end>>>>>>>>>>>>>>>>>>>")

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("test class start===========>")
    
    @classmethod
    def tearDownClass(cls) -> None:
        print("test class end=============>")

    def setUp(self) -> None:
        print("test case start============>")

    def tearDown(self) -> None:
        print("test case end==============>")

    def test_case1(self):
        print("test_case:宇宙凛")
    
    def test_case2(self):
        print("test_case2:杀狐")

if __name__ == "__main__":
    unittest.main()
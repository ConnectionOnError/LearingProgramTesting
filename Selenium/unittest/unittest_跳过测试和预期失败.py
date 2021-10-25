import unittest
class MyTest(unittest.TestCase):
    
    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("FGO 宇宙凛")

    @unittest.skipIf(3 > 2,"当测试条件为真时，跳过测试")
    def test_skipIf(self):
        print("FGO 南丁格尔")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(3,3)

    @unittest.skipUnless(3 > 2,"当测试条件为真时，执行测试")
    def test_skipUnless(self):
        print("skipUnless宇宙凛")

if __name__ == "__main__":
    unittest.main()
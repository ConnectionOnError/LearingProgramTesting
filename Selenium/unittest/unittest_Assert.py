import unittest
class TestAssert(unittest.TestCase):
    #unittest断言的简单认识和学习
    def test_equal(self):
        self.assertEqual(2+2,5)
        self.assertEqual("宇宙凛","宇宙凛")
        self.assertNotEqual("伊什塔尔","宇宙凛")
    
    def test_in(self):
        self.assertIn("Fate","Fate Grand Order")
        self.assertNotIn("命运","Fate Grand Order")

    def test_true(self):
        self.assertTrue(True)
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
    
import unittest
import os
from unittest import runner
#定义测试用例的目录
test_dir = './unittest/test_case'
#导入文件失败的时候，使用getcwd看看当前文件路径，然后检查相对路径
#或者直接写成绝对路径
pwd = os.getcwd()               
print("当前运行文件路径" + pwd)

suits = unittest.defaultTestLoader.discover(test_dir,pattern='unittest*.py')

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suits)
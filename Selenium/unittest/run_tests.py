import os
import unittest
import time
from unittest import runner
from TestRunner import HTMLTestRunner

#定义测试用例的目录
test_dir = './unittest/test_case'
#导入文件失败的时候，使用getcwd看看当前文件路径，然后检查相对路径
#或者直接写成绝对路径
pwd = os.getcwd()               
print("当前运行文件路径" + pwd)

suit = unittest.defaultTestLoader.discover(test_dir,pattern='unittest*.py')

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(suits)

    #生成HTML格式的报告
    #为了能不覆盖，我们给结果文件添加一个时间的字段
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    fp = open('C:/Users/admin/Desktop/JMeter/Selenium/unittest/test_report/'+now_time+'result.html',"wb")
    runner = HTMLTestRunner(stream = fp,title="百度搜索测试报告",description="运行环境：Windows 10，Chrome浏览器")
    runner.run(suit)
    fp.close()

import csv
import codecs
from itertools import islice
data = csv.reader(codecs.open('./data_file/user_info.csv','r','utf_8_sig'))

#存放用户数据
users = []

#循环输出每行信息
for line in islice(data,1,None):
    users.append(line)

print(users)

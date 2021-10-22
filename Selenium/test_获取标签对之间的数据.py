from xml.dom.minidom import parse

#打开xml文件
dom = parse('./data_file/config.xml')

#得到文档元素对象
root = dom.documentElement

#获取一组标签
tag_name = root.getElementsByTagName('os')

print(tag_name[0].firstChild.data)
print(tag_name[1].firstChild.data)
print(tag_name[2].firstChild.data)
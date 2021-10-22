from xml.dom.minidom import parse

dom = parse("./data_file/config.xml")
root = dom.documentElement

#获得login标签
login_info = root.getElementsByTagName('login')

#获得第一个login标签的username属性值
username = login_info[0].getAttribute("username")
print(username)

#获得第一个login标签的password属性值
password = login_info[0].getAttribute("password")
print(password)

#获得第二个login标签的username属性值
username = login_info[1].getAttribute("username")
print(username)

#获得第二个login标签的password属性值
password = login_info[1].getAttribute("password")
print(password)
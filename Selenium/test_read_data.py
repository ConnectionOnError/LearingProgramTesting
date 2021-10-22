with(open("./data_file/user_info.txt","r")) as user_file:
    data = user_file.readlines()
#line[:-1]作用：
#   去除换行符
users = []
for line in data:
    user = line[:-1].split(":")
    users.append(user)

print(users)
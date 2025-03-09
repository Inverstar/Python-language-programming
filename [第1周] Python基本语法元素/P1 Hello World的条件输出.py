# 获取用户输入
user_input = input("请输入一个数字：")
message = "Hello World"

# 判断输入并输出相应结果
try:
    num = int(user_input)
    if num == 0:
        print(message)
    elif num > 0:
        for i, char in enumerate(message):
            print(char, end="")
            if i % 2 != 0:
                print()
    else:
        for char in message:
            print(char)
except ValueError:
    print("请输入一个有效的数字")
#BMI: Body Mass Index
# 计算公式：BMI = 体重(kg) / 身高(m)^2

while True:
    try:
        s = input("请输入身高(米)和体重(公斤)[空格或逗号隔开]: ")
        s = s.replace('，', ',').replace(' ', ',')
        height, weight = eval(s)
        break
    except Exception as e:
        print("输入格式有误，请用空格、英文或中文逗号分隔身高和体重。请重新输入。")
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI 指标为:国际'{0}', 国内'{1}'".format(who, nat))


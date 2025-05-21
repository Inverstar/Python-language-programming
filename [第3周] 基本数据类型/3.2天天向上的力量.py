def DayDayUpQ1():
    """
    问题1：‰1的力量
    """
    dayup=pow(1.001,365)
    daydown=pow(0.999,365)
    print("向上：{:.2f}，向下：{:.2f}".format(dayup,daydown))

DayDayUpQ1()

def DayDayUpQ2(dayfactor):
    """
    问题2：‰5和1%的力量
    """
    dayup=pow(1+dayfactor,365)
    daydown=pow(1-dayfactor,365)
    print("向上：{:.2f}，向下：{:.2f}".format(dayup,daydown))

DayDayUpQ2(dayfactor=0.005)
DayDayUpQ2(dayfactor=0.01)

def DayDayUpQ3():
    """
    问题3：工作日的力量
    """
    dayup = 1.0
    dayfactor = 0.01
    for i in range(365):
        if i % 7 in [0, 1]:  # 周末
            dayup *= (1 - dayfactor)
        else:  # 工作日
            dayup *= (1 + dayfactor)    
    print("工作日的力量：{:.2f}".format(dayup))

DayDayUpQ3()

def DayDayUpQ4(df):
    """
    问题4：工作日的力量
    """
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup *= (1 - 0.01)
        else:
            dayup *= (1 + df)
    return dayup
dayfactor = 0.01
while DayDayUpQ4(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的力量：{:.2f}".format(DayDayUpQ4(dayfactor)))
print("工作日的力量：{:.2f}".format(DayDayUpQ4(dayfactor-0.001)))
print("工作日的努力参数：{:.3f}".format(dayfactor))
# 工作日模式每天要努力到1.9%,才能达到365模式每天1%的效果

# 天天向上的力量
# GRIT:perseveranceandpassionf0rlong-termgoals
# 1．01**365=37．78
# 1．019**365=962．89
# GRIT,坚毅，对长期目标的持续激情及持久耐力
# GR仃是获得成功最重要的因素之一，牢记天天向上的力量
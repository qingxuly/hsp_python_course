# 判断一个年份是否是闰年，闰年的条件是符合下面二者之一：（1）年份能被4整除，但不能被100整除（2）能被400整除
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")

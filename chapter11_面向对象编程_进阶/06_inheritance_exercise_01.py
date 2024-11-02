class GrandPa:
    name = "大头爷爷"
    hobby = "旅游"


class Father(GrandPa):
    name = "大头爸爸"
    age = 39


class Son(Father):
    name = "大头儿子"


son = Son()
print(f"son.name is {son.name} and son.age is {son.age} and son.hobby is {son.hobby}")

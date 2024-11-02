# Account类要求具有属性：姓名（长度为2-4位）、余额（必须>20）、密码（必须是六位），如果不满足，则给出提示
# 通过set_xx 的方法给Account 的属性赋值
# 编写query_info() 接收姓名和密码，如果姓名和密码正确，返回该账号信息

"""
    思路分析：
    类名：Account
    私有属性：姓名（长度为2-4位）、余额（必须>20）、密码（必须是六位）
    构造器：无
    方法：set_xx(self, 属性名) 进行赋值，并且对各个接收到的数据进行校验
    方法：query_info(self, name, pwd) 而且需要验证，才返回响应信息
"""


class Account:
    __name = None
    __balance = None
    __pwd = None

    def set_name(self, name):
        if 2 <= len(name) <= 4:
            self.__name = name
        else:
            print("名字的长度不在2-4位之间")

    def set_balance(self, balance):
        if balance > 20:
            self.__balance = balance
        else:
            print("余额（必须>20）")

    def set_pwd(self, pwd):
        if len(pwd) == 6:
            self.__pwd = pwd
        else:
            print("密码（必须是六位）")

    def query_info(self, name, pwd):
        if name == self.__name and pwd == self.__pwd:
            return f"账户信息：{self.__name} {self.__balance}"
        else:
            return "请输入正确的名字和密码"


# 测试
account = Account()
account.set_name("tim")
account.set_pwd("000000")
account.set_balance(100)
print(account.query_info("tim", "000000"))

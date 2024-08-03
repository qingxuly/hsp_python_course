# 在module1.py中，没有__all__时，会导入所有的功能
# 使用了__all__=['ok'] 在其它文件使用 from module1 import * 只会导入ok()
# 注意：import 模块方式，不受__all__的限制

# 表示如果其它文件使用 from module1 import * 导入，则只能导入ok()函数
__all__ = ["ok"]


def hi():
    print("hsp hi")


def ok():
    print("hsp ok")


# 测试代码，当导入模块文件时，也会执行测试代码
# hi()

print(f"module1: {__name__}")

# 如果我们不希望导入模块时，去执行测试代码hi()，可以使用__name__
if __name__ == "__main__":
    hi()




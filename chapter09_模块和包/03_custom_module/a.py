# 导入module1的所有功能
from module1 import *

# import 模块方式，不受`__all__`的限制
# import module1
# module1.hi()
# module1.ok()


# hi()  # __all__ = ["ok"]，设置了只允许ok()函数被导入
ok()

print(f"a.py: {__name__}")

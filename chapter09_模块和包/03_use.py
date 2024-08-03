# # 导入包下的模块
# import package.module01
# import package.module02
#
# # 使用导入的模块
# package.module01.hi()
# package.module02.ok()
#
# # 这种方式导入，在使用时，`模块.功能`，不用带包名。
# from package import module01
#
# module01.hi()
#
# # 导入包的模块的指定函数、类、变量
# from package.module01 import hi
#
# # 直接使用功能名调用即可
# hi()
#
# # from 包名.模块 import *：表示导入包的模块的所有功能。
# from package.module01 import *
#
# hi()
# hello()
#
# # __init__.py 通过__all__控制允许导入的模块
# from package import *
#
# module02.ok()
#
# # 引入限制了module01模块导入，因此不能使用
# # module01.hi()
from math import fabs

# __all__ = ['module02']不能限制下面的导入方式
# import package.module01
# import package.module02
#
# package.module01.hi()
# package.module02.ok()
#
# # 包可以有多个层级
# # 使用方式1
# import package.package2.module03
#
# package.package2.module03.cal(10, 20)
#
# # 使用方式2
# from package.package2.module03 import cal
#
# cal(10, 20)
#
# # 使用方式3
# from package.package2 import module03
#
# module03.cal(10, 20)


print(fabs(-90.8))

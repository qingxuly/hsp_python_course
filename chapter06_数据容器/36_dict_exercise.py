# 一个公司有多个员工，请使用合适的数据类型保存员工信息（员工号、年龄、姓名、入职时间、薪水）
clerks = {
    "0001": {
        "age": 20,
        "name": "贾宝玉",
        "entry_time": "2011-11-11",
        "salary": 12000
    },
    "0002": {
        "age": 21,
        "name": "薛宝钗",
        "entry_time": "2015-12-12",
        "salary": 10000
    },
    "0010": {
        "age": 18,
        "name": "林黛玉",
        "entry_time": "2018-10-10",
        "salary": 20000
    }
}

print(f"员工号为0010的信息为：姓名-{clerks['0010']['name']} "
      f"年龄-{clerks['0010']['age']} "
      f"入职时间-{clerks['0010']['entry_time']} "
      f"薪水-{clerks['0010']['salary']}")

# 增加
clerks['0020'] = {
    "age": 30,
    "name": "老韩",
    "entry_time": "2020-08-10",
    "salary": 6000
}
print("clerks:", clerks)

# 删除
del clerks['0001']
print("clerks:", clerks)

# 修改
clerks['0020']['name'] = '韩顺平'
clerks['0020']['entry_time'] = '1999-10-10'
clerks['0020']['salary'] += clerks['0020']['salary'] * 0.1
print("clerks:", clerks)

# 遍历
keys = clerks.keys()
for key in keys:
    clerks[key]['salary'] += clerks[key]['salary'] * 0.2
print("clerks:", clerks)

# 格式化输出
for key in keys:
    print(f"员工号为{key}的员工信息如下 年龄:{clerks[key]['age']}"
          f"名字:{clerks[key]['name']}"
          f"入职时间:{clerks[key]['entry_time']}"
          f"薪水:{clerks[key]['salary']}")
print("-" * 60)
for key in keys:
    clerk_info = clerks[key]
    print(f"员工号为{key}的员工信息如下 年龄:{clerks[key]['age']}"
          f"名字:{clerk_info['name']}"
          f"入职时间:{clerk_info['entry_time']}"
          f"薪水:{clerk_info['salary']}")

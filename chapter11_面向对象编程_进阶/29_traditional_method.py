import time


class AA:
    def job(self):
        # 得到开始的时间，秒数
        start = time.time()
        num = 0
        for i in range(1, 800001):
            num += 1
        # 得到结束的时间，秒数
        end = time.time()
        print("计算任务执行时间（秒）", (end - start))


class BB:
    def job(self):
        # 得到开始的时间，秒数
        start = time.time()
        num = 1
        for i in range(1, 90001):
            num -= 1
        # 得到结束的时间，秒数
        end = time.time()
        print("计算任务执行时间（秒）", (end - start))


if __name__ == '__main__':
    aa = AA()
    bb = BB()

    aa.job()
    bb.job()

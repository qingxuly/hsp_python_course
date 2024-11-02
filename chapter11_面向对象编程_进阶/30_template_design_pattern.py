import time
from abc import abstractmethod, ABC


class Template(ABC):
    @abstractmethod
    def job(self):
        pass

    # 统计任务执行时间
    def cal_time(self):
        # 得到开始的时间，秒数
        start = time.time()
        self.job()
        # 得到结束的时间，秒数
        end = time.time()
        print("计算任务执行时间（秒）", (end - start))


class AA(Template):
    def job(self):
        num = 0
        for i in range(1, 800001):
            num += 1


class BB(Template):
    def job(self):
        num = 1
        for i in range(1, 90001):
            num -= 1


if __name__ == '__main__':
    aa = AA()
    bb = BB()

    aa.cal_time()
    bb.cal_time()

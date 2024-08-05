# 定义Music类，里面有音乐名name，音乐时长times属性，并有播放play功能，和返回本身属性信息的方法get_info
"""
    思路分析：
    类名：Music
    属性：name, times
    构造器：__init__(self, name, times)
    方法：play, get_info
"""


class Music:
    def __init__(self, name, times):
        self.name = name
        self.times = times

    def play(self):
        print(f"音乐名 {self.name} 正在播放中... 时长为 {self.times}")

    def get_info(self):
        return f"音乐的信息： name:{self.name} times:{self.times}"


# 测试
music = Music("月光曲", 300)
music.play()
print(music.get_info())

import random


class Tom:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.choices = ['石头', '剪刀', '布']

    def play(self):
        user_choice = int(input("请输入你的选择（0=石头，1=剪刀，2=布）："))
        if user_choice not in [0, 1, 2]:
            print("输入错误，请输入0、1或2。")
            return

        computer_choice = random.randint(0, 2)
        print(f"Tom的选择是：{self.choices[user_choice]}，电脑的选择是：{self.choices[computer_choice]}")

        if user_choice == computer_choice:
            print("平局！")
        elif (user_choice == 0 and computer_choice == 1) or \
                (user_choice == 1 and computer_choice == 2) or \
                (user_choice == 2 and computer_choice == 0):
            print("Tom赢了！")
            self.wins += 1
        else:
            print("Tom输了！")
            self.losses += 1

    def show_scores(self):
        print(f"Tom的赢的次数：{self.wins}，输的次数：{self.losses}")


# 使用示例
tom = Tom()
tom.play()
tom.play()
tom.show_scores()

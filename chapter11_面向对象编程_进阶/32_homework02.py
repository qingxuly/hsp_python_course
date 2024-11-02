class Grand:
    name = 'AA'
    __age = 100

    def g1(self):
        print('Grand-g1()')


class Father(Grand):
    id = '001'
    __score = None

    def f1(self):
        # super() 可以访问哪些成员（属性和方法）
        super().name
        super().g1()

        # self() 可以访问哪些成员
        self.id
        self.__score
        self.name
        self.f1()
        self.g1()

        print('Father-f1()')


class Son(Father):
    name = 'BB'

    def g1(self):
        print('Son-g1()')

    def __show(self):
        # super() 可以访问哪些成员（属性和方法）
        super().id
        super().name
        super().f1()
        super().g1()

        # self() 可以访问哪些成员
        self.name
        self.id

        self.g1()
        self.__show()
        self.f1()

        print('Son-show()')

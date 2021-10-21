class Animal:
    def __init__(self,name,age,gender,weight):
        #非私有属性
        self.name = name
        self.age = age
        self.gender = gender
        #私有属性 不能被继承，也不能在类的外部被调用
        self.__weight = weight
    #私有方法 不能被继承，也不能在类的外部被调用
    def __eat(self,food):
        print("{}不爱吃肉，爱吃{}".format(self.name,food))
    #非私有方法
    def run(self):
        print("{}吃完饭了喜欢跑来跑去".format(self.name))
    def shower(self):
        print("{}喜欢吃饭前去洗澡".format(self.name))
    def introduce(self):
        msg = "{}是一个{}孩子，小可爱今年才{}岁，但是体重居然已经{}斤了。"
        print(msg.format(self.name,self.gender,self.age,self.__weight))
        self.__eat("鬼鬼") #调用私有化方法

#狗类，子类继承父类，获得父类所有非私有的属性和方法
class Dog(Animal):
    def drink(self):
        print("{}喜欢喝牛奶".format(self.name))
    #子类重写了父类的同名方法
    def run(self):
        print("{}吃完饭了就在那躺着，根本就不动".format(self.name))

class Cat(Animal):
    def __init__(self,name,age,gender,weight):
        super(Cat,self).__init__(name,age,gender,weight) #super关键字重写父类构造方法
        self.name = name
        print("我是{}".format(self.name))
    def getName(self):
        return "Cat"+self.name
    def drink(self):
        print("{}喜欢喝酸奶".format(self.name))

a1 = Animal("瑰丝",18,"女",40)
a1.run()
# a1.__eat("鬼鬼")  #私有方法不能在类的外部被调用
# print(a1.__weight) #私有属性不能在类的外部被调用

d1 = Dog("小瑰",3,"男",20)
#子类调用父类非私有方法
d1.introduce()
d1.drink()
#子类调用方法时，如果已经重写了父类同名方法，则调用自己的
d1.run()

c1 = Cat("娃琳可",2,"女",18)
c1.introduce()
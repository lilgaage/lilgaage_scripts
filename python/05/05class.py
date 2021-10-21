#定义鬼类
class Ghost:
    #构造方法，用于实例化对象
    def __init__(self,name,sex,age):  #self指代对象，哪个对象调用哪个方法就用哪个
        self.name = name
        self.sex = sex
        self.age = age
    #私有方法
    def __call(self):
        print("一起打电话吧")
    #非私有方法
    def reminx(self):
        print("鬼会混音",id(self))

    def punk(self):
        print("朋克鬼",id(self))

    def verse(self):
        print("鬼的诗句韵律很好",id(self))

    def explicit(self):
        print("也想听鬼限制级曲",id(self))

    def info(self):
        print("{}今年{}岁，是{}生".format(self.name,self.age,self.sex))

#实例化对象 对象名=类名()
ghost1 = Ghost("娃琳可","男",22)
#对象名.方法名()
ghost1.reminx()
ghost1.punk()
ghost1.info()
#对象名.属性名
print(ghost1.name)
print("ghost1的id值是{}".format(id(ghost1)))

ghost2 = Ghost("瑰丝","女",18)
ghost2.explicit()
ghost2.verse()
ghost2.info()
print(ghost2.name,ghost2.sex)
print("ghost2的id值是{}".format(id(ghost2)))



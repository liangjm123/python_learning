"""
面向对象技术简介
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    局部变量：定义在方法中的变量，只作用于当前实例的类。
    实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    方法：类中定义的函数。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""

# 实例
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000) # 创建 Employee 类的第一个对象
emp2 = Employee("Manni", 5000) # 创建 Employee 类的第二个对象
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

"_init__()"
"__str__()"
# python的__init__几种方法总结
# 这个方法一般用于初始化一个类
# 但是 当实例化一个类的时候, __init__并不是第一个被调用的, 第一个被调用的是__new__

"__new__(cls[,...])"
# __new__方法的第一个参数是这个类，而其余的参数会在调用成功后全部传递给__init__方法初始化
class A:
    pass

class B(A):
    def __new__(cls):
        print("__new__方法被执行")
        return super().__new__(cls)

    def __init__(self):
        print("__init__方法被执行")
b = B()

class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return super().__new__(cls, string)
a = CapStr("I love China!")
print(a)

"__metaclass__"
# 可以在实现一个类的时候为其添加__metaclass__属性,如果你这么做了, python就会用元类来创建类,
# 当在内存中创建类对象时, python会在类的定义中寻找__metaclass__属性, 如果找到了, python就用它来创建,
# 如果没有找到, 就会用内建的type元类来创建这个类.

class UpperAttrMetaClass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls, name, bases, uppercase_attrs)

class Foo(object):
    __metaclass__ = UpperAttrMetaClass
    bar = 'bip'

print (hasattr(Foo, 'bar'))
# 输出false
print (hasattr(Foo, 'BAR'))
# 输出true


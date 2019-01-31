class Singleton:
    __instance = None
    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance

		
x = Singleton()
x.val = 'burger'
print(x,x.val)
y = Singleton()
print(y,y.val)
print(x, x.val)
y.val= 'Chips'
print(y,y.val)
print(x, x.val)
print(x==y)


class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

x = Borg()
x.val = 'burger'
print(x,x.val)
y = Borg()
print(y,y.val)
print(x, x.val)
y.val= 'Chips'
print(y,y.val)
print(x, x.val)
print(x==y)




# Output
# (base) D:\>python dp7_singleton_bourg.py
# <__main__.Singleton object at 0x00000272ABFB1C50> burger
# <__main__.Singleton object at 0x00000272ABFB1C50> None
# <__main__.Singleton object at 0x00000272ABFB1C50> None
# <__main__.Singleton object at 0x00000272ABFB1C50> Chips
# <__main__.Singleton object at 0x00000272ABFB1C50> Chips
# True
# <__main__.Borg object at 0x00000272ABFB1978> burger
# <__main__.Borg object at 0x00000272ABFB1CF8> burger
# <__main__.Borg object at 0x00000272ABFB1978> burger
# <__main__.Borg object at 0x00000272ABFB1CF8> Chips
# <__main__.Borg object at 0x00000272ABFB1978> Chips
# False
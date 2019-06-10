class Singleton(object):
    __instance = None
    def __new__(cls, val):
        if not Singleton.__instance:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance

s = Singleton(15)
#s.value = 15
s2 = Singleton("x")
#s2.value = 'x'
print(s.val)

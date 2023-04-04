class Singleton:

    __instance = None

    @staticmethod
    def getinstance():
        if Singleton.__instance is None:
            Singleton()

        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Singleton object already exist")

        Singleton.__instance = self

s1 = Singleton()
s2 = Singleton.getinstance()
s3 = Singleton.getinstance()

print(s1)
print(s2)
print(s3)

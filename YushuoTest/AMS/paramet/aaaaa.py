class clsTest():
    y = ''

    def __init__(self):
        self.y = '你'


x = clsTest
print(x.y)

x = clsTest()
print(x.y)
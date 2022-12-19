class User:
    username = ""
    password= ""
    def __init__(self,username='admin',password='1234'):
        self.username=username
        self.password=password
    def clear(self):
        self.password=''
        self.username=''
        self.__privatePrint()

    def __privatePrint(self):
        print('test private fuction')

user=User()
user.clear()

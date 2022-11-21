class Parent: # it's parent class
    def __init__(self, login, password, id, name):
        self.__login = login
        self.__password = password
        self.id = id
        self.name = name

    def Show_info(self):
        print(f'{self.__login}\n{self.__password}')



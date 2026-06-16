class Authentication:
    # Private members
    __username = 'scaleracad'
    __password = 'scaler@a'
    def creden(self):
        print(f"Username: {self.__username}")
        print(f"Password:{self.__password}")
p = Authentication()
p.creden()
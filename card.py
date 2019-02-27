class card:

    def __init__(self, name, suit):
        self.__name = name
        self.__suit = suit

    def loval(self):
        if 'Ace' in self.__name:
            return 1
        elif 'Two' in self.__name:
            return 2
        elif 'Three' in self.__name:
            return 3
        elif 'Four' in self.__name:
            return 4
        elif 'Five' in self.__name:
            return 5
        elif 'Six' in self.__name:
            return 6
        elif 'Seven' in self.__name:
            return 7
        elif 'Eight' in self.__name:
            return 8
        elif 'Nine' in self.__name:
            return 9
        else:
            return 10

    def hival(self):
        if 'Ace' in self.__name:
            return 11
        else:
            hival = self.loval()
            return hival

    def getsuit(self):
        return self.__suit

    def getname(self):
        return self.__name

    def __str__(self):
        return self.__name + ' of ' + self.__suit

    def isace(self):
        if 'Ace' in self.__name:
            return True
        return False

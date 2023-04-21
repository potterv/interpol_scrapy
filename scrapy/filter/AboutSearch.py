"""
 Класс AboutSearch описывает структуру информации
 об общем количестве розыскиваемых лиц
 в желтом или красном списке
"""

class AboutSearch:
    __total_number: int
    __serch_result: int
    __number_pages: int
    __DISPLAYS_UP = 160
    def __init__(self,totalNumber,searchResult):
        self.__total_number=totalNumber
        self.__serch_result=searchResult
    @property
    def numberPages(self):
        if self.__serch_result%20 == 0:
            return int(self.__serch_result/20)
        else:
            return int((self.__serch_result // 20)+1)
    @property
    def displaysUp(self):
        return self.__DISPLAYS_UP
    @property
    def totalNumber(self):
        return self.__total_number
    @property
    def searchResult(self):
        return self.__serch_result
    def __str__(self):
        return (f"""total_number: {self.__total_number}, serch_result: {self.__serch_result}, number_pages: {self.numberPages}, DISPLAYS_UP: {self.__DISPLAYS_UP}""")
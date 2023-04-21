

class PhysicalDescription:
    __height:int
    __colourOfHair:str
    __colourOfEyes:str
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        self.__height=height
    @property
    def colourOfHair(self):
        return self.__colourOfHair
    @colourOfHair.setter
    def colourOfHair(self,colourOfHair):
        self.__colourOfHair = colourOfHair
    @property
    def colourOfEyes(self):
        return self.__colourOfEyes
    @colourOfEyes.setter
    def colourOfEyes(self,colourOfEyes):
        self.__colourOfEyes =colourOfEyes

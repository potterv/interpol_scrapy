class Details:
    __fatherFamilyNameAndForename:str
    __motherFamilyNameAndForename:str
    __languageSpoken:str
    @property
    def fatherFamilyNameAndForename(self):
        return self.__fatherFamilyNameAndForename
    @fatherFamilyNameAndForename.setter
    def fatherFamilyNameAndForename(self,fatherFamilyNameAndForename):
        self.__fatherFamilyNameAndForename =fatherFamilyNameAndForename
    @property
    def motherFamilyNameAndForename(self):
        return self.__motherFamilyNameAndForename
    @motherFamilyNameAndForename.setter
    def motherFamilyNameAndForename(self,motherFamilyNameAndForename):
        self.__fatherFamilyNameAndForename= motherFamilyNameAndForename
    @property
    def languageSpoken(self):
        return self.__languageSpoken
    @languageSpoken.setter
    def languageSpoken(self,languageSpoken):
        self.__languageSpoken = languageSpoken

class IdentityParticulars:
  __family_name:str
  __forename:str
  __gender:str
  __age:int
  __date_of_birth: str
  __nationality: str
  __place_of_disappearance:str
  __dateof_disappearance:str
  __distinguishing_marks_and_characteristics:str

  @property
  def family_name(self):
      return self.__family_name
  @family_name.setter
  def family_name(self, family_name):
      self.__family_name = family_name
  @property
  def forename(self):
      return self.__forename

  @forename.setter
  def forename(self, forename):
    self.__forename = forename

  @property
  def gender(self):
      return self.__gender
  @gender.setter
  def gender(self,gender):
      self.__gender = gender
  @property
  def age(self):
    return self.__age
  @age.setter
  def age(self, age):
    self.__age = age
  @property
  def date_of_birth(self):
    return self.__date_of_birth
  @date_of_birth.setter
  def date_of_birth(self, date_of_birth):
    self.__date_of_birth = date_of_birth
  @property
  def nationality(self):
    return self.__nationality
  @nationality.setter
  def nationality(self, nationality):
    self.__nationality = nationality
  @property
  def place_of_disappearance(self):
    return self.__place_of_disappearance
  @place_of_disappearance.setter
  def place_of_disappearance(self, place_of_disappearance):
    self.__place_of_disappearance = place_of_disappearance

  @property
  def dateof_disappearance(self):
    return self.__dateof_disappearance
  @dateof_disappearance.setter
  def dateof_disappearance(self, dateof_disappearance):
    self.__dateof_disappearance = dateof_disappearance

  @property
  def distinguishing_marks_and_characteristics(self):
    return self.__distinguishing_marks_and_characteristics
  @distinguishing_marks_and_characteristics.setter
  def distinguishing_marks_and_characteristics(self, distinguishing_marks_and_characteristics):
    self.__distinguishing_marks_and_characteristics = distinguishing_marks_and_characteristics
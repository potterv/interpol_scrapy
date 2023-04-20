# This is a sample Python script.
from notices.filter import AboutSearch
from notices.FactoryYellowNotices import FactoryYellowNotices
from notices.human import Human


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   host ='10.92.192.51:3128'
   # conf = cp.ConfigProxy(host,host,host)
   # print(conf.proxies)
   # s = Scrapy("https://www.interpol.int/How-we-work/Notices/View-Yellow-Notices",conf)
   # s.read()
   # s.test()
   # a_s=AboutSearch(200,43)
   # print(a_s)


   factory = FactoryYellowNotices()
   ip=factory.create_identity_particulars()
   ip.interface_identity_particulars()


   class MyNumber:
       def __init__(self,i,j):
           self.i=i
           self.j=j

   class MyNumbers:
       def __iter__(self,value):
           self.a = 1
           return self

       def __next__(self):
           x = self.a
           self.a += 1
           return f'{x}   /   {self}'
       def __add__(self, other):
          MyNumbers(other)


   # num = MyNumber(3,4)
   # myclass = MyNumbers(num)
   #
   # myiter = iter(myclass)
   #
   # print(next(myiter))
   # print(next(myiter))
   # print(next(myiter))
   # print(next(myiter))
   # print(next(myiter))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

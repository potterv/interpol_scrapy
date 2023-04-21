# This is a sample Python script.
from notices.FactoryYellowNotices import FactoryYellowNotices


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
   pd = factory.create_physical_description().interface_physical_description()
   pd.height=34
   print(pd.height)
   idp = ip.interfas_IdentityParticularsr()
   idp.gender='hkl'
   print(idp.gender)
   print(type(ip))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

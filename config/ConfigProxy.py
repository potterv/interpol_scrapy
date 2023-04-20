import self as self


class ConfigProxy:
     __http_proxy:str
     __url:str
     def __init__(self,url,http_proxy):
         self.__url
         self.__http_proxy = http_proxy

     @property
     def proxies(self):
         return  {
                   'server': self.__http_proxy
                 }



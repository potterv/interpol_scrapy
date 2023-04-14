import self as self


class ConfigProxy:
     __http_proxy:str
     __https_proxy:str
     __ftp_proxy:str

     def __init__(self,http_proxy,https_proxy,ftp_proxy):
         self.__http_proxy = http_proxy
         self.__https_proxy = https_proxy
         self.__ftp_proxy = ftp_proxy
     @property
     def proxies(self):

         return {
              "http"  : self.__http_proxy,
              "https" : self.__https_proxy,
              "ftp"   : self.__ftp_proxy
               }
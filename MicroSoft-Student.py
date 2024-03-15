import requests
import random
res = requests.post('https://2gfre.kskb.eu.org/getOffice',json={"subscription":"16ddbbfc-09ea-4de2-b1d7-312db6112d70","email":{"username":"whisper"+str(random.randint(1,9999)),"domain":"2gfre.mcsoft.org"},"code":"Teams@Free"}).json()
try:
 email=res['account']['email']
 psw=res['account']['password']
 print(f'''[+] E-mail : {email}
[+] PassWord : {psw}''')
except:
 print(res)
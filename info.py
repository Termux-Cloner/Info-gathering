import requests
import random
import os
import string
import hashlib
import sys
import time
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\033[1;34m' # BIRU +
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
net = requests.get("http://ip-api.com/json/").json()["isp"]
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
def line():
    print('\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\x1b[1;93m')

os.system('clear')
logo = """\033[1;33m               
\033[1;31m██╗   ██╗███████╗██╗  ██╗
\033[1;31m██║   ██║██╔════╝╚██╗██╔╝
\033[1;31m██║   ██║█████╗   ╚███╔╝ 
\033[1;31m╚██╗ ██╔╝██╔══╝   ██╔██╗ 
\033[1;31m╚████╔╝ ███████╗██╔╝ ██╗
 \033[1;38m ╚═══╝  ╚══════╝╚═╝  ╚═╝            
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
\033[1;39m━▷ \033[0;91m𝙊𝙒𝙉𝙀𝙍   \033[1;39m◈＊◈\033[1;33m  𝗟𝗨𝗙𝗙𝗬 (𝗡𝗜𝗞𝗘𝗦𝗛)
\033[1;39m━▷ \033[0;91m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 \033[1;39m◈＊◈ \033[1;33m 𝐒𝐓𝐑𝐀𝐖𝐇𝐀𝐓 𝐋𝐔𝐅𝐅𝐘 × 𝐍𝐈𝐊𝐄𝐒𝐇
\033[1;39m━▷ \033[0;91m𝗧𝗢𝗢𝗟-𝗜𝗡𝗙𝗢  \033[1;39m◈＊◈ \33[0;92m 𝗜𝗡𝗙𝗢 𝗚𝗔𝗧𝗛𝗘𝗥𝗜𝗡𝗚
\033[1;39m━▷ \033[0;91m𝙑𝙀𝙍𝙎𝙄𝙊𝙉  \033[1;39m◈＊◈ \033[1;31m𝟭.𝟬   """ 
line()
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def _call(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

def get_account_details(account_id, password):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    req = {
        'api_key': api_key,
        'attempt_login': True,
        'email': account_id,
        'format': 'json',
        'locale': 'en_US',
        'method': 'auth.login',
        'password': password,
        'return_ssl_resources': True,
        'v': '1.0'
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()  # Using hashlib for MD5
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/auth.login'
    response = _call(api_url, req)

    if 'access_token' in response:
        access_token = response['access_token']
        user_info = get_user_info(access_token)
        creation_date = get_creation_date(access_token)
        line()
        print(f"\x1b[34;24mACCESS TOKEN : {access_token}")
        print(f"\x1b[35;25mCLIENT UID : {user_info.get('id', 'N/A')}")
        print(f"\x1b[36;26mNAME : {user_info.get('first_name', 'N/A')} {user_info.get('last_name', 'N/A')}")
        print(f"\x1b[37;27mBIRTHDAY : {user_info.get('birthday', 'N/A')}")
        print(f"\x1b[38;28mGENDER : {user_info.get('gender', 'N/A')}")
    else:
        print(f'[×] Failed to login: {response.get("error_msg", "Unknown error")}')

def get_user_info(access_token):
    url = f"https://graph.facebook.com/me?fields=id,first_name,last_name,birthday,gender&access_token={access_token}"
    response = requests.get(url)
    return response.json()

def get_creation_date(access_token):
    url = f"https://graph.facebook.com/me?fields=created_time&access_token={access_token}"
    response = requests.get(url)
    data = response.json()
    return data.get('created_time', 'N/A')

if __name__ == "__main__":
    print(logo)

    line()
    account_id = input("\x1b[32;5;22mYOUR EMAIL OR UID : ")
    password = input("\x1b[31;5;23mYOUR PW : ")
    get_account_details(account_id, password)
    line()

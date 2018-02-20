#https://github.com/TCWTEAM
#Made by XO
import requests
from bs4 import BeautifulSoup as bs
import json
from utils import c_logging, n_logging
import string
import names
from time import sleep
from random import *
import os
import sys

os.remove("accounts.txt")
f = open("accounts.txt", "w+")
f.close()

with open('config.json') as file:
    config = json.load(file)
    file.close()

def dot_trick(username):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""
        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@gmail.com")
    return emails

def main(num):
    count = 0
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'www.adidas.com',
        'Origin':'https://www.adidas.com',
        'Referer':'https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    for i in range(int(num)):
        min_char = 9
        max_char = 14
        min_char0 = 8
        max_char0 = 10
        allchar = string.ascii_letters + string.digits
        rprefix = "".join(choice(allchar) for x in range(randint(min_char0, max_char0)))
        passw = config['password']
        s = requests.session()

        a = s.post("https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/", headers=headers)
        soup0 = bs(a.content, "html.parser")
        sk1 = soup0.find('input', {'name':'dwfrm_mipersonalinfo_securekey'})
        sk1 = str(sk1)
        sk1 = sk1.split('value="')[1]
        sk1 = sk1.split('"/>')[0]

        link0 = soup0.find_all('form', {'data-component':'form/Form'})
        link0 = str(link0)
        link0 = link0.split('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/')[1]
        link0 = link0.split('" class="fanyform"')[0]
        link0 = link0.split('"')[0]
        link0 = "https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/{}".format(link0)

        firstname = names.get_first_name(gender='male')
        lastname = names.get_last_name()

        dayofmonth = randint(1, 25)
        month = randint(1, 12)
        year = randint(1990, 1999)

        payload1 = {
            'dwfrm_mipersonalinfo_firstname':firstname,
            'dwfrm_mipersonalinfo_lastname':lastname,
            'dwfrm_mipersonalinfo_customer_birthday_dayofmonth':dayofmonth,
            'dwfrm_mipersonalinfo_customer_birthday_month':month,
            'dwfrm_mipersonalinfo_customer_birthday_year':year,
            'dwfrm_mipersonalinfo_step1':'Next',
            'dwfrm_mipersonalinfo_securekey':sk1,
        }

        req1 = s.post(link0, data=payload1, headers=headers)

        soup1 = bs(req1.content, "html.parser")
        link2 = soup1.find_all('form', {'id':'dwfrm_milogininfo'})
        link2 = str(link2)
        link2 = link2.split('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/')[1]
        link2 = link2.split('" class="fanyform"')[0]
        link2 = link2.split('"')[0]
        link2 = "https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/{}".format(link2)

        sk2 = soup1.find('input', {'name':'dwfrm_milogininfo_securekey'})
        sk2 = str(sk2)
        sk2 = sk2.split('value="')[1]
        sk2 = sk2.split('"/>')[0]

        emailJig = config['emailJig']
        emailJig = emailJig.upper()

        if emailJig == "GMAIL":
            prefix = config['email'].split("@")[0]
            dotarray = dot_trick(prefix)
            dotnum = randint(0, len(dotarray) - 1)
            email = dotarray[dotnum]
        else:
            prefix = config['email'].split("@")[0]
            domain = config['email'].split("@")[1]
            email = "{}{}@{}".format(prefix, rprefix, domain)


        payload2 = {
            'dwfrm_milogininfo_email':email,
            'dwfrm_milogininfo_password':passw,
            'dwfrm_milogininfo_newpasswordconfirm':passw,
            'dwfrm_milogininfo_step2':'Next',
            'dwfrm_milogininfo_securekey':sk2,
        }

        req2 = s.post(link2, data=payload2, headers=headers)

        soupf = bs(req2.content, "html.parser")
        link3 = soupf.find_all('form', {'id':'dwfrm_micommunicinfo'})
        link3 = str(link3)
        link3 = link3.split('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/')[1]
        link3 = link3.split('" class="fanyform"')[0]
        link3 = link3.split('"')[0]
        link3 = "https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/{}".format(link3)

        sk3 = soupf.find('input', {'name':'dwfrm_micommunicinfo_securekey'})
        sk3 = str(sk3)
        sk3 = sk3.split('value="')[1]
        sk3 = sk3.split('"/>')[0]

        payload3 = {
            'dwfrm_micommunicinfo_agreeterms':'true',
            'dwfrm_micommunicinfo_step3':'Register',
            'dwfrm_micommunicinfo_securekey':sk3,
        }

        req3 = s.post(link3, data=payload3, headers=headers)
        if req3.status_code == 200:
            count = count + 1
            f = open("accounts.txt", "a+")
            f.write("{}:{} | {} {}\n".format(email, passw, firstname, lastname))
            c_logging("Created Account {}/{}".format(count, num), "green")
        else:
            c_logging("Error Creating Account", "red")
    c_logging("Created {}/{} Accounts".format(count, num), "magenta")
    c_logging("If you love me paypal.me/ehxoh", "magenta")




if __name__ == '__main__':
    n_logging("===========================")
    c_logging("Adidas Account Creator V2", "cyan")
    c_logging("Made By XO", "cyan")
    c_logging("paypal.me/ehxoh", "cyan")
    n_logging("===========================")
    print("")
    n_logging("----------------------------")
    c_logging("Email Jig: {}".format(config['emailJig']), "magenta")
    c_logging("Email: {}".format(config['email']), "magenta")
    c_logging("Password: {}".format(config['password']), "magenta")
    n_logging("----------------------------")
    print("")
    num = input("# Of Accs To Create: ")
    main(num)

import os
import sys
import time


def start_printings():
    os.system('cls')

    print('downloading libraries.')
    os.system('pip install colorama')
    os.system('cls')
    time.sleep(0.7)

    print(Fore.MAGENTA + 'downloading libraries..')
    os.system('pip install requests')
    os.system('cls')
    time.sleep(0.7)

    print(Fore.MAGENTA + 'downloading libraries...')
    os.system('pip install fade')
    os.system('cls')
    time.sleep(0.7)

    print(Fore.MAGENTA + 'downloading libraries.')
    os.system('pip install python-whois')
    os.system('cls')
    time.sleep(0.7)

    print(Fore.MAGENTA + 'downloading libraries..')
    os.system('pip install pywebcopy')
    os.system('cls')
    time.sleep(0.7)

    print(Fore.MAGENTA + 'downloading libraries...')
    os.system('pip install validators')
    os.system('cls')
    time.sleep(0.7)

    print(Fore.MAGENTA + 'downloading libraries.')
    os.system('pip install shutil')
    os.system('cls')
    time.sleep(0.7)
    
    print(Fore.MAGENTA + 'downloading libraries.')
    os.system('pip install bs4')
    os.system('cls')
    time.sleep(0.7)

    print('Successful!')
    os.system('cls')
    print(Style.RESET_ALL)


start_printings()


import ctypes
import fade
import requests
import whois
from colorama import Fore, Style
from pywebcopy import save_webpage, save_website
import validators
from bs4 import *


os.system('mode con: cols=87 lines=50')


def warning(text):
    print("\033[1m\033[31m{}\033[0m".format(text))



def webpage(url, folder, name):
    save_webpage(
        url=url,
        project_folder=folder,
        project_name=name,
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )


def website(url, folder, name):
    save_website(
        url=url,
        project_folder=folder,
        project_name=name,
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )


def site_downloader():
    print("""Choose:
    1 - save page
    2 - save website""")
    b = False

    while not b:
        try:
            a = int(input())
            if a == 1 or a == 2:
                b = True
            else:
                warning("Here is no anoother functions( ...")
        except:
            warning("Only numbers")

    c = False
    while c == False:
        url = input("Input link: ")
        if validators.url(url):
            c = True
        else:
            warning("Inccorect word!")

    folder = input("Way for saving: ")
    name = input("project name: ")
    if a == 1:
        webpage(url, folder, name)
    else:
        website(url, folder, name)


def set_console_title():
    ctypes.windll.kernel32.SetConsoleTitleW("Celestial /|\ ^._.^ /|\ ")


API = '6C6A0565BD8ACBA3637521531867E4C0'






def nickname_finder(self):
    os.system('cls')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '/' + Fore.MAGENTA + ']' + Fore.BLUE + 'Searching nickname', Fore.MAGENTA + f'{self}' + Fore.BLUE + ' on:')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Archive.org:', Fore.MAGENTA + f'https://archive.org/details/@{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'AskFM:', Fore.MAGENTA + f'https://ask.fm/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Audiojungle:', Fore.MAGENTA + f'https://audiojungle.net/user/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'BitBucket:', Fore.MAGENTA + f'https://bitbucket.org/{self}/')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Blogger:', Fore.MAGENTA + f'https://{self}.blogspot.com')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Codecademy:', Fore.MAGENTA + f'https://www.codecademy.com/profiles/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'DEV Community:', Fore.MAGENTA + f'https://dev.to/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'DeviantART:', Fore.MAGENTA + f'https://{self}.deviantart.com')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Disqus:', Fore.MAGENTA + f'https://disqus.com/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Docker Hub:', Fore.MAGENTA + f'https://hub.docker.com/u/{self}/')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Ello:', Fore.MAGENTA + f'https://ello.co/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Euw:', Fore.MAGENTA + f'https://euw.op.gg/summoner/userName={self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'F3.cool:', Fore.MAGENTA + f'https://f3.cool/{self}/')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Facebook:', Fore.MAGENTA + f'https://www.facebook.com/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Facenama:', Fore.MAGENTA + f'https://facenama.com/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Flipboard:', Fore.MAGENTA + f'https://flipboard.com/@{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'FortniteTracker:', Fore.MAGENTA + f'https://fortnitetracker.com/profile/all/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Freelancer:', Fore.MAGENTA + f'https://ww.freelancer.com/u/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Giphy:', Fore.MAGENTA + f'https://giphy.com/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'GitHub:', Fore.MAGENTA + f'https://www.github.com/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Gitee:', Fore.MAGENTA + f'https://gitee.com/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Youtube:', Fore.MAGENTA + f'https://www.youtube.com/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Vkontakte:', Fore.MAGENTA + f'https://vk.com/{self}')
    print(Fore.MAGENTA + f'['+ Fore.BLUE + '+' + Fore.MAGENTA + ']' + Fore.BLUE + 'Instagram:', Fore.MAGENTA + f'https://www.instagram.com/{self}/')


def get_ip_location():
    ip_address = input('Input ip-adress > ')
    url = f'https://api.ip2location.io/?key={API}&ip={ip_address}'

    try:
        response = requests.get(url)
        data = response.json()
        print()
        return data
        print()
    except requests.exceptions.RequestException as e:
        print(f'Except error: {e}')
        return None


def ping_ip():
    ip_address = input('Input IP-adress : ')
    process = os.system(f'ping {ip_address}')
    print(process)

def main_menu2():
        print(fade.water("""
 ██████╗███████╗██╗     ███████╗       |      [1] get my ip info
██╔════╝██╔════╝██║     ██╔════╝       |      [2] get another ip info
██║     █████╗  ██║     █████╗         |      [3] ping ip
██║     ██╔══╝  ██║     ██╔══╝         |      [4] (bonus) download website / page
╚██████╗███████╗███████╗███████╗       |      [5] whois function
 ╚═════╝╚══════╝╚══════╝╚══════╝       |      [6] nickname byfinder
                                       |      
███████╗████████╗██╗ █████╗ ██╗        |      [9] exit
██╔════╝╚══██╔══╝██║██╔══██╗██║        |      
███████╗   ██║   ██║███████║██║        |      Author: https://github.com/CelestialEcho 
╚════██║   ██║   ██║██╔══██║██║        |
███████║   ██║   ██║██║  ██║███████╗   |      
╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝   |      
"""))



def get_my_ip_info():
    try:
        response = requests.get('https://ipinfo.io')
        ip_information = response.json()

        return ip_information
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None


def main_scene():
    while True:

        print()
        choose_def = input(Fore.CYAN + '[+]Choose function > ')
        if choose_def == '1':
            print()
            os.system('cls')
            ip_info = get_my_ip_info()

            if ip_info:
                for key, value in ip_info.items():
                    if key != 'readme':
                        print(Fore.CYAN + f'{key}: {value}')
            main_menu2()


        elif choose_def == '2':
            print()
            os.system('cls')
            ip_data = get_ip_location()
            if ip_data:
                for key, value in ip_data.items():
                    print(Fore.CYAN + f'{key}: {value}')
            main_menu2()


        elif choose_def == '3':
            print()
            os.system('cls')
            ping_ip()
            print()
            main_menu2()

        elif choose_def == '4':
            print()
            site_downloader()
            os.system('cls')
            print('Succesful!')
            print()
            main_menu2()

        elif choose_def == '5':
            print()
            os.system('cls')
            get_whois_info()
            print()
            main_menu2()

        elif choose_def == '6':
            nickname = input('Input nickname for search: ')
            nickname_finder(nickname)
            main_menu2()


        elif choose_def == '8':
            os.system('cls')
            print(
                '\n I did this programm for 2 days, i think that is quite a lot, \nmodules which i have used: '
                '\nctypes, os, sys\ntime, fade, requests\nwhois, colorama, pywebcopy\n and validators')
            main_menu2()

        elif choose_def == '9':
            os.system('cls')
            print(Style.RESET_ALL)
            sys.exit()


        else:
            os.system('cls')
            print(Fore.CYAN + "here isn't another functions (...")
            print()
            main_menu2()


def get_whois_info():
    user_input = input("[1] Domain / [2] IP-adress: ")

    if user_input == '1':
        domain_name = input("Input domain name: ")
        print()
        whois_info = whois.whois(domain_name)

        interesting_keys = [
            'domain_name', 'domain_id', 'registrar', 'whois_server',
            'referral_url', 'updated_date', 'creation_date',
            'expiration_date', 'registrar_abuse_contact_email',
            'registrar_abuse_contact_phone'
        ]

        selected_info = {key: whois_info.get(key, 'N/A') for key in interesting_keys}
        for key, value in selected_info.items():
            if isinstance(value, list):
                value = ', '.join(map(str, value))
            print(f"{key.capitalize().replace('_', ' ')}: {value}")

    elif user_input == '2':
        ip_address = input("Input IP-adress: ")
        whois_info = whois.whois(ip_address)

        interesting_keys = [
            'inetnum', 'netname', 'descr', 'country', 'admin_c',
            'tech_c', 'status', 'remarks', 'created', 'last_updated'
        ]

        selected_info = {key: whois_info.get(key, 'N/A') for key in interesting_keys}
        for key, value in selected_info.items():
            if isinstance(value, list):
                value = ', '.join(map(str, value))
            print(f"{key.capitalize().replace('_', ' ')}: {value}")

    else:
        print("here is no another features( ...")


set_console_title()
main_menu2()
main_scene()

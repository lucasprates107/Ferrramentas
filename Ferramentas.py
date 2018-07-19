#coding: utf-8
import requests
import time
import os


print('''
#############################################################
##################>>>>CODED: TioDosLuar<<<<################### 
#*****************************>>>>V1..0<<<<**********************************#
#####################<hacking></hacking>#######################
############################################################

 [1] > WHOIS
 [2] > DIG
 [3] > BANNER HTTP
 [4] > ADMIN FINDER
 [5] > NIKTO -h
 [6] > PORT_SCAN_NC
 
''')

escolha = int(input('Digite a opção desejada: '))
if escolha == 1:
    site = input('Digite o site: ')
    os.system('whois '+site)

elif escolha == 2:
    site = input('Digite o site: ')
    os.system('dig -t all '+site)

elif escolha == 3:
    site = input('Digite o site: ')
    os.system('nc -v  '+site+' 80')

elif escolha == 4:
    site = input('Digite o site: ')
    wordlst = open('wordlist.txt', 'r')
    for brute in wordlst:
        brute = brute.strip()
        time.sleep(0.53)
        req = requests.get(site+brute)
        if req.status_code == 200:
            print("Página encontrada: ", site+brute)
            break
        else:
            print("Página não encontrada: ", site+brute)

elif escolha == 5:
    site = input('Digite o site: ')
    os.system('nikto -h '+site)

elif escolha == 6:
    site = input('Digite o site: ')
    porta_min = int(input('Digite o minimo de portas: '))
    porta_max = int(input('Digite o maximo de portas: '))
    os.system('nc -vz '+site+' 1-3400')

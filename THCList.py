#!/usr/bin/env python	      #
# encoding: utf-8             # 
#         THC Word List       #
#      Scripter: Ravok THC    #
# GitHUB: github.com/RavokTHC #
############################### 

import itertools

num_list= '012356789'
char_list='abcdefghijklmnopqrstuvwxyz'
especial_list='!@#$%^&*()-_=+\/'
numchar_list='012356789abcdefghijklmnopqrstuvwxyz'
numcharespec_list='012356789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+\/'

print '''


░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░ 
▒  ████████╗██╗  ██╗ ██████╗    ██╗     ██╗███████╗████████╗  ▒
░  ╚══██╔══╝██║  ██║██╔════╝    ██║     ██║██╔════╝╚══██╔══╝  ░ 
▒     ██║   ███████║██║         ██║     ██║███████╗   ██║     ▒ 
░     ██║   ██╔══██║██║         ██║     ██║╚════██║   ██║     ░
▒     ██║   ██║  ██║╚██████╗    ███████╗██║███████║   ██║     ▒
░     ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚══════╝╚═╝╚══════╝   ╚═╝     ░
▒ __      __   ___    ___   ___    _      ___   ___   _____   ▒
░ \ \    / /  / _ \  | _ \ |   \  | |    |_ _| / __| |_   _|  ░
▒  \ \/\/ /  | (_) | |   / | |) | | |__   | |  \__ \   | |    ▒
░   \_/\_/    \___/  |_|_\ |___/  |____| |___| |___/   |_|    ░
▒                                                             ▒
░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░ 

	  	    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
		    ▒╔╦╗╔═╗╔╗╔╦ ╦ ▒
		    ▒║║║║╣ ║║║║ ║ ▒
		    ▒╩ ╩╚═╝╝╚╝╚═╝ ▒
		    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      ░《1》|Gerar WordList Numerica           |≺0-9≻ ░
      ░《2》|Gerar WordList com Letras         |≺a-z≻ ░
      ░《3》|Gerar Wordlist Especiais          |≺!@#≻ ░
      ░《4》|Gerar Wordlist NUM + LETRAS       |      ░
      ░《5》|Gerar Wordlist NUM + LETRAS + ESPC|      ░
      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      Selecione uma opçao para prosseguir!
'''
choice=input("Escolha um Numero:")
    

def characters(char_list):
    length=input("Digite o Tamanho:")
    wordlist=open("Letras.txt","w")
    for i in itertools.product(char_list,repeat=length):
        op=''.join(i)+ '\n'
        wordlist.writelines(op)
    wordlist.close()
    print "OK!"
        
def numbers(num_list):
    length=input("Digite o Tamanho:")
    wordlist=open("Numeros.txt","w")
    for i in itertools.product(num_list,repeat=length):
        op=''.join(i)+ '\n'
        wordlist.writelines(op)
    wordlist.close()
    print "OK!"

def especial(especial_list):
    length=input("Digite o Tamanho:")
    wordlist=open("Especial.txt","w")
    for i in itertools.product(especial_list,repeat=length):
        op=''.join(i)+ '\n'
        wordlist.writelines(op)
    wordlist.close()
    print "OK!"

def numchar(especial_list):
    length=input("Digite o Tamanho:")
    wordlist=open("NumLetras.txt","w")
    for i in itertools.product(numchar_list,repeat=length):
        op=''.join(i)+ '\n'
        wordlist.writelines(op)
    wordlist.close()
    print "OK!"

def numcharespec(numcharespec_list):
    length=input("Digite o Tamanho:")
    wordlist=open("NumLetrasEspec.txt","w")
    for i in itertools.product(numcharespec_list,repeat=length):
        op=''.join(i)+ '\n'
        wordlist.writelines(op)
    wordlist.close()
    print "OK!"


if choice==1:
    numbers(num_list)
elif choice==2:
    characters(char_list)
elif choice==3:
    especial(especial_list)
elif choice==4:
    numchar(numchar_list)
elif choice==5:
    numcharespec(numcharespec_list)

else:
    print("Opçao Invalida!")

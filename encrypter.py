# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:41:47 2019

@author: DEXER
"""

import key_generator as KN
import key_decrypter as KD
import decrypter as DC
import random


def Is_valid(key):
    flag1 = 0
    flag2 = 0
    for i in range(0,2):
        if(ord(key[i]) >=97 and ord(key[i])<=106 ):
            flag1 = flag1 + 1
    for i in range(2,4):
        if(int(key[i] )>= 0 and int(key[i]) <=9):
            flag2 = flag2 + 1
    if(flag1 == 2 and flag2 == 2):
        return True
    else:
        return False
def Change(mess,key):
    list1 = ['a','b','c','d','e','f','g','h','i','j','k']
    enc = ''
    for i in range(0,len(mess)):
        j = mess[i]
        if(ord(j) >=48 and ord(j) <=57):
            enc = enc + list1[int(j)]
        elif(ord(j)>=65 and ord(j)<=90):
            j = int((ord(j))+key)
            if(j>90):
                j = j - 26
            enc = enc + chr(j)
        else:
            enc = enc + j
    return enc

def White_spaces(message):
    lim = len(message)
    spaces = []
    count = 0
    for i in range(0,lim):
        j = message[i]
        if j == ' ':
            spaces.append(count)
            count = 0
        else:
            count = count + 1
    return spaces

def Main_key(key1,key2):
    main_key = str(key1)
    for i in key2:
        if(i>10):
            ch = chr(random.randint(97,122))
            main_key = main_key + ch + str(i) + ch
        else:
            main_key = main_key + str(i)
    return main_key

        
    

def Operation(message,key):
    lim = len(message)
    mess1 = ''
    mess2 = '' 
    mess3 = ''
    mess4 = ''
    key = int(key)
    key1 = int(key/1000)
    key2 = int((key%1000)/100)
    key3 = int((key%100)/10)
    key4 = int(key%10)
    
    main_mes = ''
    for i in range(0,int(lim/4)):
        mess1 = mess1 + message[i]
    mess1 = Change(mess1,key1) 
    for i in range(int(lim/4),int(lim/2)):
        mess2 = mess2 + message[i]
    mess2 = Change(mess2,key2)
    for i in range(int(lim/2),int((3*lim)/4)):
        mess3 = mess3 + message[i]
    mess3 = Change(mess3,key3)
    for i in range(int((3*lim)/4),lim):
        mess4 = mess4 + message[i]
    mess4 = Change(mess4,key4)
    main_mes = mess4 + mess2 + mess3 + mess1
    return main_mes


def Encrypt(message,key):
    limit = len(message)
    message1 = ''
    list_space = []
    for i in range(limit):
        if(ord(message[i]) == 32):
            list_space.append(i+1)
        else:
            message1 = message1 + message[i]
    message2 = Operation(message1,key)
    return message2
    
    


if __name__ == '__main__':
    public_key = 0
    private_key = 0
    print('Options......')
    print('1 to encrypt and 2 to decrypt')
    option = int(input())
    if(option == 1):
        message = input("Enter the message : ")
        message = message + ' '
        message = message.upper()
        private_key2 = White_spaces(message)
        ans = input('do you have the key? : ')
        if(ans == 'yes' or ans == 'y' or ans == 'Y' or ans == 'YES' or ans == 'Yes'):
            public_key = input('enter the key to encrypt the message : ')
            if(Is_valid(public_key)):
                private_key = KD.Decrypt(public_key)
                encrypt = Encrypt(message,private_key)
                private_key = Main_key(private_key,private_key2)
                print('private key : {}'.format(private_key))
                #print('private key2 : {}'.format(private_key2))
                print('encrypted message : {}'.format(encrypt))
            else:
                print('your provided key is not valid please try with different key')
        else:
            ans = input('do you want to generate the key? : ')
            if(ans == 'y' or ans == 'Y' or ans == 'yes' or ans == 'Yes' or ans == 'Yes'):
                private_key = KN.Private_key()
                public_key  = KN.Public_key(private_key)
                encrypt = Encrypt(message,private_key)
                print('your public key is : {}'.format(public_key))
                private_key = Main_key(private_key,private_key2)
                print('your private key is : {}'.format(private_key))
                #print('private key2 : {}'.format(private_key2))
                print('encrypted message : {}'.format(encrypt))
    elif(option == 2):
        message = input('enter the message to decrypt : ')
        private_key = input('enter the key to decrypt : ')
        if(DC.Is_true(int(private_key[:4]))):
            dec = DC.Decrypt(message,private_key)
            print('decrypted message is : {}'.format(dec))
        else:
            print('invalid key entered')
            

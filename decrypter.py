# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 23:06:34 2019

@author: DEXER
"""

def Is_true(key):
    if(key >= 1111 and key <= 9999):
        return True
    else:
        return False
def Divide(message,flag):
    mess1 = ''
    limit = len(message)
    mess2 = ''
    if flag == 1:
        h1 = int(limit/2 + 1)
    else:
        h1 = int(limit/2)
    mess2 = message[h1:limit]
    mess1 = message[0:h1]
    return mess1,mess2

def Change(mess,key):
    list1 = ['a','b','c','d','e','f','g','h','i','j','k']
    dec = ''
    for i in range(len(mess)):
        j = mess[i]
        if(ord(j) >= 97 and ord(j)<= 107):
            j = list1.index(j)
            j = str(j)
        else:
            j = int(ord(j) - key)
            if(j < 65):
                j = j + 26
            j = chr(j)
        dec = dec + j
    return dec
    

def Decrypt(message,key):
    half_message1 = ''
    half_message2 = ''
    limit = len(message)
    key1 = int(key/1000)
    key2 = int((key%1000)/100)
    key3 = int((key%100)/10)
    key4 = int(key%10)
    if(limit%2 == 0 and (limit/2)%2 == 0):
        half_message1,half_message2 = Divide(message,0)
    else:
        half_message1,half_message2 = Divide(message,1)
    if((len(half_message1))%2 == 0):
        mess1,mess2 = Divide(half_message1,0)
    else:
        mess1,mess2 = Divide(half_message1,1)
    if((len(half_message2))%2 == 0):
        mess3,mess4 = Divide(half_message2,0)
    else:
        mess3,mess4 = Divide(half_message2,1)
    mess1 = Change(mess1,key4)
    mess2 = Change(mess2,key2)
    mess3 = Change(mess3,key3)
    mess4 = Change(mess4,key1)
    return(mess4+mess2+mess3+mess1)
    
    

if __name__ == '__main__':
    message = input('enter the message to decrypt : ')
    key = int(input('enter the key :'))
    if(Is_true(key)):
        decrypted = Decrypt(message,key)
        print('decrypted message is : {}'.format(decrypted))
    else:
        print('invalid key entered')

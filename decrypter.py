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
        elif(ord(j) >= 65 and ord(j) <= 90):
            j = int(ord(j) - key)
            if(j < 65):
                j = j + 26
            j = chr(j)
        else:
            j = j
        dec = dec + j
    return dec

def Divide_key(key):
	list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	per_key = 0 
	for i in range(0,4):
		per_key = per_key * 10 + int(key[i])
	space_key = []
	for i in range(4,len(key)):
		if (ord(key[i]) >= 48 and ord(key[i]) <= 57):
			space_key.append(int(key[i]))
		elif(ord(key[i]) >= 97  and ord(key[i]) <= 122):
			num = 0
			space_key.append(list1.index(key[i]) + 10)
	return per_key,space_key

    

def Decrypt(message,key1):
    half_message1 = ''
    half_message2 = ''
    key,skey = Divide_key(key1)
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
    sum_mess = mess4 + mess2 + mess3 + mess1
    dmess = ''
    j  = 0
    k = 0
    for i in sum_mess:
        if j == skey[k]:
            k = k + 1
            dmess = dmess + ' '
            dmess = dmess + i
            j = 1
        else :
            dmess += i
            j = j + 1
    return dmess
        
    
    

if __name__ == '__main__':
    message = input('enter the message to decrypt : ')
    key1 = input('enter the key :')
    key = 0
    for i in range(0,4):
        key = key * 10 + int(key1[i])
    if(Is_true(key)):
        decrypted = Decrypt(message,key1)
        print('decrypted message is : {}'.format(decrypted))
    else:
        print('invalid key entered')

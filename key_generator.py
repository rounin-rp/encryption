
"""
Created on Fri Feb 22 21:14:25 2019

@author: DEXER

"""
import random

list1 = ['a','b','c','d','e','f','g','h','i','j']

def Private_key():
    key = random.randint(1111,9999)
    key = str(key)
    return key

def Public_key(key):
    temp = int(key) + 9999
    temp = temp - 10000
    temp = str(temp)
    public_key = ''
    for i in range(0,2):
        public_key = public_key + list1[int(temp[i])]
    for i in range(2,4):
        public_key = public_key + temp[i]
    return public_key

if __name__ == '__main__':
    print('options....')
    print('1 to generate keys')
    print('2 to encrypt key')
    option = int(input())
    if(option == 1):
        private_key = Private_key()
        public_key = Public_key(private_key)
        print('public key : {}'.format(public_key))
        print('private key : {}'.format(private_key))
    elif(option == 2):
        private_key = int(input('enter private key : '))
        if(private_key >= 1111 and private_key <=9999):
            public_key = Public_key(private_key)
            print('public key : {}'.format(public_key))
           # print('private key : {}'.format(private_key))
        else:
            print('error! invalid key entered')
    else:
        print('error! invalid option selection')
    if(input()):
        exit()
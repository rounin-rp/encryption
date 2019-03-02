# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:26:11 2019

@author: DEXER
"""
list1 = ['a','b','c','d','e','f','g','h','i','j']

def Decrypt(key):
    private = ''
    private = private + str(list1.index(key[0]))
    private = private + str(list1.index(key[1])) 
    private = private + key[2]
    private = private + key[3]
    private = int(private)
    private = 10000 + private
    private = private - 9999
    return private

    
    
    
    
if __name__ == '__main__' :
    key = input('enter the public key : ')
    private_key = Decrypt(key)
    print('private key : {}'.format(private_key))
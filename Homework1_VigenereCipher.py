#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:08:54 2021

@author: victoriaz
"""
import math

message = input("Please enter your message: ").lower()
key = input('Please enter your key: (ONLY LETTERS) ').lower()

#check only-letter key
while key.isalpha() == False:
    print('WARNING! PLEASE ONLY enter LETTERS as key!!!')
    key = input('Please enter another key: ').lower()

#create the dictronary
letters = 'abcdefghijklmnopqrstuvwxyz'

#expend the length of the key same ot more than the length of messsage
n_repeated = math.ceil(len(message)//len(key))+1
key_repeated = key*n_repeated

message_new = ''
index_m = 0    #the indet of the character in the message
index_k = 0    #the index of the character in the key
index_new = 0  #the index of the encrypted character

#Encrypte Procss
for i in range(len(message)):
    m = message[i]
    index_m = letters.find(m) 
    if index_m > -1:                 #in case of letters in message 
        index_k = letters.find(key_repeated[i])
        index_new = (index_m + index_k) % len(letters)
        message_new += letters[index_new]
    elif index_m == -1 and m == ' ':          #in case of empty space in the message
        message_new = message_new + ' '
    else:                                     #in case of numbers in message 
        message_new += m                    
print(f'Encrypted Massage: {message_new}')



#Decrypt Back
message_back = ''
index_m_encry = 0
index_k_encry = 0
index_back = 0


for j in range(len(message_new)):
    cha = message_new[j]
    index_m_encry = letters.find(cha)
    if index_m_encry > -1:
        index_k_encry = letters.find(key_repeated[j])
        index_back    = index_m_encry - (index_k_encry % len(letters))
        message_back += letters[index_back]
    elif index_m_encry == -1 and cha == ' ':
        message_back = message_back + ' '
    else: 
        message_back += cha
    
print(f'Decrypted Message: {message_back}')


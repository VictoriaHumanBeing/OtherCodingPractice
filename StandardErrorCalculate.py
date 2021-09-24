#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:24:50 2021

@author: victoriaz
"""
##################HW 1###################
import math
import random
# Exercise 1

pop = list(range(0,10001))
size = [10, 20, 50, 100, 200, 500, 1000, 5000]

print("#Samples\t\t Mean\t\t Std Error\t\t 95%CI(L)\t\t 95%CI(U)")
for i in size:
    sample = random.sample(population=pop,k = i)
    s_mean = sum(sample)/i
    
    s_di = []
    for x in sample: 
        s_di.append((x-s_mean)**2)
    s_std = math.sqrt(sum(s_di)/(i-1))
    se = s_std/math.sqrt(i)
    print(f'{i}\t\t {s_mean:2f}\t\t {se:6f}\t\t {s_mean-1.96*se}\t\t {s_mean+1.96*se}')
    
   
    

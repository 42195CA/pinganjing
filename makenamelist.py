#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:15:03 2020

@author: liuxia
"""
from pypinyin import pinyin, lazy_pinyin, Style
#count=1
#Nc=5
file1 = open('chinesename.txt', 'r') 
#file1 = open('test.txt', 'r') 
file2 = open('name_pingan.tex','w+')
abc_old='' 
Lines = file1.readlines() 
for line in Lines:
    line=line.strip()
    abc=pinyin(line, style=Style.FIRST_LETTER)
    abc=abc[0][0]
    if abc!=abc_old:
#        count=1
#       start a new file, create a new file
        if abc_old != '':
#            file2 = open('name_'+abc+'.tex','w+')            
#        else:
            t='\\end{itemize}\n'
            file2.writelines(t)

            t='\\end{multicols}\n'
            file2.writelines(t)
#            file2.close() 
#            file2 = open('name_'+abc+'.tex','w+') 
        t='\\chapter{人人平安:'+line[0]+'}\n'
        file2.writelines(t)
        t='\\begin{multicols}{4}'+'\n'
        file2.writelines(t)
        t='\\begin{itemize}'+'\n'
        file2.writelines(t)
    abc_old=abc
    g='\\item '+line.strip()+'平安'+'\n'
    file2.writelines(g)
#    count=count+1
t='\\end{itemize}\n'
file2.writelines(t)
t='\\end{multicols}\n'
file2.writelines(t)
file2.close()     


#file2 = open('name_.txt', 'w') 
#    count=count+1
#    print(g)

#    print("Line{}: {}".format(count, line.strip())) 
#count = 0
# Strips the newline character
#    
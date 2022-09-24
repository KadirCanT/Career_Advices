# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# jobs
# Artificial Intelligence Software                      0

# mathematician                                         1

# Embedded Software j-m-s                               2-3-4

# Networking and Web Applications Software j-m-s        5-6-7


# reklamcılık                                           8

# Artist                                                9

# trader                                                10

# inşaat müh                                            11

# takım yöneticisi                                      12



## sorular
# YL(1) or L(0)     0
# yaratıcılık       1
# analiz yapma      2
# soru geliştirme   3
# hesap denetimi    4
# leading           5
# ikna etme         6
# bilimsel çalışma yapma 7
# yazılım bilmek    8
# cinsiyet          9
# 10 yıldan fazla iş tecrübesi 10
# ofis(1)-saha(0)         11

from random import randint
def randomBinary():
    return randint(0,1)

def ai_or_software():
    data = [randomBinary(),
            randomBinary(),
            1,
            1,
            randomBinary(),
            0,
            randomBinary(),
            1,
            randomBinary(),
            randomBinary(),
            randomBinary(),
            randomBinary(),
            randomBinary()]
    
    return data

def embedded_software():
    deger = randint(0,10)
    if deger > 7: ## senior
        data = [1,
                0,
                1,
                1,
                0,
                randomBinary(),
                randomBinary(),
                randomBinary(),
                1,
                randomBinary(),
                1,
                1,
                4
                ]
    elif 4 < deger <= 7: ## med
        data = [1,
                0,
                1,
                1,
                0,
                randomBinary(),
                randomBinary(),
                randomBinary(),
                1,
                randomBinary(),
                randomBinary(),
                1,
                3
                ]
    else: # junior    
        data = [randomBinary(),
                0,
                1,
                1,
                0,
                randomBinary(),
                randomBinary(),
                randomBinary(),
                1,
                randomBinary(),
                0,
                1,
                2
                ]
    return data

def WebDeveloper():
    deger = randint(0, 2)
    if deger == 0: # j
        data = [randomBinary(),
                1,
                1,
                1,
                0,
                randomBinary(),
                randomBinary(),
                0,
                1,
                randomBinary(),
                0,
                1,
                5
                ]       
    elif deger == 1:
        data = [1,
                1,
                1,
                1,
                0,
                randomBinary(),
                randomBinary(),
                0,
                1,
                randomBinary(),
                0,
                1,
                6
                ]     
    else:
        data = [randomBinary(),
                1,
                1,
                1,
                0,
                randomBinary(),
                randomBinary(),
                0,
                1,
                randomBinary(),
                1,
                1,
                6
                ]
    return data
        
def advertising():
    data = [randomBinary(),
            1,
            1,
            randomBinary(),
            randomBinary(),
            randomBinary(),
            1,
            0,
            0,
            randomBinary(),
            randomBinary() ,
            1,
            8
            ]
    return data

def artist():
    data = [randomBinary(),
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            randomBinary(),
            randomBinary(),
            1,
            9]
    return data
    
def trader():
    data = [randomBinary(),
            0,
            1,
            1,
            1,
            randomBinary(),
            1,
            0,
            0,
            randomBinary(),
            randomBinary(),
            2,
            10
            ]
    return data
def insaat():
    data = [
            randomBinary(),
            randomBinary(),
            1,
            1,
            0,
            1,
            1,
            randomBinary(),
            0,
            randomBinary(),
            randomBinary(),
            0,
            11
            ]    
    return data
def leader():
    data = [1,
            0,
            1,
            1,
            1,
            1,
            1,
            randomBinary(),
            randomBinary(),
            randomBinary(),
            1,
            1,
            12
            ]
    return data

def main():
    dataset= [ ]
    func_list = [ai_or_software(),leader(),insaat(),trader(),artist(),advertising(),embedded_software(),WebDeveloper()]
    for _ in range(5000):
        deger = randint(0, len(func_list)-1)
        dataset.append(func_list[deger])
    return dataset
a = main()
import numpy as np
b = np.array(a)
np.save("datasetim",b)
## sorular
# YL(1) or L(0)     0
# yaratıcılık       1
# analiz yapma      2
# soru geliştirme   3
# hesap denetimi    4
# leading           5
# ikna etme         6
# bilimsel çalışma yapma 7
# yazılım bilmek    8
# cinsiyet          9
# 10 yıldan fazla iş tecrübesi 10
# ofis(1)-saha(0)         11





















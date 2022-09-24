#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 01:41:28 2021

@author: fxdemir
"""

from openpyxl import Workbook,load_workbook
import numpy as np


# Artificial Intelligence Software                      0
# mathematician                                         1
# Embedded Software j-m-s                               2-3-4
# Networking and Web Applications Software j-m-s        5-6-7
# reklamcılık                                           8
# Artist                                                9
# trader                                                10
# inşaat müh                                            11
# takım yöneticisi                                      12



def excel():
    jobs = ["AI Software Engineer",
            "Mathematician",
            "Embedded Software Junior Engineer",
            "Embedded Software Med Level Engineer",
            "Embedded Software Senior Engineer",
            "Web Developer Junior",
            "Web Developer Med Level",
            "Web Developer Senior",
            "Display artist",
            "Artist",
            "Trader",
            "Civil Engineer",
            "Team Leader"          
            ]
    
    a = np.load("./datasetim.npy")
    a = a.tolist()
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"
    
    for row in a:
        indis = row[-1]
        row[-1] = jobs[indis]
    
    for row in a:
        ws.append(row)


    wb.save("dataset.xlsx")
    
excel()
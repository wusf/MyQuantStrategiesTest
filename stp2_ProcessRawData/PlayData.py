#!/usr/bin/env python
#coding:utf-8
"""
  Author:  wusf --<>
  Purpose: 
  Created: 2015/11/26
"""

import os,sys
MyQtLibPath = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(MyQtLibPath)
import sqlite3 as lite
import time,datetime
from datetime import datetime,timedelta
import ProcessRawData.Fundamental.GetFdmtDerivData as FdmtData

dbPath1 = "D:\\QData\\RawData\\FinRptData\\FinRptData_Wind_CICC.db"
dbPath2 = "D:\\QData\\RawData\\MktData\\MktData_Wind_CICC.db"



fdmtData = FdmtData.GetFdmtDerivData(dbPath1,dbPath2)
start = '20100101'
_start = datetime.strptime(start,"%Y%m%d")

import Tools.GetModuleNames as ModuleNames
algoNames = ModuleNames.GetModuleNames(MyQtLibPath+"\\ProcessRawData\\Fundamental\\AnalystDataAlgos")
algos = []
for algoName in algoNames:
    print algoName
    exec("import ProcessRawData.Fundamental.AnalystDataAlgos.{} as algo".format(algoName))
    algos.append(algo)
for i in xrange(1500):
    _start = _start+timedelta(days=5)
    dt = _start.strftime("%Y%m%d")
    ind = fdmtData.CalcAnalystDerivData(dt,300,"600837",algos)
    print dt,ind    
    if dt >= "20151204":
        break






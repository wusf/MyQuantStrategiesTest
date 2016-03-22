#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/1/18
"""

import os,sys,sqlite3
MyQtLibPath = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(MyQtLibPath)

import FactorAlgos.GenPortByRawSingleFactor as GenPort



dbPath1 = "Factor_399906_20D.db"
dbPath2 = "MktData\\MktData_Wind_CICC.db"   
portReturns = GenPort.GetFactorPortReturns(dbPath1,dbPath2,"20160126")

addr = "D:\\QData\\ProcessedData\\"+dbPath1
conn = sqlite3.connect(addr)
conn.text_factory = str
cur = conn.cursor()
cur.execute("PRAGMA table_info(FactorVals)")
cols = cur.fetchall()
factors = []
for col in cols[8:]:
    factors.append(col[1])

for factor in factors:
    portReturns.CalcLongMinusBenchMarkReturns(factor,"FactorVals","0","2",0.2,"DESC","ByFactorVar\\Plot_ZZ500")
    portReturns.CalcLongMinusBenchMarkReturns(factor,"FactorVals","1","2",0.2,"DESC","ByFactorVar\\Plot_HS300")
    portReturns.CalcLongMinusBenchMarkReturns(factor,"FactorVals","0,1","2",0.2,"DESC","ByFactorVar\\Plot_ZZ800")
    
    portReturns.CalcLongMinusBenchMarkReturns(factor,"ZScores","0","2",0.2,"DESC","ByZScore\\Plot_ZZ500")
    portReturns.CalcLongMinusBenchMarkReturns(factor,"ZScores","1","2",0.2,"DESC","ByZScore\\Plot_HS300")
    portReturns.CalcLongMinusBenchMarkReturns(factor,"ZScores","0,1","2",0.2,"DESC","ByZScore\\Plot_ZZ800")    
#portReturns.CalcLongMinusBenchMarkReturns("InterestCoverage_TTM","FactorVals","0","2",0.2,"DESC","Plot_ZZ500")
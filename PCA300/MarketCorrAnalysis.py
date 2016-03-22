#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/2/26
"""

import os,sys,sqlite3
MyQtLibPath = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(MyQtLibPath)

import PCA.PCA_For_Stat_Arb as pca

stkRetPCA = pca.PCA_For_Stat_Arb("MktData\\MktData_Wind_CICC.db", 1,"20050101")
stkRetPCA.LoadDataIntoTimeSeries("000300",1)

numCalc = int(len(stkRetPCA.trdDay)/10)
#c = stkRetPCA.GenEigenPort("20160202",0.7,60,0.1)
for i in range(252,len(stkRetPCA.trdDay),10):
    date = stkRetPCA.trdDay[i]
    a = stkRetPCA.GenEigenPort(date,0.60,250,0.05)
    b = stkRetPCA.GenEigenPort(date,0.60,250,0.1)
    print a[0],a[1],b[1],a[-2],b[-2],a[-1],b[-1]


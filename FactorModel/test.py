#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/5/24
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3
from datetime import datetime,timedelta

root = os.path.abspath("D:\\PyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import FactorModel.GetFactorValues as modGetFactorValues

#----------------------------------------------------------------------
def MainFunc():
    """"""
    #Set up a file log
    myLog = logging.Logger("BuildPITFundamentalDatabase", level="DEBUG")
    myLogHandler = LogHandler.LogOutputHandler("BuildPITFundamentalDatabase.log")
    fh=myLogHandler[0]
    ch=myLogHandler[1]
    myLog.addHandler(fh)
    myLog.addHandler(ch)
    
    objGetFactorValues = modGetFactorValues.GetFactorValues(myLog)
    
    dbNameFactor = "TestFctorDatabase.db"
    factorTypes = ["Fundamental"]
    
    objGetFactorValues.LoadFactorValueTablesIntoMemory(dbNameFactor,factorTypes)
    
    objGetFactorValues.ChooseFactors(["Date","ROOA"],[],[])
    
    v = objGetFactorValues.GetFactorValues("600837","20151205",90)
    print v
    
if __name__ == "__main__":
    MainFunc()
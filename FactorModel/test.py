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
    
    dbNameFactor = "TestFactorDatabase.db"
    factorTypes = ["Fundamental"]
    
    objGetFactorValues.LoadFactorTablesIntoMemory(dbNameFactor,factorTypes)
    
    objGetFactorValues.ChooseFactors(["EBIT2EV_TTM"],["FRet60d"],[])
    
    v = objGetFactorValues.GetFactorValues("600723","20140826",90)
    print type(v["RptType"])
    
if __name__ == "__main__":
    MainFunc()
    
    
#import Tools.GetTradeDays as TradeDays


#td = TradeDays.TradeDays()
#td.GetTradeDays()
#rbd = td.GetRebalanceDays("20100101","20151231","weekly",1)
#for d in rbd:
    #print d
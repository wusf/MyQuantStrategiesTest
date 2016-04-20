#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/4/19
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3
from datetime import datetime,timedelta

root = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import FactorModel.EvaluateFactorByInformationCoefficient.ComputeFactorICs as modComputeFactorICs


#----------------------------------------------------------------------
def MainFunc():
    """
    计算因子IC
    """
    #Set up a file log
    myLog = logging.Logger("ComputeFactorICs", level="DEBUG")
    myLogHandler = LogHandler.LogOutputHandler("ComputeFactorICs.log")
    fh=myLogHandler[0]
    ch=myLogHandler[1]
    myLog.addHandler(fh)
    myLog.addHandler(ch)    
    
    #Database address
    dbPathZScores = "Index_000300_10Day_Rebalance.db"
    dbPathMarketData = "MktData\\MktData_Wind_CICC.db"
    
    begDate = "20100101"
    endDate = "20160101"
    
    #Initiate a GetHedgedPortfolioBySingleFactor object
    objComputeICs = modComputeFactorICs.ComputeICs(dbPathZScores,dbPathMarketData,begDate,endDate,conn=None,logger=myLog) 
    

    #Calculate hedged portfolio return
    factors = objComputeICs.GetFactorNames()
    #print factors[0]
    tm1 = time.time()

    objComputeICs.GetZScores("ZScores","1,2","20120723",'2')
    #print objComputeICs.zscores
    #print objComputeICs.zscoresDay
    
    objComputeICs.GetStockReturn(1,20)
    
    print factors
    for fct in factors:
        objComputeICs.ComputeIC(fct)
    tm2 = time.time()
    print tm2-tm1
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    MainFunc()
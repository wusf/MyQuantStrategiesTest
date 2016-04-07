#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 计算对冲组合收益,判断因子的作用
  Created: 2016/4/7
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3
from datetime import datetime,timedelta

root = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import FactorModel.GetHedgedPortfolioAndCalculateReturn.GetHedgedPortfolioBySingleFactor as modGetHedgedPort


#----------------------------------------------------------------------
def MainFunc():
    """
    计算对冲组合收益,判断因子的作用
    """
    #Set up a file log
    myLog = logging.Logger("GetHedgedPortfolioAndCalculateReturn", level="DEBUG")
    myLogHandler = LogHandler.LogOutputHandler("GetHedgedPortfolioAndCalculateReturn.log")
    fh=myLogHandler[0]
    ch=myLogHandler[1]
    myLog.addHandler(fh)
    myLog.addHandler(ch)    
    
    #Database address
    dbPathFactorValues = "Index_000300_10Day_Rebalance.db"
    dbPathMarketData = "MktData\\MktData_Wind_CICC.db"
    begDate = "20100101"
    endDate = "20120101"
    
    #Initiate a GetHedgedPortfolioBySingleFactor object
    objGetHedgedPort = modGetHedgedPort.GetHedgedPortfolioBySingleFactor(dbPathFactorValues,
                                                                         dbPathMarketData,
                                                                         begDate,endDate,myLog)

    #Calculate hedged portfolio return
    factors = objGetHedgedPort.GetFactorNames()
    print factors
    
    
    
    
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    MainFunc()
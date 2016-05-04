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
import FactorModel.EvaluateFactorByHedgedPortfolioReturn.GetHedgedPortfolioBySingleFactor as modGetHedgedPort


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
    dbPathFactorValues = "Index_399906_21Day_Rebalance.db"
    dbPathMarketData = "MktData\\MktData_Wind_CICC.db"
    
    begDate = "20070101"
    endDate = "20160101"
    
    #Initiate a GetHedgedPortfolioBySingleFactor object
    objGetHedgedPort = modGetHedgedPort.GetHedgedPortfolioBySingleFactor(dbPathFactorValues,
                                                                         dbPathMarketData,
                                                                         begDate,endDate,myLog)

    #Calculate hedged portfolio return
    factors = objGetHedgedPort.GetFactorNames()
    #for factor in factors:
    #    objGetHedgedPort.CalculateHedgedPortfolioReturn(factor,"FactorValues","0","2",0.2,"DESC","Plot_ZScores")
    factor = "Size"
    objGetHedgedPort.CalculateHedgedPortfolioReturn(factor,"FactorValues","0","2",0.2,"DESC","Plot_ZScores")
    
    
    
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    MainFunc()
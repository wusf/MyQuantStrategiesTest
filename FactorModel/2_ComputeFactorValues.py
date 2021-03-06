#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/4/6
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3
from datetime import datetime,timedelta

root = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import FactorModel.ComputeFundamentalFactors.ComputeFactorValues as modComputeFactor

#----------------------------------------------------------------------
def MainFunc():
    """
    使用已经处理过的财报数据和预测数据计算因子值并按行业对该值进行标准化
    """
    #Set up a file log
    myLog = logging.Logger("ComputeFactorValuesAndZScores", level="DEBUG")
    myLogHandler = LogHandler.LogOutputHandler("ComputeFactorValuesAndZScores.log")
    fh=myLogHandler[0]
    ch=myLogHandler[1]
    myLog.addHandler(fh)
    myLog.addHandler(ch)

    #Initiate a ComputeFactor object
    objComputeFactor = modComputeFactor.ComputeFactorValues(myLog)

    #Load source database
    dbPathFdmtData = "PITFundamentalData.db"
    dbPathMktData = "MktData\\MktData_Wind_CICC.db"
    dbPathConstituentStocks = "MktGenInfo\\IndexConstituent_WIND.db"
    objComputeFactor.LoadSourceData(dbPathFdmtData,dbPathMktData,dbPathConstituentStocks)
    
    #Set stock universe and rebalance date
    stockUnviverIndex = "399906"
    begDate = "20070101"
    endDate = "20160101"
    holdingPeriod = 21
    objComputeFactor.SetStockUniverseAndFactorReCalcDate(stockUnviverIndex,begDate,endDate,holdingPeriod)
    
    #Load factor algorithem
    factorStyle = ["Technical"] #["Growth","Momentum","Profitability","Quality","Risk","Value"]
    objComputeFactor.LoadFactorAlgos(factorStyle)
    
    #Start to run factor computation
    objComputeFactor.ComputeAndSaveFactorValues()
    
    #objComputeFactor.ComputeAndSaveZScores("Industry.cfg","SW1_ZZ500")
    
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    MainFunc()
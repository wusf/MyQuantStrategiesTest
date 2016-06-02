#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/5/9
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3


root = os.path.abspath("D:\\PyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import UpdateFactorDatabase.TechnicalFactors.ComputeFactorValues as modComputeFactor


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
    dbPathMktData = "MktData\\MktData_Wind_CICC.db"
    dbPathConstituentStocks = "MktGenInfo\\IndexConstituent_WIND_CICC.db"
    objComputeFactor.LoadSourceData(dbPathMktData,dbPathConstituentStocks)
    
    #Set stock universe and rebalance date
    begDate = "20070101"
    
    objComputeFactor.LoadFactorAlgos()
    
    
    objComputeFactor.ComputeAndSaveFactorValues("TestFactorDatabase",begDate)
    

    
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    MainFunc()
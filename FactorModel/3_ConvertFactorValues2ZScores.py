#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/4/12
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3
from datetime import datetime,timedelta

root = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import FactorModel.ComputeFundamentalFactors.ConvertFactorValuesToZScores as modConvertToZScores


#----------------------------------------------------------------------
def MainFunc():
    """
    把基本面因子原始值转换成ZScores
    """
    #Set up a file log
    myLog = logging.Logger("ConvertFactorValuesToZScores", level="DEBUG")
    myLogHandler = LogHandler.LogOutputHandler("ConvertFactorValuesToZScores.log")
    fh=myLogHandler[0]
    ch=myLogHandler[1]
    myLog.addHandler(fh)
    myLog.addHandler(ch)
    
    #Initiate a ComputeFactor object
    objConvertToZScores = modConvertToZScores.ConvertFactorValuesToZScores(myLog)
    
    #Connect to local fundamental factor database
    dbNameFactorValues = "Index_000300_10Day_Rebalance.db"
    objConvertToZScores.ConnectToFactorDatabase(dbNameFactorValues)
    
    #Get factor names and save them
    #objConvertToZScores.GetFactorNames("OutlierRule.cfg")
    
    #Load outlier rule config
    objConvertToZScores.LoadOutlierRuleConfig("OutlierRule.cfg")
    #print objConvertToZScores.outlierRule

    #Load factor values into in-memory database
    objConvertToZScores.LoadFactorValues()
    
    #Calculate ZScores
    objConvertToZScores.ToZScores(90,3)
    #print objConvertToZScores.factorTrim



    
#----------------------------------------------------------------------
if __name__ == "__main__":
    MainFunc()
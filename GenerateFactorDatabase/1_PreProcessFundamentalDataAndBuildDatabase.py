#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/3/31
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3
from datetime import datetime,timedelta

root = os.path.abspath("D:\\PyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import UpdateFactorDatabase.PreProcessFundamentalData.BuildPointInTimeFundamentalDatabase as modBuildPITDB


#----------------------------------------------------------------------
def MainFunc():
    """
    处理原始财报数据和预测数据，将数据按时间点整理
    """
    #Set up a file log
    myLog = logging.Logger("BuildPITFundamentalDatabase", level="DEBUG")
    myLogHandler = LogHandler.LogOutputHandler("BuildPITFundamentalDatabase.log")
    fh=myLogHandler[0]
    ch=myLogHandler[1]
    myLog.addHandler(fh)
    myLog.addHandler(ch)
    
    #Initiate a BuildPITDB object
    objBuildPITDB = modBuildPITDB.BuildPITFundamentalDatabase(myLog)
    
    #Database address and load raw data
    addrssDBIndexConstituent = "\\MktGenInfo\\IndexConstituent_Wind_CICC.db"
    constituentIndex = ["399106","000001"]
    objBuildPITDB.SetStockUniverse(addrssDBIndexConstituent,constituentIndex)
    objBuildPITDB.LoadFundamentalDataItemsToBeProcessed()
    
    #Name PITDatabase and create it
    namePITDatabase = "PITFundamentalData.db"
    objBuildPITDB.CreateDatabase(namePITDatabase)
    
    #Start to process data
    startDate="20050101"
    objBuildPITDB.CalculateAndSaveData(startDate)
    

#----------------------------------------------------------------------    
if __name__ == "__main__":
    MainFunc()
    

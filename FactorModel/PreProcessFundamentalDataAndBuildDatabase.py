#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/3/31
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3
from datetime import datetime,timedelta

root = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import FactorModel.PreProcessFundamentalData.BuildPointInTimeFundamentalDatabase as modBuildPITDB

myLog = logging.Logger("BuildPITFundamentalDatabase", level="DEBUG")
myLogHandler = LogHandler.LogOutputHandler("BuildPITFundamentalDatabase.log")
fh=myLogHandler[0]
ch=myLogHandler[1]
myLog.addHandler(fh)
myLog.addHandler(ch)

objBuildPITDB = modBuildPITDB.BuildPITFundamentalDatabase(myLog)

addrssDBIndexConstituent = "\\MktGenInfo\\IndexConstituent_Wind.db"
constituentIndex = "000300"
objBuildPITDB.SetStockUniverse(addrssDBIndexConstituent,constituentIndex)
objBuildPITDB.LoadFundamentalDataItemsToBeProcessed()

namePITDatabase = "PITFundamentalData.db"
objBuildPITDB.CreateDatabase(namePITDatabase)

startDate="20050101"
objBuildPITDB.CalculateAndSaveData(startDate)
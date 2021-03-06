#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/5/16
"""

import os,sys,logging
root = os.path.abspath("D:\\PyQuantLib\\")
sys.path.append(root)

import SynchronizeDatabase.Db_Wind_CICC.SyncFinRptData as SyncFinRpt
import SynchronizeDatabase.Db_Wind_CICC.SyncMktData as SyncMktData
import Tools.LogOutputHandler as LogHandler
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

logHandlers = LogHandler.LogOutputHandler("SyncPrice.log")

sync = SyncMktData.SyncData(logHandlers)
sync.SetStartDate("19900101")
sync.ConvertDatesToMonths()
sync.LoadDataTableConfigs("Configs//MktData_Wind_CICC.cfg")
sync.ConnRmtDb()
sync.CheckRmtDb()
localDbName = "MktData\\MktData_Wind_CICC.db"
sync.ConnLocalDb(localDbName)
sync.CheckLocalDb()
sync.Sync(1)
#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2015/11/25
"""

import os,sys,logging
root = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(root)

import SynchronizeDatabase.Db_Wind_CICC.SyncFinRptData as SyncFinRpt
import SynchronizeDatabase.Db_Wind_CICC.SyncMktData as SyncMktData
import Tools.LogOutputHandler as LogHandler
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

logHandlers = LogHandler.LogOutputHandler("SyncFinRpt.log")

sync = SyncFinRpt.SyncData(logHandlers)
sync.SetStartDate("20020301")
sync.ConvertDatesToMonths()
sync.LoadDataTableConfigs("Configs\\FinRptData_Wind_CICC.cfg")
sync.ConnRmtDb()
sync.CheckRmtDb()
localDbName = "FinRptData\\FinRptData_Wind_CICC.db"
sync.ConnLocalDb(localDbName)
sync.CheckLocalDb()
sync.Sync(1)

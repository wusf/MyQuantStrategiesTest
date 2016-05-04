#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/4/27
"""

import os,sys,logging
root = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(root)

import SynchronizeDatabase.Db_Goal_CICC.SyncAnalystData as SyncAnalystData
import Tools.LogOutputHandler as LogHandler
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'


logHandlers = LogHandler.LogOutputHandler("SyncAnalystData.log")

sync = SyncAnalystData.SyncData(logHandlers)
sync.SetStartDate("20020301")
sync.ConvertDatesToMonths()
sync.LoadDataTableConfigs("Configs\\AnalystData_Goal_CICC.cfg")
sync.ConnRmtDb()
#sync.CheckRmtDb()
localDbName = "AnalystData\\AnalystData_Wind_CICC.db"
sync.ConnLocalDb(localDbName)
sync.CheckLocalDb()
sync.Sync(1)

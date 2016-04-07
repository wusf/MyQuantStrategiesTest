#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2015/12/15
"""

import os,sys,logging
root = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(root)

import SynchronizeDatabase.Db_Wind_CICC.SyncIndexComp as SyncIndexComp
import SynchronizeDatabase.Db_Wind_CICC.SyncTradeDay as SyncTradeDay
import Tools.LogOutputHandler as LogHandler
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

logHandlers = LogHandler.LogOutputHandler("SyncIndexComp.log")

sync = SyncTradeDay.SyncData(logHandlers)
sync.ConnRmtDb()
localDbName = "MktGenInfo\\TradeDate_Wind_CICC.db"
sync.ConnLocalDb(localDbName)
sync.Sync()
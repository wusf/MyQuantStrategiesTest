#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2015/12/14
"""

import os,sys,logging
root = os.path.abspath("D:\\PyQuantLib\\")
sys.path.append(root)

import SynchronizeDatabase.Db_Wind_CICC.SyncIndexComp as SyncIndexComp
import SynchronizeDatabase.Db_Wind_CICC.SyncMktData as SyncMktData
import Tools.LogOutputHandler as LogHandler
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

logHandlers = LogHandler.LogOutputHandler("SyncIndexComp.log")

sync = SyncIndexComp.SyncData(logHandlers)
sync.LoadDataTableConfigs("Configs\\IndexComp_Wind_CICC.cfg")
sync.ConnRmtDb()
sync.CheckRmtDb()
localDbName = "MktGenInfo\\IndexConstituent_Wind_CICC.db"
sync.ConnLocalDb(localDbName)
sync.CheckLocalDb()
sync.Sync(1)

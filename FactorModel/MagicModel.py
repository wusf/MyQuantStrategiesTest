#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/5/26
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3


root = os.path.abspath("D:\\PyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import UpdateFactorDatabase.FundamentalFactors.ComputeFactorValues as modComputeFactor
import FactorModel.ClassicModels.MagicFormula as MF


myLog = logging.Logger("mf", level="DEBUG")
myLogHandler = LogHandler.LogOutputHandler("ComputeFactorICs.log")
fh=myLogHandler[0]
ch=myLogHandler[1]
myLog.addHandler(fh)
myLog.addHandler(ch) 

mf = MF.MagicFormula(myLog)
mf.LoadFactorDatabase("TestFactorDatabase.db",["Fundamental"])
addrssDBIndexConstituent = "\\MktGenInfo\\IndexConstituent_Wind_CICC.db"
constituentIndex = ["000300"]
mf.SetStockUniverse(addrssDBIndexConstituent,constituentIndex)
mf.SetRebalanceDate("20080101","20150101","quarterly",1)
mf.GenerateTradeList(30000)
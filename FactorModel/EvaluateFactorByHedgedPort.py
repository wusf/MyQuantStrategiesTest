#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/6/1
"""

import os,sys,logging,time,decimal,codecs,numpy,re,sqlite3


root = os.path.abspath("D:\\PyQuantLib\\")
sys.path.append(root)
import Tools.LogOutputHandler as LogHandler
import UpdateFactorDatabase.FundamentalFactors.ComputeFactorValues as modComputeFactor
import FactorModel.EvaluateFactors.HedgedPortfolio as HedgedPort
import Backtest.SimpleBacktest as Backtest


myLog = logging.Logger("mf", level="DEBUG")
myLogHandler = LogHandler.LogOutputHandler("ComputeFactorICs.log")
fh=myLogHandler[0]
ch=myLogHandler[1]
myLog.addHandler(fh)
myLog.addHandler(ch) 

hedgedPort = HedgedPort.HedgedPortfolio(myLog)
hedgedPort.LoadFactorDatabase("TestFactorDatabase.db",["Fundamental"])
addrssDBIndexConstituent = "\\MktGenInfo\\IndexConstituent_Wind_CICC.db"
constituentIndex = ["000905"]
hedgedPort.SetStockUniverse(addrssDBIndexConstituent,constituentIndex)
hedgedPort.SetRebalanceDate("20090101","20151231","monthly",1)

factorName1 = "ROIC_TTM"
factorName2 = "EBIT2EV_TTM"
port1 = hedgedPort.GeneratePortfolios(factorName1,180,0.1,[2,3,4],1)
port2 = hedgedPort.GeneratePortfolios(factorName2,180,0.1,[2,3,4],1)

objTest = Backtest.SimpleBacktest(myLog)
addressDBMarketData = "\\MktData\\MktData_Wind_CICC.db"
objTest.LoadDatabase(addressDBMarketData,"20070101",1,None)
objTest.LoadPortfolios(port1)
objTest.Run(factorName1,"20090101","20151231","000300")
objTest.Output(1)

objTest.LoadPortfolios(port2)
objTest.Run(factorName2,"20090101","20151231","000300")
objTest.Output(1)

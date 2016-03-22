#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2015/12/15
"""

import os,sys,logging,pyclbr
MyQtLibPath = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(MyQtLibPath)
import Tools.LogOutputHandler as LogHandler
import Tools.GetModuleNames as ModuleNames
import ProcessRawData.Fundamental.ConsolidateFdmtDerivData as ConsoData
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

logHandlers = LogHandler.LogOutputHandler("GenFundIndic.log")
consoData = ConsoData.ConsolidateData(logHandlers)

consoData.SetStockUniverse("MktGenInfo\\IndexComp_Wind_CICC.db","399906")

algoNames = ModuleNames.GetModuleNames(MyQtLibPath+"\\ProcessRawData\\Fundamental\\FinRptDerivDataAlgos")
algos = []
for algoName in algoNames:
    print algoName
    exec("import ProcessRawData.Fundamental.FinRptDerivDataAlgos.{} as algo".format(algoName))
    algos.append(algo)
consoData.AppendFinRptItems(algos)

algoNames = ModuleNames.GetModuleNames(MyQtLibPath+"\\ProcessRawData\\Fundamental\\ForecastDerivDataAlgos")
algos = []
for algoName in algoNames:
    print algoName
    exec("import ProcessRawData.Fundamental.ForecastDerivDataAlgos.{} as algo".format(algoName))
    algos.append(algo)
consoData.AppendFcstItems(algos)
consoData.CreateDatabase("FumdamentalDerivData.db")
consoData.GenerateData()
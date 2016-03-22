#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2015/12/17
"""

import os,sys
MyQtLibPath = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(MyQtLibPath)
import FactorAlgos.GenRawFactorsAndZScores as GenFactor

if __name__ == "__main__":

    dbPath1 = "FumdamentalDerivData.db"
    dbPath2 = "MktData\\MktData_Wind_CICC.db"   
    dbPath3 = "MktGenInfo\\IndexComp_Wind_CICC.db"    
    GFctZScore = GenFactor.GenRawFactorsAndZScoresDatabase()
    #GFctZScore.LoadSourceData(dbPath1,dbPath2,dbPath3)
    GFctZScore.SetStockUniverseAndRevalueDate("399906","20070101","20160128",20)
    GFctZScore.LoadFactorAlgos("FdmtFactors.Growth","FdmtFactors.Profitability","FdmtFactors.Quality","FdmtFactors.Value","FdmtFactors.Risk","TechnicalFactors")
    #GFctZScore.GenRawFactors()
    GFctZScore.RawFactors2ZScores("399906","Industry.cfg","SW1_ZZ500")







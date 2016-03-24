#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/3/23
"""

import os,sys,sqlite3
MyQtLibPath = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(MyQtLibPath)

import StatArb.PairWithIndex.PairWithMarketIndex as statArb
import pandas as pd
import numpy as np
import time


def ComputeZScores(begDate,endDate,computeZScore,paramsDict,mark):

    regressSampleDays = paramsDict['RegressSampleDays']
    ouSampleDays = paramsDict['OUFitSampleDays']
    ifDeTrend = paramsDict['IfDeTrend']

    days = []
    score=pd.DataFrame()
    score_adj = pd.DataFrame()
    revsD=pd.DataFrame()
    rsqrd=pd.DataFrame()

    c = 0
    for i in range(600,len(computeZScore.trdDay)):
        scoreDate = computeZScore.trdDay[i]
        if scoreDate>=begDate and scoreDate<endDate:   
            c+=1

    tm1 = time.time()
    k = 1
    for i in range(600,len(computeZScore.trdDay)):
        scoreDate = computeZScore.trdDay[i]
        if scoreDate>=begDate and scoreDate<endDate:
            computeZScore.RegressOnIndex(scoreDate,regressSampleDays,3,winsorize=1)
            res = computeZScore.OUFitAndCalcZScore(scoreDate,ouSampleDays,ifDeTrend)
            _score = res.loc['score'].to_frame(scoreDate).transpose()
            _scoreAdj = res.loc['score_adj'].to_frame(scoreDate).transpose()
            _revsD = res.loc['period'].to_frame(scoreDate).transpose()
            #_rsqrd = res[1].to_frame(scoreDate).transpose()
            score = score.append(_score)
            score_adj=score_adj.append(_scoreAdj)
            revsD = revsD.append(_revsD)
            #rsqrd = rsqrd.append(_rsqrd)
            k+=1
            tm2 = time.time()
            deltaT = int((tm2-tm1)/k*(c-k))
            print "Generating zscore,date:{},paras:{}......{}s left".format(scoreDate,regressSampleDays,deltaT)
    score.to_csv("ZScores{}.csv".format(mark))
    score_adj.to_csv("ZScores_adj{}.csv".format(mark))
    revsD.to_csv("ReversePerid{}.csv".format(mark))
    #rsqrd.to_csv("RegressionRSquared{}.csv".format(mark))




if __name__=="__main__":
    computeZScore = statArb.PairWithMarketIndex("MktData\\MktData_Wind_CICC.db", 1,"20050104")
    computeZScore.LoadDataIntoTimeSeries("000905","000905",1)   
    begDate = "20080101"
    endDate = "20160310"
    params1 = {}
    params1['RegressSampleDays']=180
    params1['OUFitSampleDays']=60
    params1['IfDeTrend']=0


    ComputeZScores(begDate,endDate,computeZScore,params1,'Params501')





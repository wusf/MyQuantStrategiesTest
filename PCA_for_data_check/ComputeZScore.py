#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/2/29
"""

import os,sys,sqlite3
MyQtLibPath = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(MyQtLibPath)

import PCA.PCA_For_Stat_Arb_for_check as pca
import pandas as pd
import numpy as np
import time


def ComputeZScores(begDate,endDate,computeZScore,paramsDict,mark):

    v = paramsDict['EigenNum']
    varPecent = paramsDict['VarExplained']
    corrSampleDays = paramsDict['CorrMatSampleDays']
    regressSampleDays = paramsDict['RegressSampleDays']
    ouSampleDays = paramsDict['OUFitSampleDays']
    ifDeTrend = paramsDict['IfDeTrend']
    ifAdjustReturnByVol = paramsDict['IfAdjRetByVol']

    
    days = []
    score=pd.DataFrame()
    score_adj = pd.DataFrame()
    revsD=pd.DataFrame()
    rsqrd=pd.DataFrame()
    significantEigNum = []
    
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
            if k==1 or i%1==0:
                reEstCorrDay = computeZScore.trdDay[i]
                computeZScore.GenEigenPort(reEstCorrDay,v,varPecent,corrSampleDays,0.05)
                print "Re estimate correlation matrix and process PCA"
            computeZScore.RegressOnEigenFactor(scoreDate,regressSampleDays,ifAdjustReturnByVol,winsorize=0)
            res = computeZScore.OUFitAndCalcZScore(ouSampleDays,ifDeTrend)
            significantEigNum.append(computeZScore.significantEigNum)
            _score = res[0].loc['score'].to_frame(scoreDate).transpose()
            _scoreAdj = res[0].loc['score_adj'].to_frame(scoreDate).transpose()
            _revsD = res[0].loc['period'].to_frame(scoreDate).transpose()
            _rsqrd = res[1].to_frame(scoreDate).transpose()
            score = score.append(_score)
            score_adj=score_adj.append(_scoreAdj)
            revsD = revsD.append(_revsD)
            rsqrd = rsqrd.append(_rsqrd)
            k+=1
            tm2 = time.time()
            deltaT = int((tm2-tm1)/k*(c-k))
            print "Generating zscore,date:{},paras:{}|{}|{}|{}......{}s left".format(scoreDate,v,varPecent,corrSampleDays,regressSampleDays,deltaT)
    score.to_csv("ZScores{}.csv".format(mark))
    score_adj.to_csv("ZScores_adj{}.csv".format(mark))
    revsD.to_csv("ReversePerid{}.csv".format(mark))
    rsqrd.to_csv("RegressionRSquared{}.csv".format(mark))
    np.savetxt("sigEigNum{}.csv".format(mark), np.array(significantEigNum), delimiter=",")




if __name__=="__main__":
    computeZScore = pca.PCA_For_Stat_Arb("MktData\\MktData_Wind_CICC.db", 1,"20050104")
    computeZScore.LoadDataIntoTimeSeries("000905","000905",1)   
    begDate = "20150720"
    endDate = "20150721"
    
    params1 = {}
    params1['EigenNum']=0
    params1['VarExplained']=0.55
    params1['CorrMatSampleDays']=250
    params1['RegressSampleDays']=60
    params1['OUFitSampleDays']=60
    params1['IfDeTrend']=0
    params1['IfAdjRetByVol']=0
    
    ComputeZScores(begDate,endDate,computeZScore,params1,'Params1')




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

import PCA.PCA_For_Stat_Arb2 as pca
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
            computeZScore.RegressOnEigenFactor(scoreDate,regressSampleDays,ifAdjustReturnByVol,winsorize=1)
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
    begDate = "20080101"
    endDate = "20160310"
    params1 = {}
    params1['EigenNum']=5
    params1['VarExplained']=0.55
    params1['CorrMatSampleDays']=300
    params1['RegressSampleDays']=180
    params1['OUFitSampleDays']=60
    params1['IfDeTrend']=0
    params1['IfAdjRetByVol']=0
    
    params2 = {}
    params2['EigenNum']=0
    params2['VarExplained']=0.55
    params2['CorrMatSampleDays']=250
    params2['RegressSampleDays']=60
    params2['OUFitSampleDays']=60
    params2['IfDeTrend']=0
    params2['IfAdjRetByVol']=0   
    
    params3 = {}
    params3['EigenNum']=0
    params3['VarExplained']=0.55
    params3['CorrMatSampleDays']=300
    params3['RegressSampleDays']=60
    params3['OUFitSampleDays']=60
    params3['IfDeTrend']=0
    params3['IfAdjRetByVol']=0       
    
    params4 = {}
    params4['EigenNum']=18
    params4['VarExplained']=0.55
    params4['CorrMatSampleDays']=250
    params4['RegressSampleDays']=60
    params4['OUFitSampleDays']=60
    params4['IfDeTrend']=0
    params4['IfAdjRetByVol']=0       
    
    params5 = {}
    params5['EigenNum']=15
    params5['VarExplained']=0.60
    params5['CorrMatSampleDays']=250
    params5['RegressSampleDays']=60
    params5['OUFitSampleDays']=60
    params5['IfDeTrend']=0
    params5['IfAdjRetByVol']=0     
    
    params6 = {}
    params6['EigenNum']=10
    params6['VarExplained']=0.65
    params6['CorrMatSampleDays']=250
    params6['RegressSampleDays']=60
    params6['OUFitSampleDays']=60
    params6['IfDeTrend']=0
    params6['IfAdjRetByVol']=0    
    
    params7 = {}
    params7['EigenNum']=5
    params7['VarExplained']=0.60
    params7['CorrMatSampleDays']=250
    params7['RegressSampleDays']=60
    params7['OUFitSampleDays']=60
    params7['IfDeTrend']=0
    params7['IfAdjRetByVol']=0      
    
    ComputeZScores(begDate,endDate,computeZScore,params1,'Params501')
    ComputeZScores(begDate,endDate,computeZScore,params2,'Params502')
    ComputeZScores(begDate,endDate,computeZScore,params3,'Params503')
    ComputeZScores(begDate,endDate,computeZScore,params4,'Params504')
    ComputeZScores(begDate,endDate,computeZScore,params5,'Params505')
    ComputeZScores(begDate,endDate,computeZScore,params6,'Params506')
    ComputeZScores(begDate,endDate,computeZScore,params7,'Params507')




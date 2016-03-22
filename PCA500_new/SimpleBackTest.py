#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wushifan --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/3/1
"""

import os,sys,sqlite3
MyQtLibPath = os.path.abspath("D:\\MyQuantLib\\")
sys.path.append(MyQtLibPath)

import PCA.PCA_For_Stat_Arb2 as pca
import pandas as pd



#----------------------------------------------------------------------
def Backtest(computeZScoreObj,scoreFile,revsFile,entry,exit,revsThreshold,dd):
    """"""
    score = pd.read_csv(scoreFile,index_col=0)
    score.index = score.index.astype('str')
    #score = score.rank(axis=1,pct=True)-0.5
    #mean = pd.rolling_mean(score,5)
    #std = pd.rolling_std(score,5)
    #score = (score-mean)/std
    revsT = pd.read_csv(revsFile,index_col=0)
    revsT.index = score.index.astype('str')    
    ret = computeZScoreObj.SimpleBacktest(score,revsT,entry,exit,revsThreshold,"",dd)
    return ret
    
if __name__=="__main__":

    computeZScore = pca.PCA_For_Stat_Arb("MktData\\MktData_Wind_CICC.db", 1,"20050101")
    computeZScore.LoadDataIntoTimeSeries("000905","000905",1)
    
    entry = 1.8
    exit =  0.40
    revsT = 30
    dd = 1
    params = "Params501"
    
    rets = pd.DataFrame()
    posi = pd.DataFrame()    
    for params in ["Params502"]:#,"Params502","Params503","Params504","Params505","Params506","Params507"]:#,"Params4","Params5"]:
        scoreFile = "ZScores_adj{}.csv".format(params)
        revsFile = "ReversePerid{}.csv".format(params)        
        print "Run backtest, param: {}, value:{}".format('score',params)
        ret = Backtest(computeZScore, scoreFile, revsFile, entry, exit, revsT,dd)
        rets = pd.concat([rets,ret[0]],axis=1)
        posi = pd.concat([posi,ret[1]],axis=1)
    rets.to_csv("HedgedReturn{}.csv".format("_ZScoreTest"))
    rets.cumsum().to_csv("CumReturn{}.csv".format("_ZScoreTest"))
    posi.to_csv("Position{}.csv".format("_ZScoreTest"))   
    
    #entry = 1.6
    #exit =  1.0005
    #revsT = 10
    #dd = 0
    #params = "Params503"
    
    #rets = pd.DataFrame()
    #posi = pd.DataFrame()     
    #for dd in [0,1,2,3,4,5,6,7,8]:
        #scoreFile = "ZScores{}.csv".format(params)
        #revsFile = "ReversePerid{}.csv".format(params)        
        #print "Run backtest, param: {}, value:{}".format('delay',dd)
        #ret = Backtest(computeZScore, scoreFile, revsFile, entry, exit, revsT,dd)
        #rets = pd.concat([rets,ret[0]],axis=1)
        #posi = pd.concat([posi,ret[1]],axis=1)        
    #rets.to_csv("HedgedReturn{}.csv".format("_DelayTest"))
    #rets.cumsum().to_csv("CumReturn{}.csv".format("_DelayTest"))
    #posi.to_csv("Position{}.csv".format("_DelayTest"))
    
    #entry = 1.6
    #exit =  1.0005
    #revsT = 10
    #dd = 0
    #params = "Params503"    
    
    #rets = pd.DataFrame()
    #posi = pd.DataFrame()     
    #for entry in [1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]:
        #scoreFile = "ZScores{}.csv".format(params)
        #revsFile = "ReversePerid{}.csv".format(params)        
        #print "Run backtest, param: {}, value:{}".format('entry',entry)
        #ret = Backtest(computeZScore, scoreFile, revsFile, entry, exit, revsT,dd)
        #rets = pd.concat([rets,ret[0]],axis=1)
        #posi = pd.concat([posi,ret[1]],axis=1)        
    #rets.to_csv("HedgedReturn{}.csv".format("_EntryTest"))
    #rets.cumsum().to_csv("CumReturn{}.csv".format("_EntryTest"))
    #posi.to_csv("Position{}.csv".format("_EntryTest"))    
    
    #entry = 1.6
    #exit =  1.0005
    #revsT = 10
    #dd = 0
    #params = "Params503"    
    
    #rets = pd.DataFrame()
    #posi = pd.DataFrame()     
    #for exit in [0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6]:
        #scoreFile = "ZScores{}.csv".format(params)
        #revsFile = "ReversePerid{}.csv".format(params)        
        #print "Run backtest, param: {}, value:{}".format('exit',exit)
        #ret = Backtest(computeZScore, scoreFile, revsFile, entry, exit, revsT,dd)
        #rets = pd.concat([rets,ret[0]],axis=1)
        #posi = pd.concat([posi,ret[1]],axis=1)        
    #rets.to_csv("HedgedReturn{}.csv".format("_ExitTest"))
    #rets.cumsum().to_csv("CumReturn{}.csv".format("_ExitTest"))
    #posi.to_csv("Position{}.csv".format("_ExitTest"))    
    
    #entry = 1.6
    #exit =  1.0005
    #revsT = 10
    #dd = 0
    #params = "Params503"    
    
    #rets = pd.DataFrame()
    #posi = pd.DataFrame()     
    #for revsT in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        #scoreFile = "ZScores{}.csv".format(params)
        #revsFile = "ReversePerid{}.csv".format(params)        
        #print "Run backtest, param: {}, value:{}".format('revsT',revsT)
        #ret = Backtest(computeZScore, scoreFile, revsFile, entry, exit, revsT,dd)
        #rets = pd.concat([rets,ret[0]],axis=1)
        #posi = pd.concat([posi,ret[1]],axis=1)        
    #rets.to_csv("HedgedReturn{}.csv".format("_RevsTTest"))
    #rets.cumsum().to_csv("CumReturn{}.csv".format("_RevsTTest"))
    #posi.to_csv("Position{}.csv".format("_RevsTTest"))        
    
    #entry = 2.1
    #exit =  0
    #revsT = 30
    #dd = 0
    #params = "Params507"    
    
    #rets = pd.DataFrame()
    #posi = pd.DataFrame()     
 
    #scoreFile = "ZScores{}.csv".format(params)
    #revsFile = "ReversePerid{}.csv".format(params)        
    #print "Run backtest, param: {}, value:{}".format('best',1)
    #ret = Backtest(computeZScore, scoreFile, revsFile, entry, exit, revsT,dd)
    #rets = pd.concat([rets,ret[0]],axis=1)
    #posi = pd.concat([posi,ret[1]],axis=1)        
    #rets.to_csv("HedgedReturn{}.csv".format("_best"))
    #rets.cumsum().to_csv("CumReturn{}.csv".format("_best"))
    #posi.to_csv("Position{}.csv".format("_best"))            
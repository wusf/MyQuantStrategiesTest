import numpy
import pandas as pd


def CalcZScore(_x,drift):
    """"""
    l = len(_x)
    xm = numpy.mean(_x)
    st = float(xm/l) 
    if drift==1:
        tr = numpy.linspace(st,xm,l)
        x = (numpy.array(_x)-tr).tolist()
    else:
        x = _x
    print x
    y = x[1:]
    X = numpy.vstack((x[0:-1],numpy.ones(len(x)-1))).T
    res = numpy.linalg.lstsq(X,y)
    a = res[0][1]
    b = res[0][0]
    r = y - numpy.dot(X,res[0])
    v = numpy.var(r)
    k = -numpy.log(b)*250
    m = a/(1-b)
    sig = numpy.sqrt(v*2*k/(1-b**2))
    sigEq = numpy.sqrt(v/(1-b**2))
    s = (x[-1]-m)/sigEq
    #print s
    #print k
    return pd.Series({'m':-m,'s':sigEq,'period':250/k,'score':s})


a= CalcZScore([2,3,4,5,6,6,7,7,8],1)

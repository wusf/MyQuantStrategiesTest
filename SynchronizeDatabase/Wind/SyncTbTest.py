import os,sys,logging
root = os.path.abspath("D:\\PyQuantStrategy\\")
sys.path.append(root)

import SynchronizeDatabase.Db_Wind_CICC.SyncFinRptData as SyncFinRpt
import SynchronizeDatabase.Db_Wind_CICC.SyncMktData as SyncMktData
#import SynchronizeDatabase.CICCWindDb.SyncStkBasicInfo as SyncStkBasic
import Tools.LogOutputHandler as LogHandler
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

#sync1 = SyncStkBasic.SyncStkBasicInfo()
#sync1.LoadDataTableConfigs("StkBasicInfo.cfg")
#sync1.ConnRmtDb()
#sync1.CheckRmtDb()
#localDbName = "MktGenInfo\\StkBasicInfo.db"
#sync1.ConnLocalDb(localDbName)
#sync1.CheckLocalDb()
#sync1.Sync(1)

logHandlers = LogHandler.LogOutputHandler("SyncPrice.log")

#sync = SyncFinRpt.SyncData(logHandlers)
#sync.SetStartDate("20120301")
#sync.ConvertDatesToMonths()
#sync.LoadDataTableConfigs("tbs.cfg")
#sync.ConnRmtDb()
#sync.CheckRmtDb()
#localDbName = "test2.db"
#sync.ConnLocalDb(localDbName)
#sync.CheckLocalDb()
#sync.Sync(0)

sync = SyncMktData.SyncData(logHandlers)
sync.SetStartDate("20030101")
sync.ConvertDatesToMonths()
sync.LoadDataTableConfigs("MktDataTables.cfg")
sync.ConnRmtDb()
sync.CheckRmtDb()
localDbName = "MktData\\Price.db"
sync.ConnLocalDb(localDbName)
sync.CheckLocalDb()
sync.Sync(0)
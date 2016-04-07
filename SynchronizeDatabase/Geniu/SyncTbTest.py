import os,sys,logging
root = os.path.abspath("D:\\PyQuantStrategy\\")
sys.path.append(root)

import SynchronizeDatabase.Db_Geniu_CICC.SyncFinRptData as Sync
import SynchronizeDatabase.Db_Geniu_CICC.SyncStkBasicInfo as SyncStkBasic
import Tools.LogOutputHandler as LogHandler

#sync1 = SyncStkBasic.SyncStkBasicInfo()
#sync1.LoadDataTableConfigs("StkBasicInfo.cfg")
#sync1.ConnRmtDb()
#sync1.CheckRmtDb()
#localDbName = "MktGenInfo\\StkBasicInfo.db"
#sync1.ConnLocalDb(localDbName)
#sync1.CheckLocalDb()
#sync1.Sync(1)

logHandlers = LogHandler.LogOutputHandler("log.log")

sync = Sync.SyncFinDataDb(logHandlers)
sync.SetStartDate("20120301")
sync.ConvertDatesToMonths()
sync.LoadDataTableConfigs("tbs.cfg")
sync.ConnRmtDb()
sync.CheckRmtDb()
localDbName = "test.db"
sync.ConnLocalDb(localDbName)
sync.CheckLocalDb()
sync.Sync(0)
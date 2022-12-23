'''
Created on 2022-12-22

@author: wf
'''
import os
from pathlib import Path
from lodstorage.sql import SQLDB
from plp.download import Download

class EventSignature:
    """
    event Signature extract of Conference Corpus database
    """
    
    def __init__(self,debug:bool=False):
        """
        construct me
        
        Args:
            debug(bool): if True switch debugging mode one
        """
        debug=debug
        self.sqlDB=self.getSignatureDB()
        #self.events=self.sqlDB.query("select * from event")
        #if self.debug:
        #    print(f"found {len(self.events)} events")
            
    def getDbPath(self)->str:
        """
        get my database path
        
        Returns:
            tuple(str,str): the database path and database name
        """
        home=str(Path.home())
        dbDir=f"{home}/.conferencecorpus" 
        os.makedirs(dbDir,exist_ok=True)
        dbName=f"Signature.db"
        return dbDir,dbName
            
    def getSignatureDB(self,fromBackup:bool=False):
        """
        get the event Signature Database
        
        Args:
            fromBackup(bool): if True load the database file
            from the backup
            
        Returns:
            SQLDB: the SQL database
        """
        dbDir,dbName=self.getDbPath()
        url=f"https://confident.dbis.rwth-aachen.de/downloads/conferencecorpus/{dbName}.gz"
        dbPath=Download.downloadBackupFile(url, dbName, dbDir)
        signatureDB=SQLDB(dbPath)
        return signatureDB
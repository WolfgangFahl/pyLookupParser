'''
Created on 2023-01-01

@author: wf
'''
from tests.basetest import BaseTest
from plp.eventrefparser import EventReferenceParser
from plp.eventsignature import EventSignature
from plp.acronym import Acronym
from lodstorage.sql import EntityInfo

class TestTrueAcronyms(BaseTest):
    """
    tests true Acronyms
    """
    
    def testAcronymExpansion(self):
        """
        test the expansion of acronyms
        """
        test_records=[
            ("NATO","The North Atlantic Treaty Organization is ","North Atlantic Treaty Organization"),
            ("FBI","Where is the Federal Bureau of Investigation","Federal Bureau Investigation"),
            ("ISWC","The 1st International Semantic Web Conference took place in Italy","International Semantic Web Conference"),
            ("TLA","A Three Letter Acronym is an acronym with three letters", "Three Letter Acronym"),
            ("NAA","NAA is not the acronym for Not an Acronym since an is lowercase",None)
        ]
        for acronym,text,expected in test_records:
            expanded_acronym=Acronym.expand_acronym(acronym, text)
            self.assertEqual(expected,expanded_acronym)
    
    def testTrueAcronyms(self):
        """
        test titles versus acronyms
        """
        eventSignature=EventSignature()
        signatureDB=eventSignature.sqlDB
        limit =10000000
        sql_query=f"select * from event where acronym is not null limit {limit}"
        event_records=signatureDB.query(sql_query)
        acronym_records=[]
        debug=True
        verbose=False
        if debug:
            print(f"found {len(event_records)} events")
        counter=0
        for index,event_record in enumerate(event_records):
            title=event_record["title"]
            acronym=event_record["acronym"]
            expanded=Acronym.expand_acronym(acronym, title)
            if expanded is not None:
                counter+=1
                if debug and verbose:
                    print(f"{acronym}:{expanded}")
                event_record["expanded_acronym"]=expanded
                acronym_records.append(event_record)
            if (index+1)%10000==0 and debug:
                print(f"{index+1:6}:{counter:6} {counter/(index+1)*100:5.1f}%")
        withStore=False
        if withStore:
            entityInfo=signatureDB.createTable(acronym_records,entityName="event_w_acronym",primaryKey='eventId',withDrop=True)
            signatureDB.store(acronym_records,entityInfo,executeMany=True,fixNone=True,replace=True)
     

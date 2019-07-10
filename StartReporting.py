'''
Created on Jun 22, 2019

@author: DIDIT SETIAWAN
'''
import os
import jpype as jp
import datetime
import configuration

class StartReporting():
    Report_Name = configuration.report_name
    now         = datetime.datetime.now()
    datenow     = now.strftime("%d-%m-%Y")
    #set classpath
    bson        = os.getcwd()+os.path.join('/','lib','bson-3.3.0.jar')
    extent      = os.getcwd()+os.path.join('/','lib','extentreports-2.41.2.jar')
    freemaker   = os.getcwd()+os.path.join('/','lib','freemarker-2.3.23.jar')
    jsoup       = os.getcwd()+os.path.join('/','lib','jsoup-1.9.2.jar')
    mongodrive  = os.getcwd()+os.path.join('/','lib','mongodb-driver-3.3.0.jar')
    mongocore   = os.getcwd()+os.path.join('/','lib','mongodb-driver-core-3.3.0.jar')
    sqlite      = os.getcwd()+os.path.join('/','lib','sqlite-jdbc-3.8.11.1.jar')
    classpath = os.pathsep.join((bson,extent,freemaker,jsoup,mongodrive,mongocore,sqlite))
    #start JVM
    jp.startJVM(jp.getDefaultJVMPath(),"-ea", "-Djava.class.path=%s" % classpath)
    #store extent function
    ExtentReports   = jp.JClass('com.relevantcodes.extentreports.ExtentReports')
    ExtentTest      = jp.JClass('com.relevantcodes.extentreports.ExtentTest')
    LogStatus       = jp.JClass('com.relevantcodes.extentreports.LogStatus')
    reportpath      = os.path.join('TEST_RESULT','HTML Report',Report_Name+'_'+datenow+'.html')
    extent          = ExtentReports(reportpath)

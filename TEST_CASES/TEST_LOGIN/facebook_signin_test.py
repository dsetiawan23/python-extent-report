'''
Created on Jun 22, 2019

@author: DIDIT SETIAWAN
'''
import unittest
import StartReporting
from PUBLIC_FUNCTION import func_library
from TEST_CASES.TEST_LOGIN import facebook_signin

class Sign_In_Test(unittest.TestCase):
    #init test
    browser         = func_library.Function.driver
    test_suite      = StartReporting.StartReporting
    #store extent function
    LogStatus       = test_suite.LogStatus
    extent          = test_suite.extent
    parent          = extent.startTest("Facebook Sign In Test")
    #call testcase module
    face_sign       = facebook_signin.Facebooklogin
    
    #setup
    def setUp(self):
        #declare to use browser
        self.driver = Sign_In_Test.browser
        #make variable for easy access
        driver = self.driver
        #maximize Firefox
        driver.maximize_window()
        #go to maukerja
        driver.get("https://www.facebook.com/")
    
    #start login test case 1
    #one node test
    test1      = extent.startTest("Facebook Login Valid All Input")
    def test_001_Facebook_Valid(self):
        Test      = Sign_In_Test.face_sign
        xtent = [Sign_In_Test.test1,Sign_In_Test.LogStatus]
        #call testcase
        Test.login_valid(xtent)
        Sign_In_Test.parent.appendChild(Sign_In_Test.test1)

    #start mock test 2
    #parent test
    testparent      = extent.startTest("This is parent")
    testchild       = extent.startTest("This is childtest - 1")
    testchild1       = extent.startTest("This is childtest - 2")
    def test_002_node_test(self):
        '''FOR THE REAL FUNCTION, BETTER TO MAKE SAME AS test001 where the class is outside this file'''
        print('This is only mock function')
        print('Just edit this line to real function to see how its works')
        Sign_In_Test.testchild.log(Sign_In_Test.LogStatus.INFO, 'Example of steps')
        Sign_In_Test.testchild1.log(Sign_In_Test.LogStatus.INFO, 'Example of steps')
        Sign_In_Test.testparent.appendChild(Sign_In_Test.testchild)
        Sign_In_Test.testparent.appendChild(Sign_In_Test.testchild1)  
        
    #shutdown test
    def test_999_ShutDownTest(self):
        #END EACH TEST PARENT
        Sign_In_Test.extent.endTest(Sign_In_Test.testparent)
        Sign_In_Test.extent.endTest(Sign_In_Test.parent)
        #push data to report
        Sign_In_Test.extent.flush()
        
if __name__ == '__main__':
    unittest.main()
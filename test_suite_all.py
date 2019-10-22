from TEST_CASES.TEST_LOGIN import facebook_signin_test
from PUBLIC_FUNCTION import func_library
import unittest
import jpype as jp

class MyTestSuite(unittest.TestCase):
    driver         = func_library.Function.driver
    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(facebook_signin_test.Sign_In_Test),                                                
            ])
        
        runner1=unittest.TextTestRunner()
        runner1.run(smoke_test)
        
    def tearDown(self):
        #closing driver
        MyTestSuite.driver.close()
        #shutdown JVM
        jp.shutdownJVM()
        
if __name__ == '__main__':
    unittest.main(exit=False)
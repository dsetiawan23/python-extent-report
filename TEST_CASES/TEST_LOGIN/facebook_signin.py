'''
Created on Jun 22, 2019

@author: DIDIT SETIAWAN
'''
from PUBLIC_FUNCTION import func_library
from PUBLIC_FUNCTION import object_repository
obj = object_repository
action = func_library.Action
function = func_library.Function
class Facebooklogin():
    """This class is for facebook login testcases"""
    print('Import Facebook Login Test')
    #Initiate Function Lib
    @staticmethod
    def login_valid(extent):
        """Login with valid credential"""
        o_b = obj.login_element
        #wait page loaded & accessible
        action.wait_element_id(o_b.email_field, '', extent, 'Waiting page loaded')
        action.wait_clickable_id(30, o_b.email_field, extent, 'Waiting page loaded')
        #write text into email & password field
        action.send_text_id(o_b.email_field, o_b.email_input, extent, 'Write on email field')
        action.send_text_id(o_b.password_field, o_b.password_input, extent, 'Write on password field')
        #tap on login button
        action.tap_by_id(o_b.login_button, extent, 'Tap on login button')
        #wait account logged in
        action.wait_element_xpath(o_b.verify_object, '', extent, 'Wait page loaded')
        action.wait_clickable_xpath(30, o_b.verify_object, extent, 'Wait profile picture clickable')
        #Check testcase is passed or failed
        result = action.is_element_xpath_present(o_b.verify_object)
        print(result)
        function.positivecase('Login Facebook', result, extent)
        
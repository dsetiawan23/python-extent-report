'''
Created on Jun 22, 2019

@author: DIDIT SETIAWAN
'''
import os
import datetime
import configuration
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class Function():
    """Basic common function class"""
    print('Importing Function Lib')
    chrome_options = webdriver.ChromeOptions()
    now = datetime.datetime.now()
    datenow = now.__str__()
    #headless settings
    headless = configuration.option_headless
    #headless configuration
    if headless is True:
        chrome_options.headless = True
        print('Chrome is running headless')
        print('Start running at '+datenow)
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-impl-side-painting')
        chrome_options.add_argument('--disable-gpu-sandbox')
        chrome_options.add_argument('--disable-accelerated-2d-canvas')
        chrome_options.add_argument('--disable-accelerated-jpeg-decoding')
        chrome_options.add_argument('window-size=1920,1080')
    elif headless is False:
        chrome_options.headless = False
    #add chrome option
    prefs = {"profile.default_content_setting_values.notifications":2, "javascript.enabled" : True}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    #sign datetime
    now = datetime.datetime.now()
    datenow = now.strftime("%d-%m-%Y")
    @staticmethod
    def get_locator(locators, obj):
        """Get element function"""
        driver = Function.driver
        if locators == 'ID':
            element = driver.find_element_by_id(obj)
        elif locators == 'NAME':
            element = driver.find_element_by_name(obj)
        elif locators == 'XPATH':
            element = driver.find_element_by_xpath(obj)
        elif locators == 'CSSSELECTOR':
            element = driver.find_element_by_css_selector(obj)
        elif locators == 'CLASSNAME':
            element = driver.find_element_by_class_name(obj)
        elif locators == 'TAGNAME':
            element = driver.find_element_by_tag_name(obj)
        return element
    @staticmethod
    def get_locators(locators, obj):
        """Get elements function"""
        driver = Function.driver
        if locators == 'ID':
            element = driver.find_elements_by_id(obj)
        elif locators == 'NAME':
            element = driver.find_elements_by_name(obj)
        elif locators == 'XPATH':
            element = driver.find_elements_by_xpath(obj)
        elif locators == 'CSSSELECTOR':
            element = driver.find_elements_by_css_selector(obj)
        elif locators == 'CLASSNAME':
            element = driver.find_elements_by_class_name(obj)
        elif locators == 'TAGNAME':
            element = driver.find_elements_by_tag_name(obj)
        return element
    #Tap Element By Locators
    @staticmethod
    def tap_element(locator, obj, extent, scenario):
        """Tap element with ID locator"""
        print('Clicking on '+obj)
        extent[0].log(extent[1].INFO, scenario)
        element = Function.get_locators(locator, obj)
        try:
            btn_next = element
            i = 0
            while not btn_next:
                sleep(1)
                i = i + 1
                if i == 30:
                    break
                next_obj = element
                if next_obj:
                    break
            element[0].click()
        except NoSuchElementException:
            extent[0].log(extent[1].ERROR, 'Element not found or not accessible.')
            Function.write_error_logs(Function.datenow, scenario, obj) 
    #Check Element Present
    @staticmethod
    def is_element_is_present(locator, obj):
        """Checking element is present using ID locator"""
        try:
            Function.get_locator(locator, obj)
            result = True
        except NoSuchElementException:
            result = False
        return result  
    #Waiting Element
    @staticmethod
    def wait_element(locator, expect, unexpect, extent, scenario):
        """Waiting element is present using ID locator"""
        print('30s Waiting element '+expect)
        extent[0].log(extent[1].INFO, scenario)
        element1 = Function.get_locators(locator, expect)
        if unexpect:
            element2 = Function.get_locators(locator, unexpect)
        elewait = element1
        i = 0
        try:
            while not elewait:
                sleep(1)
                i = i+1
                if i == 30:
                    break
                next_obj = element1
                if next_obj:
                    print(expect+' Found in '+str(i)+' seconds')
                    extent[0].log(extent[1].INFO, expect+' Found in '+str(i)+' seconds')
                    break
                if unexpect:
                    unexp = element2
                    if unexp:
                        print(unexpect+' Found in '+str(i)+' seconds')
                        extent[0].log(extent[1].INFO, unexpect+' Found in '+str(i)+' seconds')
                        break
        except NoSuchElementException:
            extent[0].log(extent[1].ERROR, 'Element not found or not accessible.')
            Function.write_error_logs(Function.datenow, scenario, expect)
    #Send Text To Element
    @staticmethod
    def write_text(locator, obj, text, extent, scenario):
        """Writting to element using ID locator"""
        print('Will write "'+text+'" to "'+obj+'" ...')
        extent[0].log(extent[1].INFO, scenario)
        element = Function.get_locators(locator, obj)
        try:
            btn_next = element
            while not btn_next:
                next_obj = element
                if next_obj:
                    break
            element[0].send_keys(text)
            print('Write "'+text+'" to "'+obj+'" finished')
            extent[0].log(extent[1].INFO, 'Write "'+text+'" to "'+obj+'" finished')
        except NoSuchElementException:
            extent[0].log(extent[1].ERROR, 'Element not found or not accessible.')
            Function.write_error_logs(Function.datenow, scenario, obj)
    #Clear Textfield
    @staticmethod
    def clear_textfield(locator, obj, extent, scenario):
        """Clear field element using ID locator"""
        print('Clear text from '+obj)
        element = Function.get_locator(locator, obj)
        try:
            extent[0].log(extent[1].INFO, scenario)
            element.clear()
        except NoSuchElementException:
            extent[0].log(extent[1].ERROR, 'Element not found or not accessible.')
            Function.write_error_logs(Function.datenow, scenario, obj)
    #Positive Testcase
    @staticmethod
    def positivecase(casename, result, extent):
        """Generate positive case result to report"""
        if result:
            logg = "Testcase "+casename+" is PASSED"
            extent[0].log(extent[1].PASS, logg)
        else:
            logg = "Testcase "+casename+" is FAILED"
            extent[0].log(extent[1].FAIL, logg)
        print(logg)
        return logg
    #Negative Testcase
    @staticmethod
    def negativecase(casename, result, extent):
        """Generate negative case result to report"""
        if result:
            logg = "Testcase "+casename+" is PASSED"
            extent[0].log(extent[1].PASS, logg)
        else:
            logg = "Testcase "+casename+" is FAILED"
            extent[0].log(extent[1].FAIL, logg)
        print(logg)
        return logg
    #wait timer
    @staticmethod
    def waittimer(seconds, extent, scenario):
        """Sleep function with countdown timer on log"""
        extent[0].log(extent[1].INFO, scenario)
        for x_x in range(seconds):
            print('Waiting for '+str(x_x+1)+' seconds')
            sleep(1)
    #Wait Element Clickable
    @staticmethod
    def wait_ele_clickable(by, seconds, obj, extent, scenario):
        """Waiting element clickable using XPATH locator"""
        extent[0].log(extent[1].INFO, scenario)
        try:
            WebDriverWait(Function.driver, seconds).until(
                EC.element_to_be_clickable((by, obj))
            )
        except NoSuchElementException:
            extent[0].log(extent[1].ERROR, 'Element not found or not accessible.')
            Function.write_error_logs(Function.datenow, scenario, obj)
        except TimeoutException:
            extent[0].log(extent[1].ERROR, 'Element not found or not accessible.')
            Function.write_error_logs(Function.datenow, scenario, obj)
    #scroll to element
    @staticmethod
    def scroll_to_element(locator, obj, extent, scenario):
        """Scroll to element using XPATH locator"""
        driver = Function.driver
        try:
            element = Function.get_locator(locator, obj)
            location = element.location
            cord_y = location['y']-200
            cord_x = location['x']
            driver.execute_script("window.scrollTo("+str(cord_x)+", "+str(cord_y)+")")
        except NoSuchElementException:
            extent[0].log(extent[1].ERROR, 'Element not found or not accessible.')
            Function.write_error_logs(Function.datenow, scenario, obj)
    #extract number from string
    @staticmethod
    def extract_nbr(input_str):
        """Extract number from string"""
        if input_str is None or input_str == '':
            return 0
        out_number = ''
        for ele in input_str:
            if ele.isdigit():
                out_number += ele
        return int(out_number)
    #get text
    @staticmethod
    def get_text_field(locator, obj, extent):
        """Get text from element using XPATH locators"""
        try:
            element = Function.get_locator(locator, obj)
            text = element.text
            extent[0].log(extent[1].INFO, obj+' Found')
        except NoSuchElementException:
            text = obj+'Element not found'
            extent[0].log(extent[1].FAIL, obj+' Not Found')
        return text
    @staticmethod
    def write_error_logs(datenow, test, obj):
        """Writing error logs to file"""
        filename = 'Error_Logs_'+datenow+'.txt'
        path = os.getcwd()+os.path.join('/', 'TEST_RESULT', 'Error Logs', filename)
        Function.write_file(path, [obj+' is error on test '+test+'\n \n'])
    @staticmethod
    def write_file(file, strlist):
        """Write and saving file"""
        line = 0
        lines = []
        while line < len(strlist):
            lines.append(Function.cheeky_new(line) + strlist[line])
            line += 1
        file = open(file, "a+")
        file.writelines(lines)
        file.close()
    @staticmethod
    def cheeky_new(line):
        """Check new lines on error logs"""
        if line != 0:
            return "\n"
        return ""
class Action():
    """Basic common action class"""
    driver = Function.driver
    #Tap Element By ID
    @staticmethod
    def tap_by_id(obj, extent, scenario):
        Function.tap_element('ID', obj, extent, scenario)        
    #Tap Element By NAME
    @staticmethod
    def tap_by_name(obj, extent, scenario):
        Function.tap_element('NAME', obj, extent, scenario) 
    #Tap Element By XPATH
    @staticmethod
    def tap_by_xpath(obj, extent, scenario):
        Function.tap_element('XPATH', obj, extent, scenario) 
    #Tap Element By CSS SELECTOR
    @staticmethod
    def tap_by_cssselector(obj, extent, scenario):
        Function.tap_element('CSSSELECTOR', obj, extent, scenario) 
    #Tap Element By CLASS NAME
    @staticmethod
    def tap_by_classname(obj, extent, scenario):
        Function.tap_element('CLASSNAME', obj, extent, scenario) 
    #Tap Element By TAG NAME
    @staticmethod
    def tap_by_tagname(obj, extent, scenario):
        Function.tap_element('TAGNAME', obj, extent, scenario)
    #Check Element ID Present
    @staticmethod
    def is_element_id_present(obj):
        result = Function.is_element_is_present('ID', obj)
        return result
    #Check Element NAME Present
    @staticmethod
    def is_element_name_present(obj):
        result = Function.is_element_is_present('NAME', obj)
        return result
    #Check Element XPATH Present
    @staticmethod
    def is_element_xpath_present(obj):
        result = Function.is_element_is_present('XPATH', obj)
        return result
    #Check Element CSSSELECTOR Present
    @staticmethod
    def is_element_cssselector_present(obj):
        result = Function.is_element_is_present('CSSSELECTOR', obj)
        return result
    #Check Element CLASSNAME Present
    @staticmethod
    def is_element_classname_present(obj):
        result = Function.is_element_is_present('CLASSNAME', obj)
        return result
    #Check Element TAGNAME Present
    @staticmethod
    def is_element_tagname_present(obj):
        result = Function.is_element_is_present('TAGNAME', obj)
        return result
    #Waiting ID Element
    @staticmethod
    def wait_element_id(expect, unexpect, extent, scenario):
        Function.wait_element('ID', expect, unexpect, extent, scenario)        
    #Waiting NAME Element
    @staticmethod
    def wait_element_name(expect, unexpect, extent, scenario):
        Function.wait_element('NAME', expect, unexpect, extent, scenario)  
    #Waiting XPATH Element
    @staticmethod
    def wait_element_xpath(expect, unexpect, extent, scenario):
        Function.wait_element('XPATH', expect, unexpect, extent, scenario)  
    #Waiting CSS SELECTOR Element
    @staticmethod
    def wait_element_cssselector(expect, unexpect, extent, scenario):
        Function.wait_element('CSSSELECTOR', expect, unexpect, extent, scenario)  
    #Waiting CLASS NAME Element
    @staticmethod
    def wait_element_classname(expect, unexpect, extent, scenario):
        Function.wait_element('CLASSNAME', expect, unexpect, extent, scenario)  
    #Waiting TAG NAME Element
    @staticmethod
    def wait_element_tagname(expect, unexpect, extent, scenario):
        Function.wait_element('TAGNAME', expect, unexpect, extent, scenario)
    #Send Text To ID Element
    @staticmethod
    def send_text_id(obj, text, extent, scenario):
        Function.write_text('ID', obj, text, extent, scenario)
    #Send Text To NAME Element
    @staticmethod
    def send_text_name(obj, text, extent, scenario):
        Function.write_text('NAME', obj, text, extent, scenario)
    #Send Text To XPATH Element
    @staticmethod
    def send_text_xpath(obj, text, extent, scenario):
        Function.write_text('XPATH', obj, text, extent, scenario)
    #Send Text To CSS SELECTOR Element
    @staticmethod
    def send_text_cssselector(obj, text, extent, scenario):
        Function.write_text('CSSSELECTOR', obj, text, extent, scenario)
    #Send Text To CLASS NAME Element
    @staticmethod
    def send_text_classname(obj, text, extent, scenario):
        Function.write_text('CLASSNAME', obj, text, extent, scenario)
    #Send Text To TAG NAME Element
    @staticmethod
    def send_text_tagname(obj, text, extent, scenario):
        Function.write_text('TAGNAME', obj, text, extent, scenario)
    #Clear Textfield ID
    @staticmethod
    def clear_text_id(obj, extent, scenario):
        Function.clear_textfield('ID', obj, extent, scenario)
    #Clear Textfield NAME
    @staticmethod
    def clear_text_name(obj, extent, scenario):
        Function.clear_textfield('NAME', obj, extent, scenario)
    #Clear Textfield XPATH
    @staticmethod
    def clear_text_xpath(obj, extent, scenario):
        Function.clear_textfield('XPATH', obj, extent, scenario)
    #Clear Textfield CSS SELECTOR
    @staticmethod
    def clear_text_cssselector(obj, extent, scenario):
        Function.clear_textfield('CSSSELECTOR', obj, extent, scenario)
    #Clear Textfield CLASS NAME
    @staticmethod
    def clear_text_classname(obj, extent, scenario):
        Function.clear_textfield('CLASSNAME', obj, extent, scenario)
    #Clear Textfield TAG NAME
    @staticmethod
    def clear_text_tagname(obj, extent, scenario):
        Function.clear_textfield('TAGNAME', obj, extent, scenario)
    #Wait Element ID Clickable
    @staticmethod
    def wait_clickable_id(seconds, obj, extent, scenario):
        Function.wait_ele_clickable(By.ID, seconds, obj, extent, scenario)    
    #Wait Element NAME Clickable
    @staticmethod
    def wait_clickable_name(seconds, obj, extent, scenario):
        Function.wait_ele_clickable(By.NAME, seconds, obj, extent, scenario)  
    #Wait Element XPATH Clickable
    @staticmethod
    def wait_clickable_xpath(seconds, obj, extent, scenario):
        Function.wait_ele_clickable(By.XPATH, seconds, obj, extent, scenario)  
    #Wait Element CSS SELECTOR Clickable
    @staticmethod
    def wait_clickable_cssselector(seconds, obj, extent, scenario):
        Function.wait_ele_clickable(By.CSS_SELECTOR, seconds, obj, extent, scenario) 
    #Wait Element CLASS NAME Clickable
    @staticmethod
    def wait_clickable_classname(seconds, obj, extent, scenario):
        Function.wait_ele_clickable(By.CLASS_NAME, seconds, obj, extent, scenario) 
    #Wait Element TAG NAME Clickable
    @staticmethod
    def wait_clickable_tagname(seconds, obj, extent, scenario):
        Function.wait_ele_clickable(By.TAG_NAME, seconds, obj, extent, scenario)
    #scroll to ID element
    @staticmethod
    def scroll_to_element_id(obj, extent, scenario):
        Function.scroll_to_element('ID', obj, extent, scenario)
    #scroll to NAME element
    @staticmethod
    def scroll_to_element_name(obj, extent, scenario):
        Function.scroll_to_element('NAME', obj, extent, scenario)
    #scroll to XPATH element
    @staticmethod
    def scroll_to_element_xpath(obj, extent, scenario):
        Function.scroll_to_element('XPATH', obj, extent, scenario)
    #scroll to CSS SELECTOR element
    @staticmethod
    def scroll_to_element_cssselector(obj, extent, scenario):
        Function.scroll_to_element('CSSSELECTOR', obj, extent, scenario)
    #scroll to CLASS NAME element
    @staticmethod
    def scroll_to_element_classname(obj, extent, scenario):
        Function.scroll_to_element('CLASSNAME', obj, extent, scenario)
    #scroll to TAG NAME element
    @staticmethod 
    def scroll_to_element_tagname(obj, extent, scenario):
        Function.scroll_to_element('TAGNAME', obj, extent, scenario)
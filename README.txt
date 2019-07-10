"""THIS IS README FILE"""
"""""""""""""""""""""""""
"""PLEASE FORGIVE ME IF IT STILL HAS SO MANY MESSY CODE OR UNUSED CODE INSIDE SCRIPT"""
"""IF NOT CLEAR YOU CAN SEE EXAMPLE TESTCASE ON TESTCASE FOLDER, JUST CHANGE FACEBOOK EMAIL & PASSWORD IN object_repository in PUBLIC_FUNCTION folder,
then run TEST_SUITE_ALL.py file"""
Using this combine script, you can easily generate Extent Report using Python. All basic common function is built-in with extent test steps, so you don't
need to write so many function anymore.You can create test case inside TEST CASE folder, each test case better in different Folder. Below are the list that 
you can use instantly :

You can change executing from headless to non headless by changing value in configuration.py and also change report name. 

obj    = Element locator
extent = Array that contains extent test & log status
scenario = Steps that will write to extent report
expect = Element that you expect to be appear
unexpect = Element that not expected to appear and will fail testcase

---TAP / CLICK ACTION---
tap_by_id(obj, extent, scenario):
tap_by_name(obj, extent, scenario):
tap_by_xpath(obj, extent, scenario):
tap_by_cssselector(obj, extent, scenario):
tap_by_classname(obj, extent, scenario):
tap_by_tagname(obj, extent, scenario):
 
---CHECKING ELEMENT, RETURN OF THIS FUNCTION IS BOOLEAN---
is_element_id_present(obj):
is_element_name_present(obj):
is_element_xpath_present(obj):
is_element_cssselector_present(obj):
is_element_classname_present(obj):
is_element_tagname_present(obj):
     
---WAITING ELEMENT TO BE APPEAR---
wait_element_id(expect, unexpect, extent, scenario):
wait_element_name(expect, unexpect, extent, scenario):
wait_element_xpath(expect, unexpect, extent, scenario):
wait_element_cssselector(expect, unexpect, extent, scenario):
wait_element_classname(expect, unexpect, extent, scenario):
wait_element_tagname(expect, unexpect, extent, scenario):

---WRITE/SEND TEXT INTO TEXT FIELD---
send_text_id(obj, text, extent, scenario):
send_text_name(obj, text, extent, scenario):
send_text_xpath(obj, text, extent, scenario):
send_text_cssselector(obj, text, extent, scenario):
send_text_classname(obj, text, extent, scenario):
send_text_tagname(obj, text, extent, scenario):

---CLEAR TEXT FROM TEXT FIELD---
clear_text_id(obj, extent, scenario):
clear_text_name(obj, extent, scenario):
clear_text_xpath(obj, extent, scenario):
clear_text_cssselector(obj, extent, scenario):
clear_text_classname(obj, extent, scenario):
clear_text_tagname(obj, extent, scenario):

---WAIT ELEMENT TO BE CLICKABLE---
wait_clickable_id(seconds, obj, extent, scenario):
wait_clickable_name(seconds, obj, extent, scenario):
wait_clickable_xpath(seconds, obj, extent, scenario):
wait_clickable_cssselector(seconds, obj, extent, scenario):
wait_clickable_classname(seconds, obj, extent, scenario):
wait_clickable_tagname(seconds, obj, extent, scenario):

---SCROLLING ELEMENT---    
scroll_to_element_id(obj, extent, scenario):
scroll_to_element_name(obj, extent, scenario):
scroll_to_element_xpath(obj, extent, scenario):
scroll_to_element_cssselector(obj, extent, scenario):
scroll_to_element_classname(obj, extent, scenario):
scroll_to_element_tagname(obj, extent, scenario):
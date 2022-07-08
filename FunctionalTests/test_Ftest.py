from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

class PageTest(LiveServerTestCase):
   def setUp(self):
      self.browser = webdriver.Firefox()

   # def tearDown(self):
   #    self.browser.quit()
      
#    def test_start_list_and_retrieve_it(self):
#       self.browser.get(self.live_server_url)
#       self.assertIn('Thevaxxwiz', self.browser.title)
#       headerText = self.browser.find_element_by_tag_name('h1').text
#       self.assertIn('The Vaxx Wiz', headerText)

#       inpTitle = self.browser.find_element_by_id('title')
#       inpTitle.send_keys('Ms.')
#       time.sleep(0.5)

#       inpSurName = self.browser.find_element_by_id('surname')
#       inpSurName.send_keys('Nasam')
#       time.sleep(0.5)

#       inpFirstname = self.browser.find_element_by_id('firstname')
#       inpFirstname.send_keys('Cecilia')
#       time.sleep(0.5)

#       inpEmail = self.browser.find_element_by_id('email')
#       inpEmail.send_keys('samantha@gmail.com')
#       time.sleep(0.5)

#       inpMobile = self.browser.find_element_by_id('phone')
#       inpMobile.send_keys('6394637542231')
#       # time.sleep(1)

#       inpRadio = self.browser.find_element_by_id('mail_type')
#       inpRadio.click()
#       time.sleep(0.5)

#       inpMessage = self.browser.find_element_by_id('messagetxt')
#       inpMessage.send_keys('Sputnik is not effective.')
#       time.sleep(0.5)


#       btnConfirm = self.browser.find_element_by_id('btnConfirm')
#       self.assertEqual(inpSurName.get_attribute('placeholder'),'(Required)')
#       self.assertEqual(inpFirstname.get_attribute('placeholder'),'(Optional)')
#       self.assertEqual(inpEmail.get_attribute('placeholder'),'juan@gmail.com')
#       self.assertEqual(inpMobile.get_attribute('placeholder'),'(Required)')
#       self.assertEqual(inpMessage.get_attribute('placeholder'),'Type message here')


#       btnConfirm.click()
#       time.sleep(0.5)

# #second
#       inpTitle = self.browser.find_element_by_id('title')
#       inpTitle.send_keys('Mrs.')
#       time.sleep(0.5)

#       inpSurName = self.browser.find_element_by_id('surname')
#       inpSurName.send_keys('Gadaingan')
#       time.sleep(0.5)

#       inpFirstname = self.browser.find_element_by_id('firstname')
#       inpFirstname.send_keys('Cecilia')
#       time.sleep(0.5)

#       inpEmail = self.browser.find_element_by_id('email')
#       inpEmail.send_keys('bryce@gmail.com')
#       time.sleep(0.5)

#       inpMobile = self.browser.find_element_by_id('phone')
#       inpMobile.send_keys('6394637542231')
#       # time.sleep(1)

#       inpRadio = self.browser.find_element_by_id('mail_type')
#       inpRadio.click()
#       time.sleep(0.5)

#       inpMessage = self.browser.find_element_by_id('messagetxt')
#       inpMessage.send_keys('Sputnik is not effective.')
#       time.sleep(0.5)


#       btnConfirm = self.browser.find_element_by_id('btnConfirm')
#       self.assertEqual(inpSurName.get_attribute('placeholder'),'(Required)')
#       self.assertEqual(inpFirstname.get_attribute('placeholder'),'(Optional)')
#       self.assertEqual(inpEmail.get_attribute('placeholder'),'juan@gmail.com')
#       self.assertEqual(inpMobile.get_attribute('placeholder'),'(Required)')
#       self.assertEqual(inpMessage.get_attribute('placeholder'),'Type message here')


#       btnConfirm.click()
#       time.sleep(0.5)


#       table = self.browser.find_element_by_id('table')
#       rows = table.find_elements_by_tag_name('tr')
      
#       self.assertIn('1: Ms., Nasam, Cecilia, samantha@gmail.com, 6394637542231', 
#          [row.text for row in rows])
#       time.sleep(0.5)

if __name__ == '__main__':
   unittest.main(warnings='ignore')
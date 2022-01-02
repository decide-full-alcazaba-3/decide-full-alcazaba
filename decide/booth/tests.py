from django.test import TestCase

# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#Test que comprueba la vista de una pregunta si/no en el booth (Selenium)

class TestBOOTHVISTASINO():
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bOOTHVISTASINO(self):
    self.driver.get("http://localhost:8081/booth/5/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("alcazaba")
    self.driver.find_element(By.ID, "password").send_keys("alcazaba")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    time.sleep(1) #Debido que el test carga más rápido que la propia página debido al React.
    self.driver.find_element(By.ID, "q2").click()
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.LINK_TEXT, "logout").click()
    
#Test que comprueba la vista de una pregunta con varias opciones en el booth (Selenium)

class TestBOOTHVISTAOPTIONS():
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bOOTHVISTAOPTIONS(self):
    self.driver.get("http://localhost:8081/booth/6/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("alcazaba")
    self.driver.find_element(By.ID, "password").send_keys("alcazaba")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    time.sleep(1) #Debido que el test carga más rápido que la propia página debido al React.
    self.driver.find_element(By.ID, "q4").click()
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.LINK_TEXT, "logout").click()
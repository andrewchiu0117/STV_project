from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import xpath
import time

class Device:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'HTC_X9u'
        desired_caps['appPackage'] = 'de.php_tech.piggybudget'
        desired_caps['appActivity'] = 'de.php_tech.piggybudget.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 20)
    def close(self):
        self.driver.quit()

    def click_expense(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.expense_xpath))
        expense_btn = self.wait.until((vision),"wait error, no expense_btn")
        expense_btn.click()

    def click_income(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.income_xpath))
        income_btn = self.wait.until((vision),"wait error, no income_btn")
        income_btn.click()

    def total_budget_text(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.total_budget_xpath))
        total_budget = self.wait.until((vision),"wait error, no total_budget")
        return total_budget

    def today_budget_text(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.today_budget_xpath))
        today_budget = self.wait.until((vision),"wait error, no today_budget")
        return today_budget

    def btn(self):
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
        el2.click()
    
    def click_icon1(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_1))
        Icon_1 = self.wait.until((vision),"wait error, no Icon_1")
        # Icon_1 = self.driver.find_element_by_xpath(xpath.Icon_1)
        Icon_1.click()

    def click_icon2(self):
        # vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_2))
        # Icon_2 = self.wait.until((vision),"wait error, no Icon_2")
        Icon_2 = self.driver.find_element_by_xpath(xpath.Icon_2)
        Icon_2.click()

    def click_icon3(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_3))
        Icon_3 = self.wait.until((vision),"wait error, no Icon_3")
        Icon_3.click()

    def click_icon4(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_4))
        Icon_4 = self.wait.until((vision),"wait error, no Icon_4")
        Icon_4.click()

    def click_icon5(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_5))
        Icon_5 = self.wait.until((vision),"wait error, no Icon_5")
        Icon_5.click()

    def click_icon6(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_6))
        Icon_6 = self.wait.until((vision),"wait error, no Icon_6")
        Icon_6.click()

    def click_icon7(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_7))
        Icon_7 = self.wait.until((vision),"wait error, no Icon_7")
        Icon_7.click()

    def click_icon8(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_8))
        Icon_8 = self.wait.until((vision),"wait error, no Icon_8")
        Icon_8.click()

    def click_icon9(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_9))
        Icon_9 = self.wait.until((vision),"wait error, no Icon_9")
        Icon_9.click()

    def click_icon10(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_10))
        Icon_10 = self.wait.until((vision),"wait error, no Icon_10")
        Icon_10.click()

    def click_icon11(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_11))
        Icon_11 = self.wait.until((vision),"wait error, no Icon_11")
        Icon_11.click()

    def click_icon12(self):
        vision=EC.visibility_of_element_located((By.XPATH,xpath.Icon_12))
        Icon_12 = self.wait.until((vision),"wait error, no Icon_12")
        Icon_12.click()
    
    def enter_numbers(self,txt):
        el3 = self.driver.find_element_by_xpath(xpath.input_number)
        el3.send_keys(txt)
    
    def submit(self):
        self.driver.press_keycode(66)

    def restart(self):
        # self.driver.close_app()
        self.driver.reset()
        time.sleep(5)
        self.driver.launch_app()
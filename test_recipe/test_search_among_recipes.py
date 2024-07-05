import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Test_Search_Among_Recipes:
    

    def setup_method(self): 
        
        self.driver = webdriver . Chrome ()
        self.driver.get("https://www.nefisyemektarifleri.com/")
        self.driver.maximize_window()


    def tearDown_method(self):
        self.driver.quit()

    @pytest.mark.run(order=6)
    def test_Filter_From_The_Search_Field(self):
        
        searcharea= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.ID, "top-search-input")))
        searcharea.click()
        searcharea.send_keys('karnıyarık')
        searchbutton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/section[1]/div/div[2]/div[2]/form/button")))
        searchbutton.click()
        truefilter= WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//strong[text()='karnıyarık']")))
        assert truefilter.text == "karnıyarık"
    
    
    @pytest.mark.run(order=7)    
    def test_Filter_From_The_Search_Button(self):
        searchbutton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/section[1]/div/div[2]/div[2]/form/button")))
        searchbutton.click()
        sleep(2)
        self.driver.execute_script("window.scrollBy(0, 500);")
        sleep(2)
        allrecipes=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//a[text()='Tüm Tarifler']")))
        allrecipes.click()
        sleep(2)
        searchword=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located ((By.XPATH, "//input[@id='widget-search-input']")))
        ActionChains(self.driver).move_to_element(searchword).click().send_keys('karnıyarık').perform()
        sleep(3)      
        to_do_search=WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//button[text()='Arama Yap']")))
        to_do_search.click()
        sleep(10)
        truefilter= WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"//strong[text()='karnıyarık']")))
        assert "karnıyarık" in truefilter.text  
    
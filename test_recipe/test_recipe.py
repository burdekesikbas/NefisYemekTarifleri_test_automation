
import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains




class Test_Recipe:
    

    def setup_method(self): 
        
        self.driver = webdriver . Chrome ()
        self.driver.get("https://www.nefisyemektarifleri.com/")
        self.driver.maximize_window()

    

    def tearDown_method(self):
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_Category_From_Recipe(self):
        
        recipes= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//li[@class='mega-link']/a/span[text() ='TARİFLER']")))
        recipes.click()
        collation_categories= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "//span[@class='category-title' and text()='Aperatifler ']")))
        collation_categories.click()
        current_url = self.driver.current_url
        assert current_url == "https://www.nefisyemektarifleri.com/kategori/tarifler/aperatifler-tarifler/"
        
        
    @pytest.mark.run(order=2)   
    def test_Category_From_Recipe3(self):
        recipes= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//li[@class='mega-link']/a/span[text() ='TARİFLER']")))
        move=ActionChains(self.driver)
        move.move_to_element(recipes)
        move.perform()
        allcategories = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//a[@class='buttons btn-red show-all-categories']")))
        allcategories.click()
        collation_categories= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "(//div[@class='col-sm-3 col-xs-12'])[4]")))
        sleep(5)
        collation_categories.click()
        collation_page=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "//span[text()='Popüler Aperatifler']")))
        assert collation_page.text=="Popüler Aperatifler"
        current_url = self.driver.current_url
        assert current_url == "https://www.nefisyemektarifleri.com/kategori/tarifler/aperatifler-tarifler/"
        
        
        
    @pytest.mark.run(order=3)    
    def test_Category_From_Recipe4(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        recipes2= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//li/a[@title='Tarif Kategorileri' and @class='tarifler ']")))
        recipes2.click()
        collation_categories= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "//span[@class='category-title' and text()='Aperatifler ']")))
        collation_categories.click()
        current_url = self.driver.current_url
        assert current_url == "https://www.nefisyemektarifleri.com/kategori/tarifler/aperatifler-tarifler/"
        
    
        
       
        
        
        

     
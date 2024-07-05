import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Test_Recipe_Details_Control:
    

    def setup_method(self): 
        
        self.driver = webdriver . Chrome ()
        self.driver.get("https://www.nefisyemektarifleri.com/")
        self.driver.maximize_window()
        
    

    def tearDown_method(self):
        self.driver.quit()

    @pytest.mark.run(order=8)
    def test_Recipe_Details(self):
        
        recipes= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//li[@class='mega-link']/a/span[text() ='TARİFLER']")))
        recipes.click()
        legumes_categories= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//img[@alt='Bakliyat Yemekleri']")))
        legumes_categories.click()
        stuffedmeatballs_recipe=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//figure/a[@title='İçli Köfte Tarifi']")))
        stuffedmeatballs_recipe.click()
        materials=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//h2[text()='İçli Köfte Tarifi İçin Malzemeler']")))
        assert materials.text == "İçli Köfte Tarifi İçin Malzemeler"
        recipedetail=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//div[@class='recipe-preparation content-articles']")))
        assert "İçli Köfte Tarifi Nasıl Yapılır?" in recipedetail.text
       
        
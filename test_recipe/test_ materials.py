import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Test_Materials:
    

    def setup_method(self): 
        
        self.driver = webdriver . Chrome ()
        self.driver.get("https://www.nefisyemektarifleri.com/")
        self.driver.maximize_window()

    

    def tearDown_method(self):
        self.driver.quit()

    @pytest.mark.run(order=4)
    def test_Materials_From_The_Search_Field(self):
        
        searcharea= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.ID, "top-search-input")))
        searcharea.click()
        searcharea.send_keys('peynir')
        searcharea.send_keys(Keys.ENTER)
        filterarea= WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//div[@class='title-area drop-filters']")))
        assert filterarea.text == "Filtrele"
    
    @pytest.mark.run(order=5)    
    def test_Materials_From_The_Search_Button(self):
        
        searchbutton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/section[1]/div/div[2]/div[2]/form/button")))
        searchbutton.click()
        containing_recipe= WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//h4[text()='Tarif bu malzemeleri içersin:']")))
        assert containing_recipe.text == "Tarif bu malzemeleri içersin:"
        not_in_the_recipe =WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//h4[text()='Tarif bu malzemeleri içermesin']")))
        assert not_in_the_recipe.text=="Tarif bu malzemeleri içermesin"
        containing_recipe_area=WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//input[@class='malzeme-select select2-search__field' and @data-name='icersin']")))
        containing_recipe_area.click()
        containing_recipe_area.send_keys('peynir')
        containing_recipe_area.send_keys(Keys.ENTER)
        not_in_the_recipe_area =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//input[@class='malzeme-select select2-search__field' and @data-name='icermesin']")))
        actions=ActionChains(self.driver)
        actions.move_to_element(not_in_the_recipe_area).click().send_keys('maya').send_keys(Keys.ENTER).perform()
        to_do_search=WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//button[text()='Arama Yap']")))
        to_do_search.click()
        example_recipe =WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//a[text()='Tepsileri Dolduran Pamuk Gibi Poğaça Tarifi (Videolu)']")))
        example_recipe.click()
        self.driver.execute_script("window.scrollBy(0, 5000);")
        example_recipe_detail=WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH,"//ul[@class='recipe-materials']//li[contains(text(), 'maya')]")))
        assert "maya" not in example_recipe_detail.text, "'maya' tarif içinde bulunuyor"
        
    
        
        
        
        
        
       
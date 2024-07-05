import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Test_Favourite_Recipe:
    

    def setup_method(self): 
        
        self.driver = webdriver . Chrome ()
        self.driver.get("https://www.nefisyemektarifleri.com/")
        self.driver.maximize_window()

    

    def tearDown_method(self):
        self.driver.quit()

    @pytest.mark.run(order=11)
    def test_Without_User_Login(self):
        
        recipes= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "//li[@class='mega-link']/a/span[text() ='TARİFLER']")))
        recipes.click()
        legumes_categories= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "(//div[@class='col-sm-3 col-xs-12'])[5]")))
        legumes_categories.click()
        stuffedmeatballs_recipe=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//figure/a[@title='İçli Köfte Tarifi']")))
        stuffedmeatballs_recipe.click()
        add_book= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//a[@title='Deftere Ekle']")))
        add_book.click()
        do_login= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "(//span[text()='Giriş Yap'])[2]")))
        assert do_login.text=="Giriş Yap"
    
    @pytest.mark.run(order=12)    
    def test_With_User_Login(self):
        
        login= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//div/a[text()='Giriş Yap']")))
        login.click()
        email=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located  ((By.XPATH, "(//a/span[text()='E-posta ile Giriş Yap'])[2]")))
        email.click()
        username=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located  ((By.XPATH, "(//input[@id='modalUsername'])[2]")))
        username.click()
        username.send_keys("brdykc@hotmail.com")
        password=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located  ((By.XPATH, "(//input[@id='modalPassword'])[2]")))
        password.click()
        password.send_keys("123456"),
        login2=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located  ((By.XPATH, "(//button[@class='login-button buttons submit'])[2]")))
        action=ActionChains(self.driver)
        action.move_to_element(login2).perform()
        login2.click()
        loginmessage=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//span[@class='text'][contains(text(), 'Giriş başarılı. Yönlendiriliyorsunuz')]")))
        message_text= loginmessage.text
        sleep(2)
        assert "Giriş başarılı. Yönlendiriliyorsunuz.." in message_text
        recipes= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//li[@class='mega-link']/a/span[text() ='TARİFLER']")))
        action=ActionChains(self.driver)
        action.move_to_element(recipes).perform()
        recipes.click()
        legumes_categories= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "(//div[@class='col-sm-3 col-xs-12'])[5]")))
        legumes_categories.click()
        stuffedmeatballs_recipe=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//figure/a[@title='İçli Köfte Tarifi']")))
        stuffedmeatballs_recipe.click()
        add_book= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//a[@title='Deftere Ekle']")))
        add_book.click()
        sleep(2)
        added_message =WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//span[@class='text'][contains(text(), 'Tarif defterinize eklendi.')]")))
        added_message_text= added_message.text
        sleep(2)
        assert "Tarif defterinize eklendi." in added_message_text
        my_recipe_book=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "(//a[@title='Tarif Defterim'])[1]")))
        my_recipe_book.click()
        recipe_book= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//div[@class='info']")))
        recipe_book.click()
        stuffedmeatballs_recipe2=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "(//a[@title='İçli Köfte Tarifi'])[2]")))
        assert stuffedmeatballs_recipe2.text=="İçli Köfte Tarifi"
        
       
        
       
        
        
        
        
        
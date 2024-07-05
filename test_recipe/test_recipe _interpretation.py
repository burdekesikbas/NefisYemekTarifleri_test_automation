import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Test_Interpretation:
    

    def setup_method(self): 
        
        self.driver = webdriver . Chrome ()
        self.driver.get("https://www.nefisyemektarifleri.com/")
        sleep(3)
        self.driver.maximize_window()
        sleep(3)

    

    def tearDown_method(self):
        self.driver.quit()

    @pytest.mark.run(order=9)
    def test_Without_User_Login(self):
        
        recipes= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "//li[@class='mega-link']/a/span[text() ='TARİFLER']")))
        recipes.click()
        legumes_categories= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "(//div[@class='col-sm-3 col-xs-12'])[5]")))
        legumes_categories.click()
        stuffedmeatballs_recipe=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//figure/a[@title='İçli Köfte Tarifi']")))
        stuffedmeatballs_recipe.click()
        comments= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//span[text()='Yorumlar']")))
        comments.click()
        commentarea=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located ((By.XPATH, "//textarea[@name='comment']")))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",commentarea)
        sleep(2)
        placeholder_text = commentarea.get_attribute("placeholder")
        assert "Yorum yapabilmek için giriş yapmanız gerekmektedir." in placeholder_text     
    
    @pytest.mark.run(order=10)     
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
        comments= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//span[text()='Yorumlar']")))
        comments.click()
        self.driver.execute_script("window.scrollBy(0, 5000);")
        commentarea=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//textarea[@name='comment']")))
        self.driver.execute_script("arguments[0].scrollIntoView(false);",commentarea)
        sleep(2)
        placeholder_text = commentarea.get_attribute("placeholder")
        assert "Bu tarif hakkında ne düşünüyorsun? Yorumunu buraya yazabilirsin." in placeholder_text 
        commentarea=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//textarea[@name='comment']")))
        commentarea.click()
        commentarea.send_keys("Elinize sağlık")
        do_comment =WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//button[text()='Yorumu Gönder']")))
        do_comment.click()
        new_comments=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//span[text()='Yeni Gelen Yorumlar']")))
        assert new_comments.text=="Yeni Gelen Yorumlar"
        
         
        
        
        
        
        
        
        
        
        
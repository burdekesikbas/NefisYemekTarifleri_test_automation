import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Test_Edit_Delete:
    

    def setup_method(self): 
        
        self.driver = webdriver . Chrome ()
        self.driver.get("https://www.nefisyemektarifleri.com/")
        self.driver.maximize_window()

    

    def tearDown_method(self):
        self.driver.quit()
        
    @pytest.mark.run(order=13)
    def test_Comment_Edit_Delete(self):
        
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
        sleep(10)
        self.driver.refresh()
        
        profil=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "//a[@class='profile-link']")))
        action = ActionChains(self.driver)
        action.context_click(profil).perform()
        
        done_comment=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "(//a[text()='Yaptığım Yorumlar'])[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", done_comment)
        done_comment.click()
        delete=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//span[@class='text'][contains(text(), 'Sil')]")))
        delete.click()
        message_box=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "(//p[@class='content-texts'][contains(text(), 'Yorumu silmek istediğinizden emin misiniz?')])[2]")))
        assert message_box.text=="Yorumu silmek istediğinizden emin misiniz?"
        approve=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "(//a[text()='Onayla'])[3]")))
        approve.click()
        delete_message=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//span[@class='text'][contains(text(), 'Yorum başarılı bir şekilde silindi')]")))
        assert delete_message.text=="Yorum başarılı bir şekilde silindi"
        
    @pytest.mark.run(order=14)
    def test_Favourite_Recipe_Edit_Delete(self):  
        
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
        profil=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located ((By.XPATH, "//a[@class='profile-link']")))
        action = ActionChains(self.driver)
        action.context_click(profil).perform()
        my_recipe_book=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "(//a[@title='Tarif Defterim'])[3]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", my_recipe_book)
        my_recipe_book.click()
        sleep(2)
        recipe_book= WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//div[@class='info']")))
        recipe_book.click()
        delete_icon=WebDriverWait(self.driver,3).until(ec.visibility_of_element_located ((By.XPATH, "//a[@data-post_id='122409']")))
        delete_icon.click()
        delete_message=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located ((By.XPATH, "//span[@class='text'][contains(text(), 'Deftereden başarılı bir şekilde çıkarıldı')]")))
        assert delete_message.text=="Defterden başarılı bir şekilde çıkarıldı"
        
        
        
    
        
    
"""AMAÇ:

Derste gösterilen konuların pekiştirilmesi.

ÖDEV TANIMI:

Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.

Test Caseler;

Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())

class Sauce:
    def kullanıcısız(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        hataMesajı = driver.find_element(By.XPATH , "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        hataSonucu = hataMesajı.text == "Epic sadface: Username is required"
        print(f"Test Sonucu-1: {hataMesajı}")

    def sifreHata(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullanıcıGiris = driver.find_element(By.ID , "user-name")
        sifreGiris = driver.find_element(By.ID , "password")
        kullanıcıGiris.send_keys("Test")
        sifreGiris.send_keys()
        sleep(5)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        hataMesajı = driver.find_element(By.XPATH , "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        hataMesajı = hataMesajı.text == "Epic sadface: Password is required"
        print(f"Test Sonucu-2: {hataMesajı}")

    def kullanıcıHata(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullanıcıGiris = driver.find_element(By.ID , "user-name")
        sifreGiris = driver.find_element(By.ID , "password")
        kullanıcıGiris.send_keys("locked_out_user")
        sifreGiris.send_keys("secret_sauce")
        sleep(5)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        hataMesajı = driver.find_element(By.XPATH , "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        hataMesajı = hataMesajı.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu-3: {hataMesajı}")

    def X_ikonu(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullanıcıGiris = driver.find_element(By.ID , "user-name")
        sifreGiris = driver.find_element(By.ID , "password")
        kullanıcıGiris.send_keys()
        sifreGiris.send_keys()
        sleep(5)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        sleep(5)
        iconFind = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path")
        iconFind.click()
        
    def giris(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullanıcıGiris = driver.find_element(By.ID , "user-name")
        sifreGiris = driver.find_element(By.ID , "password")
        kullanıcıGiris.send_keys("standard_user")
        sifreGiris.send_keys("secret_sauce")
        sleep(5)
        loginBtn = driver.find_element(By.ID , "login-button")
        loginBtn.click()
        sleep(5)
        product = driver.find_elements(By.CLASS_NAME, "inventory_item")
        if (len(product) == 6):
            print(f"Test Başarılı ...  Anlık Ürün Sayısı: {len(product)}")
        else:
            print("Test Başarısız ...  6'dan fazla ürün mevcut.")
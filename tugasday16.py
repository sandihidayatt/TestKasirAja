import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self): # Test case Success Login
        # steps
        driver = self.driver #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("serbu@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("12345678") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="login"]').click() # Click login
        time.sleep(3)

        # validasi
        get_url = str(driver.current_url)
        print(get_url)
        self.assertIn('https://kasirdemo.belajarqa.com/dashboard', get_url)

    def test_login_with_invalid_email_password(self): # Test case login with invalid email and password
        # steps
        driver = self.driver #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("bukanserbu@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("ini12345") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="login"]').click() # Click login
        time.sleep(3)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"chakra-alert").text
        # print(response_data)
        self.assertIn('Kredensial yang Anda berikan salah', response_data)
    
    
    def test_login_with_invalid_password(self): # Test case login with invalid password
        # steps
        driver = self.driver #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("serbu@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("12345") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="login"]').click() # Click login
        time.sleep(3)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"chakra-alert").text
        # print(response_data)
        self.assertIn('Kredensial yang Anda berikan salah', response_data)

    def test_login_with_empty_email(self): # Test case login with empty email
        # steps
        driver = self.driver #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("12345678") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="login"]').click() # Click login
        time.sleep(3)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"chakra-alert").text
        # print(response_data)
        self.assertIn('"email" is not allowed to be empty', response_data)

    def test_login_with_empty_password(self): # Test case login with empty password
        # steps
        driver = self.driver #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("subur@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="login"]').click() # Click login
        time.sleep(3)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"chakra-alert").text
        # print(response_data)
        self.assertIn('"password" is not allowed to be empty', response_data)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


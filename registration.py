import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_success_registration(self): # Test case Success Registration
        # steps
        driver = self.driver #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,"ingin mencoba, daftar ?").click()
        time.sleep(1)
        driver.find_element(By.ID,"name").send_keys("Toko Serbu") # isi nama toko
        time.sleep(1)
        driver.find_element(By.ID,"email").send_keys("serbu@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("12345678") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="daftar"]').click() # klik daftar
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID,"chakra-toast-manager-top-right").text
        # print(response_data) # Mengecek isi respon_data
        self.assertIn('Toko berhasil didaftarkan\nanda dapat menggunakan login sekarang', response_data)
    
    def test_registration_with_empty_nama_toko(self): # Test case registration with empty nama toko
        # steps
        driver = self.driver #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,"ingin mencoba, daftar ?").click()
        time.sleep(1)
        driver.find_element(By.ID,"name").send_keys("") # isi nama toko
        time.sleep(1)
        driver.find_element(By.ID,"email").send_keys("serbu@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("12345678") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="daftar"]').click() # klik daftar
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"chakra-alert").text
        # print(response_data)
        self.assertIn('"name" is not allowed to be empty', response_data)
    
    def test_registration_with_empty_email(self): # Test case registration with empty email
        # steps
        driver = self.driver #buka web browser
        driver.get("https://kasirdemo.belajarqa.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,"ingin mencoba, daftar ?").click()
        time.sleep(1)
        driver.find_element(By.ID,"name").send_keys("Toko Serbu") # isi nama toko
        time.sleep(1)
        driver.find_element(By.ID,"email").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("12345678") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="daftar"]').click() # klik daftar
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"chakra-alert").text
        # print(response_data)
        self.assertIn('"email" is not allowed to be empty', response_data)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
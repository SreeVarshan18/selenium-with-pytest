import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def setUp():
    global driver, prod
    prod = input("Enter a Product to be searched: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_serachproducts(setUp):
    driver.get("https://www.flipkart.com/")
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_class_name("_3704LK").send_keys(prod)
    driver.find_element_by_class_name("L0Z3Pu").click()
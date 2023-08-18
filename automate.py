from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from dotenv import load_dotenv
from os import getenv


class Automate:
    def __init__(self, delay):
        # Time delay for loading(in seconds)
        self.delay = delay


class Driver:
    def __init__(self, url):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = url
        self.driver.get(self.url)
        time.sleep(3)

    def form_fill(self, name, to_fill):
        form = self.driver.find_element(By.NAME, name)
        form.clear()
        form.send_keys(to_fill)
# Testing is done here

urle = "https://www.instagram.com/"
namee = "username"
to_fille = "hello"
instagram = Driver(urle)
instagram.form_fill(namee, to_fille)


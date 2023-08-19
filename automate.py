from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Driver:
    def __init__(self, url, load_time):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.url = url
        self.driver.get(self.url)
        self.load_time = load_time
        time.sleep(self.load_time)

    def form_fill(self, name, to_fill):
        form = self.driver.find_element(By.NAME, name)
        form.clear()
        form.send_keys(to_fill)

    def select_dropdown(self, name, value):
        drop = Select(self.driver.find_element(By.NAME, name))
        drop.select_by_value(value)

class Instagram(Driver):
    pass

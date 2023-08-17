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
    def __init__(self):
        self.driver = webdriver.Chrome()
class Form(Driver):
    def __init__(self, name, to_fill):
        super().__init__()
        self.name = name
        self.to_fill = to_fill

    def fill(self):
        self.driver.


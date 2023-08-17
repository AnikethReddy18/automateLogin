from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from dotenv import load_dotenv
from os import getenv





def automate():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    print("start")
    app_num_e = driver.find_element(by=By.ID, value="getApplno")
    app_num_e.send_keys(app_num)
    d_bd = Select(driver.find_element(By.ID, "bdd"))
    d_bd.select_by_value("18")


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
load_dotenv(".env")
app_num = getenv("APPLICATION_NUMBER")
url = "https://vtop1.vitap.ac.in/studentprofile/"
automate()

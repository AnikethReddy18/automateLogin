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
    time.sleep(2)
    print("start")

    app_num_e = driver.find_element(by=By.ID, value="getApplno")
    app_num_e.send_keys(app_num)

    d_bd = Select(driver.find_element(By.ID, "bdd"))
    d_bd.select_by_value(d_bdd)

    m_bd = Select(driver.find_element(By.ID, "bmm"))
    m_bd.select_by_value(m_bdd)

    y_bd = Select(driver.find_element(By.ID, "byyyy"))
    y_bd.select_by_value(y_bdd)

    check = input("Are you done?")

    if check == "done":
        nationality_e = Select(driver.find_element(By.ID, "nationality"))
        nationality_e.select_by_value(nationality)

        native_state_e = Select(driver.find_element(By.ID, "nativeState"))
        native_state_e.select_by_value(native_state)

        mother_tongue_e = Select(driver.find_element(By.ID, "motherTongue"))
        mother_tongue_e.select_by_value(mother_tongue)

        blood_group_e = Select(driver.find_element(By.ID, "bloodGroup"))
        blood_group_e.select_by_value(blood_group)

        religion_e = Select(driver.find_element(By.ID, "religion"))
        religion_e.select_by_value(religion)

        community_e = Select(driver.find_element(By.ID, "community"))
        community_e.select_by_value(community)

        ews_e = Select(driver.find_element(By.ID, "ews"))
        ews_e.select_by_value(ews)

        phyChallenge_e = Select(driver.find_element(By.ID, "phyChallenge"))
        phyChallenge_e.select_by_value(phyChallenge)

        hostel_e = Select(driver.find_element(By.ID, "hostel"))
        hostel_e.select_by_value(hostel)

        aadharno_e = driver.find_element(By.ID, "aadharno")
        aadharno_e.send_keys(aadharno)

        currentStreetName_e = driver.find_element(By.ID, "currentStreetName")
        currentStreetName_e.send_keys(currentStreetName)

        currentAreaName_e = driver.find_element(By.ID, "currentAreaName")
        currentAreaName_e.send_keys(currentAreaName)

        currentCountry_e = Select(driver.find_element(By.ID, "currentCountry"))
        currentCountry_e.select_by_value(currentCountry)

        currentStatename_e = Select(driver.find_element(By.ID, "currentStatename"))
        currentStatename_e.select_by_value(currentStatename)

        currentDistrict_e = Select(driver.find_element(By.ID, "currentDistrict"))
        currentDistrict_e.select_by_value(currentDistrict)

        currentPincode_e = driver.find_element(By.ID, "currentPincode")
        currentPincode_e.send_keys(currentPincode)

        currentMobileno_e = driver.find_element(By.ID, "currentMobileno")
        currentMobileno_e.send_keys(currentMobileno)

        currentEmailid_e = driver.find_element(By.ID, "currentEmailid")
        currentEmailid_e.send_keys(currentEmailid)


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

load_dotenv(".env")
app_num = getenv("APPLICATION_NUMBER")
d_bdd = getenv("B_BD")
m_bdd = getenv("M_BD")
y_bdd = getenv("Y_BD")
nationality = getenv("NATIONALITY")
native_state = getenv("NATIVE_STATE")
mother_tongue = getenv("MOTHER_TONGUE")
blood_group = getenv("BLOOD_GROUP")
religion = getenv("RELIGION")
community = getenv("COMMUNITY")
ews = getenv("EWS")
phyChallenge = getenv("PHY_CHALLENGED")
hostel = getenv("HOSTEL")
aadharno = getenv("AADHARNO")
currentStreetName = getenv("CUR_STRT_NAME")
currentAreaName = getenv("CUR_ARA_NAME")
currentCountry = getenv("CUR_CON")
currentStatename = getenv("CUR_STATE")
currentDistrict = getenv("CUR_DIST")
currentPincode = getenv("CUR_PIN")
currentMobileno = getenv("CUR_MOBILE")
currentEmailid = getenv("CUR_EMAIL")

url = "https://vtop1.vitap.ac.in/studentprofile/"
automate()

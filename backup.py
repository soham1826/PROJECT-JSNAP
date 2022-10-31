from selenium import webdriver
import time
from random import seed
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def getRandomTime():
    randTime = randint(3, 5)
    return randTime


class InstaBot:
    def __init__(self, username, password):
        followFarm = ["ducks.ig"]
        comment_pallet = ["how cute","Cutie pie","super cute","so adorable"]

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://instagram.com")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@name=\"username\"]") \
            .send_keys(username)
        time.sleep(4)
        driver.find_element(By.XPATH, "//input[@name=\"password\"]") \
            .send_keys(password)
        time.sleep(3)
        driver.find_element(By.XPATH, '//button[@type="submit"]') \
            .click()
        # first not now

        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button") \
            .click()
        # second not now

        time.sleep(5)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]") \
            .click()

        # search

        time.sleep(10)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input") \
            .send_keys(followFarm[0])

        # click on selection
        time.sleep(7)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div[1]") \
            .click()

        #click on follow
        time.sleep(10)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")\
            .click()

        #click on first post
        time.sleep(7)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[4]/article/div[1]/div/div[1]/div[1]")\
            .click()

        #like first post
        time.sleep(7)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")\
            .click()

        #comment first post
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button")\
            .click()

        time.sleep(5)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")\
            .send_keys(comment_pallet[randint(0,(len(comment_pallet)-1))])

        time.sleep(5)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button")\
            .click()

        time.sleep(7)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button")\
            .click()

        # like second post
        time.sleep(7)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button") \
            .click()

        time.sleep(7)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div")\
            .click()
        #log out

        time.sleep(10)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span")\
            .click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]/div/div/div/div")

        driver.quit()












InstaBot("JARVIS18264", "soham@123")

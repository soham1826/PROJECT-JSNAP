import pyttsx3
import speech_recognition as sr
import datetime
from selenium import webdriver
import time

from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Hello Everyone, Welcome To JARVIS SOCIAL NETWORKING AUTOMATION PROGRAM")
    speak("I am Jarvis, Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def getRandomTime():
    randTime = randint(3, 5)
    return randTime


class InstaBot:
    def __init__(self, username, password):
        followFarm = ["dogs.lovers"]
        comment_pallet = ["how cute", "Cutie pie", "super cute", "so adorable"]

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://instagram.com")

        speak("Entering Password and Username")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@name=\"username\"]") \
            .send_keys(username)
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@name=\"password\"]") \
            .send_keys(password)
        time.sleep(2)
        driver.find_element(By.XPATH, '//button[@type="submit"]') \
            .click()
        # first not now

        time.sleep(3)
        speak("Clearing Two dialog boxes")
        driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button") \
            .click()
        # second not now

        time.sleep(3)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]") \
            .click()

        # search

        time.sleep(3)
        speak("Now searching for an account")
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input") \
            .send_keys(followFarm[randint(0, (len(followFarm) - 1))])

        # click on selection
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div") \
            .click()

        # click on follow
        time.sleep(5)
        speak("Now lets follow this account")
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button") \
            .click()

        # click on first post
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/div[2]/a[2]/div/span") \
            .click()

        time.sleep(4)
        speak("Lets open the first post and put a like and comment ")
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/div[3]/div/div/div/div[1]/div[1]") \
            .click()
        # like first post
        time.sleep(5)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button") \
            .click()

        # comment first post
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button") \
            .click()

        time.sleep(4)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea") \
            .send_keys(comment_pallet[randint(0, (len(comment_pallet) - 1))])

        time.sleep(3)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button") \
            .click()

        time.sleep(6)

        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button") \
            .click()

        time.sleep(3)
        speak("lets give a like for second post as well")
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button") \
            .click()

        time.sleep(4)

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div") \
            .click()
        # log out

        time.sleep(4)
        speak("now loging out of the instagram")
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]") \
            .click()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]/div/div/div/div")
        speak("Thank you for using J-snap")

        driver.quit()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'instagram' in query:
            speak('Automating instagram')
            InstaBot("JARVIS18264", "soham@123")

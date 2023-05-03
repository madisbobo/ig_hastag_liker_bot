from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import random, choice, randint
from datetime import datetime


# ________ Constants ________ #

TIME_CONST = 6
RAND_CONST = 10

HASTAGS = ["outdoorlife", "outdoorliving", "patio"] # TODO: Add your hastags
CHROME_DRIVER_PATH = "" # TODO: Define your path to the chrome driver
USER = "" # TODO: Your IG user name
PW = "" # TODO: Your IG password


# ________ Class ________ #

class Instabot:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # Set the user agent of the Chrome browser to simulate a specific device or browser.
        self.options.add_argument("") # TODO: Add your user agent
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument("--disable-gpu")
        # Create a new WebDriver instance with the specified options and the Chrome driver executable path.
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=self.options)

    def login(self):
        """Log into your IG account"""
        print("Log in to the account...")
        # Navigate to the Instagram login page.
        self.driver.get("https://www.instagram.com/accounts/login/")
        # Wait for a random amount of time to simulate human-like behavior.
        time.sleep(TIME_CONST + random() * RAND_CONST)
        # Find and click the "Accept cookies" button if it exists.
        cookies_btn = self.driver.find_element(By.CLASS_NAME, "_a9_0")
        cookies_btn.click()
        # Wait for a random amount of time before proceeding.
        time.sleep(TIME_CONST + random() * RAND_CONST)
        # Find the username input field and enter the provided username.
        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys(USER)
        # Find the password input field and enter the provided password.
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PW)
        # Press the Enter key to submit the form and log in.
        password.send_keys(Keys.ENTER)

        time.sleep(TIME_CONST + random() * RAND_CONST)
        print("✅ Log in completed!\n")

    def find_hashtag_posts(self, tag):
        """Based on the specified hastag, finds a page containing relevant posts"""
        print("Finding posts...")
        url = f"https://www.instagram.com/explore/tags/{tag}"
        self.driver.get(url)
        time.sleep(TIME_CONST + random() * RAND_CONST)
        # Find and click on the first post
        first_post = self.driver.find_element(By.CLASS_NAME, "_aagu")
        first_post.click()
        time.sleep(TIME_CONST + random() * RAND_CONST)
        print("✅Post finding completed!")

    def like_posts(self, nr_likes):
        """Opens the first post, likes if not liked yet and then moves on to a next post"""
        print(f"\nLiking posts in progress (0/{nr_likes})...")
        likes = 0
        while True:
            like_btn = self.driver.find_element(By.CSS_SELECTOR, "span ._abl-")
            divs = like_btn.find_elements(By.TAG_NAME, "div")
            # If like not given, do it and go to a next post
            if len(divs) == 2:
                try:
                    like_btn.click()
                    time.sleep(TIME_CONST + random() * RAND_CONST)
                    like_btn.send_keys(Keys.ARROW_RIGHT)
                    time.sleep(TIME_CONST + random() * RAND_CONST)
                    if likes == nr_likes:
                        break
                    likes += 1
                    print(f"Liked: {likes}/{nr_likes}")
                except NoSuchElementException as e:
                    print(f"Error: {e}")
            # If like given, move to a next post
            else:
                like_btn.send_keys(Keys.ARROW_RIGHT)
                time.sleep(TIME_CONST + random() * RAND_CONST)

        print("✅ Post liking completed! ✅")


# ________ Code ________ #

if __name__ == "__main__":
    # Start the log
    with open(r"instagram_bot/log.txt", mode="a") as file:
        file.write(f"Task started at: {datetime.now()}\n")

    # Choose a random hastag
    hashtag = choice(HASTAGS)
    print(f"Hastag: {hashtag}\n")

    # Initialize the bot
    ig_bot = Instabot()
    # Log in to our account
    ig_bot.login()
    # Find and like post of the specified hastag
    ig_bot.find_hashtag_posts(hashtag)
    ig_bot.like_posts(randint(40, 80))

    # Quit the driver and make the end log
    ig_bot.driver.quit()
    with open(r"instagram_bot/log.txt", mode="a") as file:
        file.write(f"Task successfully completed at: {datetime.now()}\n")


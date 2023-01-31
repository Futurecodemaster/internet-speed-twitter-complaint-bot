from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = YOUR CHROME DRIVER PATH
TWITTER_EMAIL = YOUR TWITTER EMAIL
TWITTER_PASSWORD = YOUR TWITTER PASSWORD


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element_by_css_selector(".start-button a").click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//span[contains(@class, "speed-value-unit")][1]').text
        self.down = self.driver.find_element_by_xpath('//span[contains(@class, "speed-value-unit")][2]').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        email = self.driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
        password = self.driver.find_element_by_xpath('//input[@name="session[password]"]')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//div[contains(@class, "public-DraftEditor-content")]')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        self.driver.find_element_by_xpath('//div[contains(@data-testid, "tweetButtonInline")]').click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

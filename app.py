from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

TIME_FOR_ACTION_TO_FINISH = 5
URL = "https://my.yad2.co.il/login.php"


def init_driver(url, chrome_driver_path):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
    driver.get(url)
    return driver


def login(driver, yad2_username, yad2_password):
    username = driver.find_element_by_id("userName")
    username.send_keys(yad2_username)
    wait_for_action_to_finish()
    password = driver.find_element_by_id("password")
    password.send_keys(yad2_password)
    wait_for_action_to_finish()
    login = driver.find_element_by_id("submitLogonForm")
    login.click()
    wait_for_action_to_finish()


def bounce_post(driver, yad2_item_name, yad2_item_iframe):
    posts_link = driver.find_element_by_link_text("מכירות יד שנייה (2)")
    posts_link.click()
    wait_for_action_to_finish()
    item_td = driver.find_element_by_xpath(
        ".//*[@id='feed']//td[contains(.,'{}')]".format(yad2_item_name))
    item_td.click()
    wait_for_action_to_finish()
    driver.switch_to.frame(driver.find_element_by_xpath(
        "//iframe[@src='{}']".format(yad2_item_iframe)
    ))
    wait_for_action_to_finish()
    item_bounce_button = driver.find_element_by_xpath(
        "//span[@id='bounceRatingOrderBtn']")
    item_bounce_button.click()


def wait_for_action_to_finish():
    time.sleep(TIME_FOR_ACTION_TO_FINISH)


if __name__ == "__main__":
    chrome_driver_path = sys.argv[1]
    yad2_username = sys.argv[2]
    yad2_password = sys.argv[3]
    yad2_item_name = sys.argv[4]
    yad2_item_iframe = sys.argv[5]
    driver = init_driver(URL, chrome_driver_path)
    login(driver, yad2_username, yad2_password)
    bounce_post(driver, yad2_item_name, yad2_item_iframe)
    driver.close()

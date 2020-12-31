from time import sleep
import Constants
import traceback
import random

def login(webdriver):
    # Open the instagram login page
    webdriver.get(
        'https://www.instagram.com/accounts/login/?source=auth_switcher')
    # sleep for 3 seconds to prevent issues with the server
    sleep(3)
    # Find username and password fields and set their input using our constants
    username = webdriver.find_element_by_name('username')
    username.send_keys(Constants.INST_USER)
    password = webdriver.find_element_by_name('password')
    password.send_keys(Constants.INST_PASS)
    # Get the login button
    try:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
    except:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
    # sleep again
    sleep(2)
    # click login
    button_login.click()
    sleep(6)
    # In case you get a popup after logging in, press not now.
    # If not, then just return
    try:
        notnow = webdriver.find_element_by_css_selector(
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click()
    except:
        return

def like_posts(webdriver):
    likes = 0
    for hashtag in Constants.HASHTAGS:
        # Visit the hashtag
        print('Moving to new hashtag: ' + hashtag)
        webdriver.get(
            'https://www.instagram.com/explore/tags/' + hashtag + '/')
        sleep(random.randint(4, 6))

        # Get the first post thumbnail and click on it
        first_thumbnail = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div')
        sleep(random.randint(1, 3))
        first_thumbnail.click()

        for x in range(1, random.randint(35, 69)):
            try:
                sleep(3)
                button_like = webdriver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section/span/button/div/span/*[contains(@aria-label, 'Like')]")
                button_like.click()
                likes += 1
                print('Liked a picture, currently liked: ' + str(likes) + " pictures.")
                # Next picture
                sleep(random.randint(1, 2))
                webdriver.find_element_by_link_text('Next').click()
                sleep(random.randint(2, 3))
            except:
                print("Something went wrong OR picture already liked")
            finally:
                webdriver.find_element_by_link_text('Next').click()

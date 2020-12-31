import AccountAgent
import Constants


def init(webdriver):
    Constants.init()
    AccountAgent.login(webdriver)


def update(webdriver):
    while True:
        #Start following operation
        AccountAgent.like_posts(webdriver)

import sys
from instahelpers import *

instagram_login = ""
instagram_password = ""

filename = "likebot_" + instagram_login + ".log"
logging.basicConfig(filename=filename, format = '%(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO)

logging.info("Application started")
idriver = InstaDriver(True, instagram_login, instagram_password)
idriver.go_url("https://instagram.com")

driver = idriver.driver
assert "Instagram" in driver.title
idriver.suppress_notifications()

if idriver.check_already_logged_user() is False:
    if idriver.do_login() is False:
       sys.exit(1)
    idriver.suppress_notifications()

idriver.do_like_newsfeed(50)
driver.quit()

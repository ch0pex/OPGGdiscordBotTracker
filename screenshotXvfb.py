from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time

DRIVER_LOCATION = "/usr/bin/chromedriver"
BINARY_LOCATION = "/usr/bin/google-chrome"


DISPLAY_VISIBLE = 0
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 1000
def screenshot_op_gg(summoner):

    # start display
    display = Display(visible=DISPLAY_VISIBLE, size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))
    display.start()

    # start selenium
    options = webdriver.ChromeOptions()
    options.binary_location = BINARY_LOCATION

    driver = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=options)

    # 1.1 home page
    driver.get(f"https://euw.op.gg/summoners/euw/{summoner}/ingame")
    print("landing page --------->")
    print("current_url", driver.current_url)
    title=driver.title
    print("title: ", title)
    time.sleep(5)
    # 1.2 take a screenshot
    filename = f"screenshot/{summoner}.png"
    driver.save_screenshot(filename)
    driver.close()
    driver.quit()
    display.stop()
    return filename



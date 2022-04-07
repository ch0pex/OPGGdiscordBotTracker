from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time

DRIVER_LOCATION = "/usr/bin/chromedriver"
BINARY_LOCATION = "/usr/bin/google-chrome"


DISPLAY_VISIBLE = 0
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 3000
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

    # 1.2 take a screenshot
    filename = f"screenshot/{summoner}.png"
    driver.save_screenshot(filename)
    driver.close()
    driver.quit()
    display.stop()
    return filename

    # 1.3 click link to signin options page
"""    WAIT_ELEMENT = 30
    XPATH_VALUE = "//*[@id=\"imdbHeader\"]/div[2]/div[5]/a/div"
    x = WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, XPATH_VALUE)))
    outerHTML = x.get_attribute('outerHTML')
    print(outerHTML)
    time.sleep(5)
    x.click()

    # 2.1 driver is now on the signin options page
    print("\n", "signin options page --------->")
    print("current_url", driver.current_url)
    title=driver.title
    print("title: ", title)

    # 2.2 take a screenshot
    time.sleep(5)
    filename = f"/home/piuser/Desktop/tutorial/sel/screenshot/{title}.png"
    driver.save_screenshot(filename)"""

    # close browser and quit driver

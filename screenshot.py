from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from xvfbwrapper import Xvfb

class Screenshot():
    def demo_screen_capture(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://euw.op.gg/summoners/euw/TeGanoFumadisimo/ingame")
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\Users\\acbsu\\PycharmProjects\\DiscordBot\\screen.png")

    def demo_screen_capture2(self):
        d = Xvfb(width=400, height=400)
        d.start()
        browser = webdriver.Firefox()
        url = "http://stackoverflow.com/questions/4091940/how-to-save-web-page-as-image-using-python"
        browser.get(url)
        destination = "screenshot_filename.jpg"
        if browser.save_screenshot(destination):
            print
            ("File saved in the destination filename")
        browser.quit()

    def demo_screen_capture2(self):
        d = Xvfb(width=400, height=400)
        d.start()
        browser = webdriver.Firefox()
        url = "http://stackoverflow.com/questions/4091940/how-to-save-web-page-as-image-using-python"
        browser.get(url)
        destination = "screenshot_filename.jpg"
        if browser.save_screenshot(destination):
            print
            ("File saved in the destination filename")
        browser.quit()


demo = Screenshot()
demo.demo_screen_capture2()
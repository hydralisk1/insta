from splinter import Browser
from time import sleep

executable_path = {"executable_path":"chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
browser.driver.set_window_size(390, 844)

url = "https://www.instagram.com"
browser.visit(url)
sleep(1)
id = "hydralisk.ks@gmail.com"
password = "hy046790"

browser.find_by_name("username").fill(id)
browser.find_by_name("password").fill(password)
sleep(1)

browser.find_by_css(".sqdOP.L3NKy.y3zKF").first.click()
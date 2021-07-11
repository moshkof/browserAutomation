from selenium import webdriver

url = "https://www.worldometers.info/world-population/population-by-country/"

browser = webdriver.Chrome()

browser.get(url)

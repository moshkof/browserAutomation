from selenium import webdriver

url = "https://www.worldometers.info/world-population/population-by-country/"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(
    options=options, executable_path=r'C:\Users\serge\Documents\projects\python\browserAutomation\chromedriver.exe')

browser.get(url)

# assert "Population by Country" in browser.title

elem_a = browser.find_elements_by_tag_name("input")
print(elem_a)

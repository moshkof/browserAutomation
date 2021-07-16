from selenium import webdriver

url = "https://www.worldometers.info/world-population/population-by-country/"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(
    options=options, executable_path=r'C:\Users\serge\Documents\projects\python\browserAutomation\chromedriver.exe')

browser.get(url)

elem_a = browser.find_elements_by_xpath('//*[@id="example2"]/tbody/tr/td/a')
elem_text = []
for elem in elem_a:
    print(str(elem.text))
    elem_text.append(elem.text)
print(elem_text)
# //*[@id="example2"]/tbody/tr[2]/td[2]/a
# print(elem_a)
# elem_a.send_keys("Russia\n")


import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(f"https://www.google.com/travel/explore?tfs=CBwQAxojEgoyMDI1LTExLTE5agcIARIDQk5BcgwIBBIIL20vMDJqNzEaIxIKMjAyNS0xMS0xOWoMCAQSCC9tLzAyajcxcgcIARIDQk5BQAFIAXACggEECAoQAZgBAbIBBBgBIAE&tfu=GgA&hl=en&gl=us&curr=USD")

city_input = driver.find_element(By.CLASS_NAME, value="LbIaRd")
selected_city = input("Select a city: ")
print('Loading...')
driver.implicitly_wait(10)
city_input.clear()
city_input.send_keys(selected_city)
city_input.send_keys(Keys.ENTER)

print('Entered City')
print('Gathering flights')

flights_container = driver.find_elements(By.CLASS_NAME, value='tsAU4e')


flights_list = []
for flight in flights_container:
    flights_list.append(flight.text)

print(random.choice(flights_list))

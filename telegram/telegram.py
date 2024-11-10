from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome(service=Service("/home/varsha/Downloads/Python/chromedriver-linux64/chromedriver"))
driver.get("https://web.telegram.org/k/")

# login 
login_by_phone_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))

login_by_phone_button.click()

# enter mobile number
enter_number_div = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "input-field-phone")))

enter_number = enter_number_div.find_element(By.CLASS_NAME, "input-field-input")
enter_number.send_keys("+919812721938")

# after entering mobile number click on next

click_on_next = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
click_on_next.click()

# for otp, ask on console
print("Hi")
ask_otp = input("Enter OTP: ")

enter_otp_inp = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "input-field-input.is-empty")))

enter_otp_inp.clear()
enter_otp_inp.send_keys(ask_otp)
enter_otp_inp.send_keys(Keys.RETURN)

time.sleep(2)
# navigate to saved messages
driver.get("https://web.telegram.org/k/#@varsha_sharma01")

driver.implicitly_wait(10)
time.sleep(5)

last_time_stamp = None
message_only= None
prev_len = None 

while True:
    comp_messages_element = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//section[@class='bubbles-date-group']//div[@class='bubble-content']")))

    current_len = len(comp_messages_element)

    if current_len != prev_len:
        print(comp_messages_element[-1].text)
        prev_len = current_len
    else:
        print("No new message detected")


    time.sleep(5)


# driver.close()
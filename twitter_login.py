from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D')
time.sleep(3)
user_input = driver.find_element(by='xpath', value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
user_input.send_keys('bigbobbb.69.420@gmail.com')
time.sleep(3)
next_button = driver.find_element(by='xpath', value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
next_button.click()
# pass_input = driver.find_element(by='name', value='password')
time.sleep(500)

# i get the error message 'could not find account' at this point but no errors in the code, on track to work if i provide avalid phone, email, or username

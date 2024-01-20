from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd
import re

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

browser = webdriver.Chrome()
browser.get('https://linkedin.com')

username=browser.find_element(By.ID, "session_key")
username.send_keys("dirabiola@gmail.com")
password=browser.find_element(By.ID, "session_password")
password.send_keys("meet2004")

login_button=browser.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width")
login_button.click()

browser.get("https://www.linkedin.com/jobs/collections/recommended/")

job=browser.find_elements(By.CLASS_NAME, "job-card-list__title")
company=browser.find_elements(By.CLASS_NAME, "job-card-container__primary-description ")
location=browser.find_elements(By.CLASS_NAME, "job-card-container__metadata-item")
time=browser.find_elements(By.CLASS_NAME, "job-card-container__footer-item")


c=[]
d=[]
e=[]
f=[]
for i in range(0, len(job)):
    #print(i.text)
    c.append(job[i].text)
    d.append(company[i].text)
    e.append(location[i].text)
    f.append(time[i].text)

print(c)
print(d)
print(e)
print(f)

col = ['Title', 'Company', 'Location', 'Etc']

df = pd.DataFrame({'title':c, 'company':d , 'location':e, 'etc':f})

df.to_csv('jobs.csv')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import csv

firefox_binary_path = r"C:\Program Files\Mozilla Firefox\Firefox.exe"

options = Options()
options.binary_location = firefox_binary_path

service = Service('C:/geckodriver/geckodriver.exe')

driver = webdriver.Firefox(service=service, options=options)
driver.get('https://reqres.in/api-docs/#/')

wait = WebDriverWait(driver, 5)

method_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='opblock-summary-method']")))
method_texts = [method.text for method in method_elements]

path_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='opblock-summary-path']")))
path_texts = [path.text for path in path_elements]

driver.quit()

for i in range(len(path_texts)):
    if "{resource}" in path_texts[i]:
        path_texts[i] = path_texts[i].replace("{resource}", "colors")

post_body = {
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}

post_body_noEmail = {
  "email": "",
  "password": "cityslicka"
}

post_body_noPassword = {
  "email": "eve.holt@reqres.in",
  "password": ""
}

body = None

base_url = "https://reqres.in/api"

with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Method", "Path", "Body", "Result"])
    for i in range(len(method_texts)):
        if "{id}" in path_texts[i]:
            writer.writerow([method_texts[i], base_url + path_texts[i].replace("{id}", "1"), body, True])
            writer.writerow([method_texts[i], base_url + path_texts[i].replace("{id}", "0"), body, False])
            continue 
        if method_texts[i] == "POST" and (path_texts[i] == "/login" or path_texts[i] == "/register"):
            writer.writerow([method_texts[i], base_url + path_texts[i], post_body, True])
            writer.writerow([method_texts[i], base_url + path_texts[i], post_body_noEmail, False])
            writer.writerow([method_texts[i], base_url + path_texts[i], post_body_noPassword, False])
        else:
            writer.writerow([method_texts[i], base_url + path_texts[i], body, True])

   
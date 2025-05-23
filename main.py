from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import csv

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get('https://reqres.in/api-docs#/')

wait = WebDriverWait(driver, 5)

method_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='opblock-summary-method']")))
method_texts = [method.text for method in method_elements]

path_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='opblock-summary-path']")))
path_texts = [path.text for path in path_elements]

driver.get('https://reqres.in/signup')
header_value = driver.find_element(By.CSS_SELECTOR, ".code:nth-child(2)").text

driver.quit()

headers = {"x-api-key": header_value}

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

post_body_noValues = {
  "email": "",
  "password": ""
}

body = None

base_url = "https://reqres.in/api"

with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Method", "Path", "Body", "Header", "Result"])
    for i in range(len(method_texts)):
        if "{id}" in path_texts[i]:
            writer.writerow([method_texts[i], base_url + path_texts[i].replace("{id}", "1"), body, headers, True])
            writer.writerow([method_texts[i], base_url + path_texts[i].replace("{id}", "0"), body, headers, False])
            continue
        if method_texts[i] == "POST" and (path_texts[i] == "/login" or path_texts[i] == "/register"):
            writer.writerow([method_texts[i], base_url + path_texts[i], post_body, headers, headers, True])
            writer.writerow([method_texts[i], base_url + path_texts[i], post_body_noEmail, headers, False])
            writer.writerow([method_texts[i], base_url + path_texts[i], post_body_noPassword, headers, False])
            writer.writerow([method_texts[i], base_url + path_texts[i], post_body_noValues, headers, False])
        else:
            writer.writerow([method_texts[i], base_url + path_texts[i], body, headers, True])



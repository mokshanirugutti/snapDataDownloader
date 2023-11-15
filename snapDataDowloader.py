from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs",{"download.default_directory":"DOWNLOAD_DIRECTORY_PATH"})
driver = webdriver.Chrome(executable_path="CHROME_DRIVER_PATH",options=chrome_options)
file_path = "MEMORIES.HTML_PATH"
driver.get(file_path)
with open(file_path,'r',encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file,'html.parser')

links = soup.find_all("a",href=lambda href:href and "javascript:downloadMemories" in href)
for link in links:
    file_url = link['href']
    selection = f'a[href*="{file_url}"]'
    element = driver.find_element(By.CSS_SELECTOR,selection)
    element.click()
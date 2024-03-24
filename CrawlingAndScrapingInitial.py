import time
import requests
from bs4 import BeautifulSoup
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

text_elements = []
file_path = "output.txt"

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
webdriver_path = r'C:\chromedriver-win64\chromedriver.exe'

# Initialize Chrome webdriver with configured options
driver = webdriver.Chrome(service=Service(executable_path=webdriver_path), options=chrome_options)
fullsitetext = ""



# Function to crawl a webpage using requests and BeautifulSoup
def crawl_with_requests(url):
    try:
        response = requests.get(url, verify=False)  # Ignore SSL certificate verification
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.get_text(separator='\n')
        else:
            return ''
    except Exception as e:
        print("Error accessing site:", url)
        print("Error message:", e)
        return ''



# URL of the webpage you want to extract text from
with open('input.txt', 'r') as file:
    for line in file:
        site = line.strip()
        url = site
        print(site)
        try:
            driver.get(url)
            time.sleep(5)
            fullsitetext += site + ":\n"
            # Find all text elements on the webpage
            text_elements = driver.find_elements(By.XPATH, "//*[text()]")

            # Extract text from each element and print it
            try:
                for element in text_elements:
                    if len(element.text.strip()) > 0:
                        fullsitetext += element.text + "\n"
            except:
                pass

            # Use requests and BeautifulSoup for crawling
            crawled_text = crawl_with_requests(url)
            fullsitetext += crawled_text + "\n"
        except WebDriverException as e:
            print("Error accessing site:", site)
            print("Error message:", e)

# Close the webdriver
driver.quit()

# Write the collected text to output file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(fullsitetext.replace("\n\n", " "))



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import time

# Configuration
BASE_URL = "https://learn.microsoft.com/en-us/azure/?product=popular"
OUTPUT_DIR = "C:/AzureDocsPDFs"

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Set up Selenium WebDriver with advanced options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without opening a browser window
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Helper function to download PDFs
def download_pdf(pdf_url, output_dir):
    try:
        pdf_name = os.path.basename(pdf_url)
        output_path = os.path.join(output_dir, pdf_name)
        response = requests.get(pdf_url, stream=True)
        if response.status_code == 200:
            with open(output_path, 'wb') as pdf_file:
                for chunk in response.iter_content(chunk_size=1024):
                    pdf_file.write(chunk)
            print(f"Downloaded: {pdf_name}")
        else:
            print(f"Failed to download: {pdf_url} (Status: {response.status_code})")
    except Exception as e:
        print(f"Error downloading {pdf_url}: {e}")

# Step 1: Load the main page
driver.get(BASE_URL)
time.sleep(5)  # Wait for the page to load completely

# Step 2: Extract all subpage links
subpages = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "/en-us/azure/")]'))
)
subpage_links = list(set([link.get_attribute('href') for link in subpages]))

print(f"Found {len(subpage_links)} subpages to process.")

# Step 3: Iterate over each subpage and find PDF links
pdf_links = set()
for subpage in subpage_links:
    print(f"Processing subpage: {subpage}")
    driver.get(subpage)
    time.sleep(3)  # Allow the page to load
    pdf_elements = driver.find_elements(By.XPATH, '//a[contains(@href, ".pdf")]')
    for pdf in pdf_elements:
        pdf_url = pdf.get_attribute('href')
        if pdf_url and pdf_url.endswith(".pdf"):
            pdf_links.add(pdf_url)

print(f"Found {len(pdf_links)} PDF links.")

# Step 4: Download each PDF
for pdf_url in pdf_links:
    download_pdf(pdf_url, OUTPUT_DIR)

# Clean up
driver.quit()
print(f"All PDFs downloaded to {OUTPUT_DIR}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a Selenium webdriver
driver = webdriver.Chrome()

# Navigate to the webpage with dynamically loaded content
driver.get("https://example.com")

# Wait for the dynamically loaded content to appear
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dynamic-content")))

# Extract data from the dynamically loaded content
data = element.text

# Print or process the extracted data as needed
print(data)

# Close the webdriver
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the web browser
driver = webdriver.Edge()

# Navigate to the web page
driver.get('https://www.flightradar24.com/data/airports/doh/arrivals')

# Click on the alert button
button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
button.click()


# Click the button
for i in range(6):
    # wail until the button is loaded
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-flights-load'))
    )
    button.click()
    

# Close the web browser
driver.quit()




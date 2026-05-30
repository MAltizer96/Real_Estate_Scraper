from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def open_webpage(url):


    # Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Open the specified URL
    driver.get(url)

    # Keep the browser open for a while to see the result
    input("Press Enter to close the browser...")
    time.sleep(5)  # Wait for 5 seconds before closing the browser
    # Close the browser
    driver.quit()
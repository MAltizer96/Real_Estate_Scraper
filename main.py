import main_selenium
from dotenv import load_dotenv
import os

load_dotenv()
BUY_HOME_PAGE = os.getenv("BUY_HOME_PAGE")
CITYS = os.getenv("CITYS").split(",")
SEARCH_BOX_LABEL = os.getenv("SEARCH_BOX_LABEL")
VERIFICATION_PRESS_HOLD_BUTTON = os.getenv("VERIFICATION_PRESS_HOLD_BUTTON")

def main():
    main_selenium_OB = main_selenium.Main_Selenium()
    main_selenium_OB.open_webpage(BUY_HOME_PAGE)
    main_selenium_OB.check_element_exists("label", SEARCH_BOX_LABEL)
    print("Hello, World!")

if __name__ == "__main__":
    main()
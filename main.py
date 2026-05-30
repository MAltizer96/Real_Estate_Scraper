import main_selenium
import helper_methods

from dotenv import load_dotenv
import os

load_dotenv()
BUY_HOME_PAGE = os.getenv("BUY_HOME_PAGE")
CITYS = os.getenv("CITYS").split(",")
SEARCH_BOX_LABEL = os.getenv("SEARCH_BOX_LABEL").split(",")
VERIFICATION_PRESS_HOLD_BUTTON = os.getenv("VERIFICATION_PRESS_HOLD_BUTTON")

def main():
    print(SEARCH_BOX_LABEL)
    print(SEARCH_BOX_LABEL[0], SEARCH_BOX_LABEL[1])
    main_selenium_OB = main_selenium.Main_Selenium()
    main_selenium_OB.open_webpage(BUY_HOME_PAGE)
    main_selenium_OB.click_element_by_aria_label(SEARCH_BOX_LABEL[0], int(SEARCH_BOX_LABEL[1]))
    main_selenium_OB.type_in_element(CITYS[0])


    helper_methods.wait_time(5)

if __name__ == "__main__":
    main()
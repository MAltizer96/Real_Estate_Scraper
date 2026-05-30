import helper_methods

from selenium.webdriver.common.by import By
def check_for_captcha(driver):
    # Implement logic to check for captcha presence
    print("Checking for captcha...")
    while text_exists_in_dom(driver):
        element = driver.find_element(By.CLASS_NAME, "px-captcha-message")
        #element = driver.find_element(By.XPATH, "//p[contains(normalize-space(.), 'Press & Hold')]")
        print("element: ", element)
        helper_methods.move_mouse_to_element(element, y_offset=175)
        helper_methods.click_and_hold(helper_methods.get_long_random_delay())

    print("No captcha found.")
    while check_for_captcha_iframe(driver):
        helper_methods.wait_time(helper_methods.get_short_random_delay())
        iframe_element = driver.find_element(By.ID, "px-captcha-modal")
        driver.switch_to.frame(iframe_element)
        element = driver.find_element(By.ID, "px-captcha")
        print("Captcha iframe detected. Waiting for it to disappear...")
        helper_methods.move_mouse_to_element(element, y_offset=80)
        helper_methods.click_and_hold(helper_methods.get_long_random_delay())
        driver.switch_to.default_content()
    pass

def text_exists_in_dom(driver):
    print("Checking for text: 'Press & Hold'")
    helper_methods.wait_time(helper_methods.get_long_random_delay())
    print(driver.execute_script(
        "return document.querySelectorAll('.px-captcha-message').length"
    ))
    try:
        driver.find_element(By.CLASS_NAME, "px-captcha-message")

        print(f"Found text: 'Press &amp; Hold'")

        helper_methods.wait_time(helper_methods.get_short_random_delay())
        return True
    except:
        return False
    
def check_for_captcha_iframe(driver):
    print("Checking for captcha iframe...")
    
    helper_methods.wait_time(helper_methods.get_short_random_delay())
    try:
        driver.find_element(By.ID, "px-captcha-modal")
        print("Captcha iframe found.")       
        return True
    except:
        print("No captcha iframe found.")
        return False
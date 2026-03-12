from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

start_time = time.time()

def take_screenshot(driver,name):
    driver.save_screenshot(f"{name}.png")


options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app_package = "com.easemytrip.android"
options.app_activity = "com.easemytrip.compose.BaseMainActivity"
options.no_reset = True

driver = webdriver.Remote("http://127.0.0.1:4723",options=options)

wait = WebDriverWait(driver,30)

print("EaseMyTrip launched successfully")

# ---------------------
# TC1 Flights
# ---------------------
try:
    flights = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[@text='Flights']"))
    )
    flights.click()
    print("Test Case 1 - Flights Click : PASS")

except:
    print("Test Case 1 - Flights Click : FAIL")
    take_screenshot(driver,"tc1_fail")


# ---------------------
# TC2 From City
# ---------------------
try:
    from_city = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.easemytrip.android:id/search_flight_origin_code"))
    )

    from_city.click()

    search_box = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.easemytrip.android:id/search"))
    )

    search_box.send_keys("Chennai")

    city = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'Chennai')]"))
    )

    city.click()

    print("Test Case 2 - From City : PASS")

except:
    print("Test Case 2 - From City : FAIL")
    take_screenshot(driver,"tc2_fail")


# ---------------------
# TC3 To City
# ---------------------
try:
    to_city = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.easemytrip.android:id/search_flight_destination_code"))
    )

    to_city.click()

    search_box = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.easemytrip.android:id/search"))
    )

    search_box.send_keys("Mumbai")

    city = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'Mumbai')]"))
    )

    city.click()

    print("Test Case 3 - To City : PASS")

except:
    print("Test Case 3 - To City : FAIL")
    take_screenshot(driver,"tc3_fail")


# ---------------------
# TC4 Date Selection
# ---------------------
try:
    departure = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.easemytrip.android:id/search_flight_departure_date"))
    )

    departure.click()

    date = wait.until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"Date is 10 Apr 2024"))
    )

    date.click()

    driver.back()

    print("Test Case 4 - Date Selection : PASS")

except:
    print("Test Case 4 - Date Selection : FAIL")
    take_screenshot(driver,"tc4_fail")


# ---------------------
# TC5 Search Flights
# ---------------------
try:
    search_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.easemytrip.android:id/button_flight_Search"))
    )

    search_button.click()

    print("Test Case 5 - Search Flights : PASS")

except:
    print("Test Case 5 - Search Flights : FAIL")
    take_screenshot(driver,"tc5_fail")

time.sleep(5)


# ---------------------
# TC6 Negative - Invalid City
# ---------------------
try:
    from_city = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.easemytrip.android:id/search_flight_origin_code"))
    )

    from_city.click()

    search_box = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.easemytrip.android:id/search"))
    )

    search_box.send_keys("INVALIDCITY123")

    time.sleep(3)

    take_screenshot(driver,"tc6_invalid_city")

    print("Test Case 6 - Invalid City : FAIL (Screenshot captured)")

except:
    take_screenshot(driver,"tc6_invalid_city")
    print("Test Case 6 - Invalid City : FAIL (Screenshot captured)")


# ---------------------
# TC7 Negative - Empty Search
# ---------------------
try:
    driver.back()

    search_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID,"com.easemytrip.android:id/button_flight_Search"))
    )

    search_button.click()

    take_screenshot(driver,"tc7_empty_search")

    print("Test Case 7 - Empty Search : FAIL (Screenshot captured)")

except:
    take_screenshot(driver,"tc7_empty_search")
    print("Test Case 7 - Empty Search : FAIL (Screenshot captured)")


driver.quit()

print("Automation completed")

end_time = time.time()

print("Execution Time:",round(end_time-start_time,2),"seconds")

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Appium capabilities
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app_package = "com.easemytrip.android"
options.app_activity = "com.easemytrip.compose.BaseMainActivity"

# Connect to Appium
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(5)

print("App launched successfully")

# -----------------------------
# Test Case 1 : Click Flights
# -----------------------------
try:
    flights = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Flights']")
    flights.click()
    print("Flights button clicked")
except:
    print("Flights button not found")

time.sleep(3)

# -----------------------------
# Test Case 2 : Select FROM City
# -----------------------------
try:
    from_city = driver.find_element(AppiumBy.ID, "com.easemytrip.android:id/search_flight_origin_code")
    from_city.click()
    print("From city clicked")
except:
    print("From city not found")

time.sleep(3)

try:
    search_box = driver.find_element(AppiumBy.ID, "com.easemytrip.android:id/search")
    search_box.send_keys("Delhi")
    print("City typed")
except:
    print("Search box not found")

time.sleep(3)

try:
    city_select = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='New Delhi, India']")
    city_select.click()
    print("From city selected")
except:
    print("City selection failed")

time.sleep(3)

# -----------------------------
# Test Case 3 : Select TO City
# -----------------------------
try:
    to_city = driver.find_element(AppiumBy.ID, "com.easemytrip.android:id/search_flight_destination_code")
    to_city.click()
    print("To city clicked")
except:
    print("To city not found")

time.sleep(3)

try:
    search_box = driver.find_element(AppiumBy.ID, "com.easemytrip.android:id/search")
    search_box.send_keys("Mumbai")
    print("Destination typed")
except:
    print("Destination search box not found")

time.sleep(3)

try:
    city_select = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Mumbai, India']")
    city_select.click()
    print("Destination city selected")
except:
    print("Destination selection failed")

time.sleep(3)

# -----------------------------
# Test Case 4 : Select Departure Date
# -----------------------------
try:
    dep_date = driver.find_element(AppiumBy.ID, "com.easemytrip.android:id/search_flight_departure_date")
    dep_date.click()
    print("Departure calendar opened")
except:
    print("Departure date not found")

time.sleep(3)

try:
    select_date = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Date is 10 Apr 2024")
    select_date.click()
    print("Date selected")
except:
    print("Date selection failed")

time.sleep(3)

# -----------------------------
# Test Case 5 : Click Search
# -----------------------------
try:
    search_button = driver.find_element(AppiumBy.ID, "com.easemytrip.android:id/button_flight_Search")
    search_button.click()
    print("Search button clicked successfully")
except:
    print("Search button not found")

time.sleep(5)

print("All Test Cases Executed Successfully")

driver.quit()

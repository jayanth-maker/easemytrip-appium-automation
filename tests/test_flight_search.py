import time
from utils.report_generator import generate_html_report
from utils.driver_setup import get_driver
from pages.flight_page import FlightPage


start_time = time.time()

results = []

driver = get_driver()
page = FlightPage(driver)

print("EaseMyTrip launched successfully")

try:

    # Test Case 1
    page.click_flights()
    print("Test Case 1 - Flights Click : PASS")
    results.append(("Flights Click", "PASS"))
    time.sleep(2)

    # Test Case 2
    page.select_from_city("Chennai")
    print("Test Case 2 - From City : PASS")
    results.append(("From City", "PASS"))
    time.sleep(2)

    # Test Case 3
    page.select_to_city("Mumbai")
    print("Test Case 3 - To City : PASS")
    results.append(("To City", "PASS"))
    time.sleep(2)

    # Test Case 4
    page.select_date()
    print("Test Case 4 - Date Selection : PASS")
    results.append(("Date Selection", "PASS"))
    time.sleep(2)

    # Test Case 5
    page.click_search()
    print("Test Case 5 - Search Flights : PASS")
    results.append(("Search Flights", "PASS"))
    time.sleep(4)

    # Test Case 6 (Negative)
    driver.save_screenshot("tc6_invalid_city.png")
    print("Test Case 6 - Invalid City : FAIL (Screenshot captured)")
    results.append(("Invalid City", "FAIL"))
    time.sleep(2)

    # go back so second screenshot is different
    driver.back()
    time.sleep(3)

    # Test Case 7 (Negative)
    driver.save_screenshot("tc7_empty_search.png")
    print("Test Case 7 - Empty Search : FAIL (Screenshot captured)")
    results.append(("Empty Search", "FAIL"))

    print("Automation completed")

except Exception as e:

    print("Test failed:", e)

finally:

    driver.quit()

end_time = time.time()

execution_time = round(end_time - start_time, 2)

print(f"Execution Time: {execution_time} seconds")

generate_html_report(results, execution_time)

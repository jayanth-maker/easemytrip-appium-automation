import json
import time
import os

from utils.driver_setup import get_driver
from pages.flight_page import FlightPage
from utils.report_generator import generate_html_report


start_time = time.time()

print("Running AI Generated Test Cases")

results = []

# load AI test data
with open("test_data/ai_generated_tests.json") as file:
    test_cases = json.load(file)


driver = get_driver()
page = FlightPage(driver)

# ensure screenshot folder exists
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")


for index, test in enumerate(test_cases):

    try:

        time.sleep(2)

        page.click_flights()

        if test["from_city"] != "":
            page.select_from_city(test["from_city"])

        page.select_to_city(test["to_city"])

        page.click_search()

        time.sleep(4)

        if test["type"] == "positive":

            print(f"AI Test PASS → {test['from_city']} to {test['to_city']}")
            results.append((f"{test['from_city']} to {test['to_city']}", "PASS"))

        else:

            screenshot = f"screenshots/ai_negative_{index}.png"
            driver.save_screenshot(screenshot)

            print(f"AI Negative Test Executed → {test['from_city']} to {test['to_city']} (Screenshot captured)")
            results.append((f"{test['from_city']} to {test['to_city']}", "FAIL"))


    except Exception:

        screenshot = f"screenshots/ai_error_{index}.png"
        driver.save_screenshot(screenshot)

        print(f"AI Test Failed → {test['from_city']} to {test['to_city']} (Screenshot captured)")
        results.append((f"{test['from_city']} to {test['to_city']}", "FAIL"))


    finally:

        try:
            driver.back()
            time.sleep(1)

            driver.back()
            time.sleep(1)

        except:
            pass


driver.quit()

end_time = time.time()

execution_time = round(end_time - start_time, 2)

print("AI Automation completed")
print(f"Execution Time: {execution_time} seconds")

# generate HTML report
generate_html_report(results, execution_time)

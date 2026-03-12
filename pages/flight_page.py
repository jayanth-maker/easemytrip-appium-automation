from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlightPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    flights_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Flights']")

    from_city = (AppiumBy.ID, "com.easemytrip.android:id/search_flight_origin_code")

    to_city = (AppiumBy.ID, "com.easemytrip.android:id/search_flight_destination_code")

    search_box = (AppiumBy.ID, "com.easemytrip.android:id/search")

    search_button = (AppiumBy.ID, "com.easemytrip.android:id/button_flight_Search")

    departure_field = (AppiumBy.ID, "com.easemytrip.android:id/search_flight_departure_date")

    april_10 = (AppiumBy.ACCESSIBILITY_ID, "Date is 10 Apr 2024")


    # Actions

    def click_flights(self):

        self.wait.until(
            EC.element_to_be_clickable(self.flights_button)
        ).click()


    def select_from_city(self, city):

        self.wait.until(
            EC.element_to_be_clickable(self.from_city)
        ).click()

        search = self.wait.until(
            EC.element_to_be_clickable(self.search_box)
        )

        search.clear()
        search.send_keys(city)

        city_option = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, f"//android.widget.TextView[contains(@text,'{city}')]")
            )
        )

        city_option.click()


    def select_to_city(self, city):

        self.wait.until(
            EC.element_to_be_clickable(self.to_city)
        ).click()

        search = self.wait.until(
            EC.element_to_be_clickable(self.search_box)
        )

        search.clear()
        search.send_keys(city)

        city_option = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, f"//android.widget.TextView[contains(@text,'{city}')]")
            )
        )

        city_option.click()


    def select_date(self):

        # open calendar
        self.wait.until(
            EC.element_to_be_clickable(self.departure_field)
        ).click()

        # select date
        self.wait.until(
            EC.element_to_be_clickable(self.april_10)
        ).click()

        # close calendar so search button becomes visible
        self.driver.back()


    def click_search(self):

        self.wait.until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

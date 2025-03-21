import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By. CSS_SELECTOR, ".button.round")
    comfort_fare_icon = (By. XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_number_button = (By.CSS_SELECTOR, ".np-button")
    phone_number_field = (By.TAG_NAME, "label")
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    sms_code_field = (By.ID, "#code")
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    payment_method_button = (By.CSS_SELECTOR, ".pp-button.filled")
    add_card_field = (By.CSS_SELECTOR, ".card-number-input")
    add_card_code = (By.CSS_SELECTOR, ".card-code-input")
    card_form = (By.CSS_SELECTOR,
                 ".card-wrapper")  # localizador para hacer click en cualquier parte para que el campo cvv pierda el enfoque
    add_card_button = (By.XPATH, "//button[text()='Agregar']")
    close_payment_method_window = (By.XPATH, "//button[contains(@class, 'close-button')]")[2]
    mantas_y_pañuelos_slider = (By.XPATH,
                                "//div[contains(@class, 'r-sw-label') and contains(text(), 'Manta y pañuelos')]/following-sibling::div//span[contains(@class, 'slider round')]")
    helados_counter = (By.XPATH, "//div[contains(@class, 'counter-plus')]")[0]  # hacer click dos veces en el codigo
    # helados_counter.click()
    # time.sleep(1) #pausa entre clicks
    # helados_counter.click()
    final_request_taxi_button = (By.XPATH, ".smart-button")



    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.request_taxi_button)
        ).click()

    def get_comfort_fare_icon(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort_fare_icon)
        )

    def click_on_comfort_fare_icon(self):
        self.get_comfort_fare_icon().click()

    def get_phone_number_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.phone_number_button)
        )

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.phone_number_field)
        )

    def click_on_phone_number_field(self):
        self.get_phone_number_field().click()

    def set_phone_number_field(self, phone_number):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.phone_number_field)
        ).send_keys(phone_number)

    def get_next_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.next_button)
        )

    def click_on_next_button(self):
        self.get_next_button().click()

    def get_sms_code_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.sms_code_field )
        ).send_keys(self.driver.retrieve_phone_code)

    def get_payment_method_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.payment_method_button)
        )

    def click_on_payment_method_button(self):
        self.get_payment_method_button().click()








class TestUrbanRoutes:

    driver = None

    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_fare(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_request_taxi_button()
        routes_page.get_comfort_fare_icon()
        assert routes_page.get_comfort_fare_icon().text in "Comfort"

    def test_phone_number(self):
        self.test_select_comfort_fare()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_phone_number_button()
        routes_page.click_on_phone_number_field()
        routes_page.set_phone_number_field(data.phone_number)










    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

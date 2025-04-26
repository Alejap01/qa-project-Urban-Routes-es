import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from utils import retrieve_phone_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By. CSS_SELECTOR, ".button.round")
    comfort_fare_icon = (By. XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_number_field = (By.TAG_NAME, "label")
    phone = (By.XPATH, '//*[@id="phone"]')
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    sms_code_field = (By.ID,"code")
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    payment_method_button = (By.CLASS_NAME, "pp-value-text")
    add_card_button = (By.CSS_SELECTOR, "div.pp-plus-container")
    card_field = (By.ID,"number")
    card_code_field = (By.CSS_SELECTOR, ".card-code-input input")
    card_form = (By.CLASS_NAME,"card-wrapper")  # localizador para hacer click en cualquier parte para que el campo cvv pierda el enfoque
    form_add_card_button = (By.XPATH, "//button[text()='Agregar']")
    close_payment_method_window = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    message_driver = (By.ID,"comment")
    requisitos_pedido_header = (By.CLASS_NAME, "reqs-head")
    mantas_y_pañuelos_slider = (By.CSS_SELECTOR, 'div.switch > span.slider.round')
    cubeta_de_helado_header = (By.XPATH, '//div[text()="Cubeta de helado"]')
    helados_counter = (By.CSS_SELECTOR, '.counter-plus')  # hacer click dos veces en el codigo
    # helados_counter.click()
    # time.sleep(1) #pausa entre clicks
    # helados_counter.click()
    final_request_taxi_button = (By.CSS_SELECTOR, 'span.smart-button-main')
    searching_taxi_modal =(By.XPATH, '//div[@class="order-header-title"]')
    driver_information = (By.XPATH, "//div[contains(text(), 'El conductor llegará en')]")



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
        return WebDriverWait(self.driver, 10).until(
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
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.phone)
        ).send_keys(phone_number)

    def get_next_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.next_button)
        )

    def click_on_next_button(self):
        self.get_next_button().click()

    def get_sms_code_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.sms_code_field)
        )

    def click_on_sms_code_field(self):
        self.get_sms_code_field().click()

    def set_sms_code_field(self):
        sms_code = retrieve_phone_code(self.driver)
        field = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.sms_code_field)
        )
        field.send_keys(sms_code)

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.confirm_button)
        ).click()


    def get_payment_method_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.payment_method_button)
        )

    def click_on_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_card_button)
        ).click()

    def get_card_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.card_field)
        ).click()

    def set_card_field(self, card_number):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_field)
        ).send_keys(card_number)

    def get_card_code_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.card_code_field)
        ).click()

    def set_card_code_field(self, card_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_code_field)
        ).send_keys(card_code)

    def get_card_form(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.card_form)
        ).click()

    def get_form_add_card_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.form_add_card_button)
        ).click()

    def get_close_payment_method_window(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_payment_method_window)
        ).click()

    def set_message_driver(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.message_driver)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.clear()
        element.send_keys(data.message_for_driver)

    def get_requisitos_pedido_header(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.requisitos_pedido_header)
        ).click()

    def get_mantas_y_pañuelos_slider(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.mantas_y_pañuelos_slider)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def get_cubeta_de_helados_header(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cubeta_de_helado_header)
        ).click()

    def get_helados_counter(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.helados_counter)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        time.sleep(1)
        element.click()
        return element

    def get_final_request_taxi_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.final_request_taxi_button)
        ).click()

    def get_searching_taxi_modal(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.searching_taxi_modal)
        )

    def wait_for_driver_modal(self):
        wait = WebDriverWait(self.driver, 60)
        return wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'El conductor llegará en')]"))
        )


class TestUrbanRoutes:

    driver = None

    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

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
        routes_page.click_on_next_button()
        routes_page.set_sms_code_field()
        routes_page.get_confirm_button()
        second_request_taxi_button = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By. XPATH, '//span[text()="Pedir un taxi"]'))
        )
        assert second_request_taxi_button.is_displayed(), \
        "El botón 'Pedir un taxi' no está visible después de confirmar el número de teléfono."

    def test_add_credit_card(self):
        self.test_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_payment_method_button()
        routes_page.click_on_payment_method_button()
        routes_page.get_add_card_button()
        routes_page.get_card_field()
        routes_page.set_card_field(data.card_number)
        routes_page.get_card_code_field()
        routes_page.set_card_code_field(data.card_code)
        routes_page.get_card_form()
        routes_page.get_form_add_card_button()
        checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "card-1"))
        )
        # Verificar que esté seleccionado usando is_selected()
        assert checkbox.is_selected()
        routes_page.get_close_payment_method_window()

    def test_message_driver(self):
        self.test_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_driver()
        # Esperar y obtener el input del mensaje
        message_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "comment"))
        )
        # Leer el valor actual del campo
        current_message = message_input.get_attribute("value")
        # Comparar con el mensaje esperado desde data.py
        assert current_message == data.message_for_driver

    def test_request_blanket_and_tissues(self):
        self.test_message_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_requisitos_pedido_header()
        routes_page.get_mantas_y_pañuelos_slider()

        slider = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "switch-input"))
        )
        assert slider.is_selected()

    def test_ice_cream_counter(self):
        self.test_request_blanket_and_tissues()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_cubeta_de_helados_header()
        routes_page.get_helados_counter()
        counter_value = self.driver.find_element(By.CSS_SELECTOR, '.counter-value').text
        counter_value = self.driver.find_element(By.CSS_SELECTOR, '.counter-value').text
        assert counter_value == "2"

    def test_final_request_taxi_button(self):
        self.test_ice_cream_counter()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_final_request_taxi_button()
        routes_page.get_searching_taxi_modal()
        final_request_taxi_button = routes_page.get_searching_taxi_modal()
        assert final_request_taxi_button.is_displayed()

    def test_driver_information(self):
        self.test_final_request_taxi_button()
        routes_page = UrbanRoutesPage(self.driver)
        driver_information_modal = routes_page.wait_for_driver_modal()
        assert driver_information_modal.is_displayed()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

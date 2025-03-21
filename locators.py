    next_button = (By. XPATH, "//button[text()='Siguiente']")
    sms_code_field = (By.ID, "#code")
    confirm_button = (By. XPATH, "//button[text()='Confirmar']")
    payment_method_button = (By. CSS_SELECTOR, ".pp-button.filled")
    add_card_field = (By. CSS_SELECTOR, ".card-number-input")
    add_card_code = (By. CSS_SELECTOR, ".card-code-input")
    card_form = (By. CSS_SELECTOR, ".card-wrapper") #localizador para hacer click en cualquier parte para que el campo cvv pierda el enfoque
    add_card_button = (By. XPATH, "//button[text()='Agregar']")
    close_payment_method_window = (By. XPATH, "//button[contains(@class, 'close-button')]")[2]
    mantas_y_pañuelos_slider = (By. XPATH, "//div[contains(@class, 'r-sw-label') and contains(text(), 'Manta y pañuelos')]/following-sibling::div//span[contains(@class, 'slider round')]")
    helados_counter = (By. XPATH, "//div[contains(@class, 'counter-plus')]")[0] #hacer click dos veces en el codigo
        #helados_counter.click()
        #time.sleep(1) #pausa entre clicks
        #helados_counter.click()
    final_request_taxi_button = (By. XPATH, ".smart-button")
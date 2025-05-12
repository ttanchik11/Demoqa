from pages.form_page import FormPage
import time

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(3)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies_checkbox_1.click_force()
    form_page.current_address.send_keys('chtotonarodnom')
    time.sleep(3)
    form_page.btn_submit.click_force()
    time.sleep(3)

    assert form_page.modal_dialog.exist()
    form_page.bnt_close_modale.click_force()

    #выбор города в выпадашке
    # state_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "state")))
    # ActionChains(driver).move_to_element(state_dropdown).click().perform()
    #
    # # Выбор конкретного штата (например, "NCR")
    # state_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']")))
    # state_option.click()
    #
    # # Выбор City
    # city_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "city")))
    # ActionChains(driver).move_to_element(city_dropdown).click().perform()
    #
    # # Выбор конкретного города (например, "Delhi")
    # city_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Delhi']")))
    # city_option.click()


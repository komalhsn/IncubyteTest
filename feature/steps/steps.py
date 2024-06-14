import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

@given('the user is on the Gmail login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://mail.google.com/")
    context.driver.maximize_window()


@when('the user enters a valid username and password')
def step_impl(context):
    context.driver.find_element(By.ID, "identifierId").send_keys("komalkhsn@gmail.com")
    context.driver.find_element(By.ID, "identifierNext").click()
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).send_keys("Gmail@12345")
    context.driver.find_element(By.ID, "passwordNext").click()


@then('the user should be logged into Gmail')
def step_impl(context):
    inbox_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".T-I.T-I-KE.L3"))
    )
    assert inbox_button.is_displayed(), "Inbox button not displayed, login may have failed"


@when('the user clicks on the "{button}" button')
def step_impl(context, button):
    if button == "Compose":
        compose_button = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".T-I.T-I-KE.L3"))
        )
        compose_button.click()
    elif button == "Send":
        send_button = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3"))
        )
        send_button.click()


@then('a new email compose window should open')
def step_impl(context):
    compose_window = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".aaZ"))
    )
    assert compose_window.is_displayed(), "Compose window did not open"


@when('the user enters the recipient\'s email address')
def step_impl(context):
    to_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "to"))
    )
    to_field.send_keys("komal.srinu1@gmail.com")


@when('the user enters "{subject}" in the subject field')
def step_impl(context, subject):
    subject_field = context.driver.find_element(By.NAME, "subjectbox")
    subject_field.send_keys(subject)
    assert subject_field.get_attribute('value') == subject, "Subject not entered correctly"


@when('the user enters "{body}" in the email body')
def step_impl(context, body):
    body_field = context.driver.find_element(By.CSS_SELECTOR, ".Am.Al.editable.LW-avf")
    body_field.send_keys(body)
    assert body_field.text == body, "Body not entered correctly"


@then('the email should be sent successfully')
def step_impl(context):
    confirmation_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Message sent')]"))
    )
    assert confirmation_message.is_displayed(), "Email was not sent successfully"


@when('the user clicks on the "Sent" folder')
def step_impl(context):
    sent_folder = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".aio.UKr6le"))
    )
    sent_folder.click()


@then('the sent email should appear in the Sent Mail folder')
def step_impl(context):
    sent_email = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='bog']/span[contains(text(), 'Incubyte')]"))
    )
    assert sent_email.is_displayed(), "Sent email not found in Sent Mail folder"


@when('the user enters an invalid email address')
def step_impl(context):
    to_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "to"))
    )
    to_field.send_keys("invalid-email")


@then('an error message indicating an invalid email address should appear')
def step_impl(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Please check the recipient email address.')]"))
    )
    assert error_message.is_displayed(), "Error message for invalid email address not displayed"

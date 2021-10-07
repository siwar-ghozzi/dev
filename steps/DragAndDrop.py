from behave import given, when, then
from numpy.testing import assert_equal
from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains


@given(u'the user navigate to drag-drop home page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
    driver = context.driver
    driver.maximize_window()
    driver.get('https://qavbox.github.io/demo/dragndrop/')


@when(u'he drag the rectangle in his taget (green rectangle)')
def step_impl(context):
    driver = context.driver
    source_element = driver.find_element_by_id("draggable")
    dest_element = driver.find_element_by_id("droppable")
    ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
    time.sleep(2)


@then(u'"Droped!" message will be displayed in the target plce')
def step_impl(context):
    driver = context.driver
    success_msg = driver.find_element_by_id("dropText").text
    assert_equal(success_msg, "Dropped!")

from behave import when, then
from numpy.testing import assert_equal
import time

from selenium.webdriver import ActionChains


@when(u'he drag and drop the slider bar')
def step_impl(context):
    slider = context.browser.find_element_by_xpath('/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]')
    ActionChains(context.browser).drag_and_drop_by_offset(slider, 280, 16).perform()
    time.sleep(2)


@then(u'the value 100 will be displayed')
def step_impl(context):
    success_msg = context.browser.find_element_by_id("range").text
    assert_equal(success_msg, "100")


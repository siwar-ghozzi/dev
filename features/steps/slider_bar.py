from behave import when, then
from numpy.testing import assert_equal
from allure import severity, severity_level
import time

from selenium.webdriver import ActionChains

@severity(severity_level.MINOR)
@when(u'he drag and drop the slider bar')
def step_impl(context):
    context.dd.slider()
    time.sleep(2)


@then(u'the value 100 will be displayed')
def step_impl(context):
    assert_equal(context.dd.verif_slider(), "100")


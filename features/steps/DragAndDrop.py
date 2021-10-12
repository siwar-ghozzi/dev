from behave import given, when, then
from numpy.testing import assert_equal
import time

@given(u'the user navigate to drag-drop home page')
def step_impl(context):
    context.dd.setup('https://qavbox.github.io/demo/dragndrop/')


@when(u'he drag the rectangle in his taget (green rectangle)')
def step_impl(context):
    context.dd.drag()
    time.sleep(2)


@then(u'"Droped!" message will be displayed in the target plce')
def step_impl(context):
    msg = context.dd.result()
    assert_equal(msg, "Dropped!")

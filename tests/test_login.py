import pytest
from hamcrest import assert_that, equal_to

from steps import main_steps, item_steps


@pytest.mark.parametrize('item_name', [
    'Sauce Labs Backpack',
])
@pytest.mark.usefixtures('open_site')
def test_auth(item_name):
    main_page_price = main_steps.get_item_price(item_name)
    main_steps.open_item(item_name)
    item_page_price = item_steps.get_price()

    assert_that(main_page_price, equal_to(item_page_price))


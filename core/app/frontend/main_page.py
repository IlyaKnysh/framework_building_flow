from core.find_element import find_element


def item_price(item_name):
    return find_element(by='xpath',
                        value=f"//div[@class='inventory_item' and descendant::div[contains(text(), '{item_name}')]]//div[@class='inventory_item_price']")


def get_item(item_name):
    return find_element(by='xpath', value=f"//div[contains(text(), '{item_name}')]")

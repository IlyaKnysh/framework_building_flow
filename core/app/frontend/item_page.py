from core.find_element import find_element


def get_price():
    return find_element(by='xpath', value=f"//div[@class='inventory_details_price']")

import os
import final_project.test_final_project as test_final_project
from receipt import read_dictionary
from tempfile import mktemp
from final_project.test_final_project import approx

def test_read_dictionary():
    """Verify that the read_dictionary function works correctly.
    Parameters: none
    Return: nothing
    """
    PRODUCT_NUM_INDEX = 0

    # Verify if the 'products.csv' file exists
    filename = os.path.join(os.path.dirname(__file__), "products.csv")
    assert os.path.exists(filename), "File 'products.csv' not found."

    # Verify if the read_dictionary function can correctly read the file
    try:
        products_dict = read_dictionary(filename, PRODUCT_NUM_INDEX)
    except FileNotFoundError:
        test_final_project.fail(f"File '{filename}' not found.")
    except Exception as e:
        test_final_project.fail(f"Error trying to read the file '{filename}': {e}")

    # Verify that the function returns a dictionary
    assert isinstance(products_dict, dict), \
        f"Expected a dictionary, but found a {type(products_dict)}"

    # Verify that the dictionary contains exactly 16 items
    exp_len = 16
    length = len(products_dict)
    assert length == exp_len, \
        f"The dictionary contains {'fewer' if length < exp_len else 'more'} than {exp_len} items: expected {exp_len} but found {length}"

    # Verify that the dictionary contains the correct products
    check_product(products_dict, "D150", ["1 gallon milk", 2.85])
    check_product(products_dict, "D083", ["1 cup yogurt", 0.75])
    check_product(products_dict, "D215", ["1 lb cheddar cheese", 3.35])
    check_product(products_dict, "P019", ["iceberg lettuce", 1.15])
    check_product(products_dict, "P020", ["green leaf lettuce", 1.79])
    check_product(products_dict, "P021", ["butterhead lettuce", 1.83])
    check_product(products_dict, "P025", ["8 oz arugula", 2.19])
    check_product(products_dict, "P143", ["1 lb baby carrots", 1.39])
    check_product(products_dict, "W231", ["32 oz granola", 3.21])
    check_product(products_dict, "W112", ["wheat bread", 2.55])
    check_product(products_dict, "C013", ["twix candy bar", 0.85])
    check_product(products_dict, "H001", ["8 rolls toilet tissue", 6.45])
    check_product(products_dict, "H014", ["facial tissue", 2.49])
    check_product(products_dict, "H020", ["aluminum foil", 2.39])
    check_product(products_dict, "H021", ["12 oz dish soap", 3.19])
    check_product(products_dict, "H025", ["toilet cleaner", 4.50])

def check_product(products_dict, product_number, expected_value):
    """Verify that the data for one product number stored in the
    products dictionary is correct.
    Parameters:
        products_dict: dictionary containing product data
        product_number: the product number to verify
        expected_value: expected value (name and price of the product)
    Return: nothing
    """
    assert product_number in products_dict
    actual_value = products_dict[product_number]
    length = len(actual_value)
    min_len = 2
    max_len = 3
    assert min_len <= length and length <= max_len, \
        f"The value list for product {product_number} contains {'fewer' if length < min_len else 'more'} elements:" \
        f" expected {min_len} or {max_len} elements, but found {length}"

    # Verify the product's name
    if length == min_len:
        NAME_INDEX = 0
        PRICE_INDEX = 1
    else:
        NAME_INDEX = 1
        PRICE_INDEX = 2

    act_name = actual_value[NAME_INDEX]
    exp_name = expected_value[0]
    assert act_name == exp_name, \
        f"Incorrect name for product {product_number}: expected {exp_name} but found {act_name}"

    # Verify the product's price
    act_price = actual_value[PRICE_INDEX]
    if isinstance(act_price, str):
        act_price = float(act_price)
    exp_price = expected_value[1]
    assert act_price == approx(exp_price), \
        f"Incorrect price for product {product_number}: expected {exp_price} but found {act_price}"

# To run pytest directly from the code
if __name__ == "__main__":
    test_final_project.main(["-v", "--tb=line", "-rN", __file__])

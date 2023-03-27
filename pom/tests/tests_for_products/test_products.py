from pom.endpoints.products import Products
from pom.utils.json_models import product_json
from pom.base.base_api import BaseApi


def test_get_products(app_config):
    products = Products()
    products.get_products(app_config.base_url, "Polo Shirt")
    prod_list = products.get_products(app_config.base_url, 200)
    print(len(prod_list))
    products.check_products_data_by_length(prod_list, 19)


def test_create_product(app_config):
    products = Products()
    json_data = product_json.create_product_json("iphone 14", "The most awesome phone of 2022", 1000.00, 3)
    assert products.create_product(app_config.base_url, json_data).status_code == 201


def test_update_product(app_config):
    products = Products()
    json_data = product_json.update_product_json(1002, "iphone 13", "The most awesome phone of 2021", 900.00, 3)
    assert products.update_product(app_config.base_url, json_data).status_code == 200


def test_delete_product(app_config):
    products = Products()
    # product_id = products.
    product_id = product_json.delete_product_json(1002)
    assert products.delete_product(app_config.base_url, product_id).status_code == 200

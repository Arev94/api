from pom.base.base_api import BaseApi
import json

class Products(BaseApi):

    get_product_endpoint = '/api_testing/product/read.php'
    post_product_endpoint = '/api_testing/product/create.php'
    put_product_endpoint = '/api_testing/product/update.php'
    delete_product_endpoint = '/api_testing/product/delete.php'

    def get_products(self, url, expected_products):
        response = self.get_request(url + self.get_product_endpoint)
        list = self.get_json_value_by_key(response, "$.records..name")
        return list
        # exp_value = self.get_value_from_list(list, expected_products)
        # print(exp_value)

    def find_id_by_name(self, url,  product_name=None):
        response = self.get_request(url + self.get_product_endpoint)
        data_dict = json.loads(response.text)
        for record in data_dict['records']:
            if record['name'] == product_name:
                return record['id']
        return None

    def check_products_data_by_length(self, data, length):
        assert len(data) == length


    def create_product(self, url, json_data):
        response = self.post_request(url + self.post_product_endpoint, json_data )
        return response

    def update_product(self,url, json_data):
        response = self.put_request(url + self.put_product_endpoint, json_data)
        return response

    def delete_product(self, url, json_data):
        response = self.post_request(url + self.delete_product_endpoint, json_data)
        return response

from pom.base.base_api import BaseApi


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

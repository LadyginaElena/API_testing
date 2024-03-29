from dataclasses import dataclass
import requests
from data.api_data import RequestData as d


@dataclass
class Response:
    status_code: int
    json_data: object
    headers: dict
    text: str


class APIRequest:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }

    def get(self, endpoint="", path="", params=None, headers=None):
        url = f"{self.base_url}/{endpoint}/{path}"
        response = requests.get(url, params=params, headers=self.headers)
        return self.get_response_data(response)

    def post(self, endpoint="", path="", json=None, headers=None):
        url = f"{self.base_url}/{endpoint}/{path}"
        response = requests.post(url, json=d.data, headers=self.headers)
        return self.get_response_data(response)

    def put(self, endpoint="", json=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=d.data2, headers=self.headers)
        return self.get_response_data(response)

    def delete(self, endpoint="", path="", json=None, headers=None):
        url = f"{self.base_url}/{endpoint}/{path}"
        response = requests.delete(
            url, json=d.data, headers=self.headers
        )
        return self.get_response_data(response)

    def get_response_data(self, response):
        status_code = response.status_code
        json_data = response.json()
        headers = response.headers
        text = response.text
        return Response(status_code, json_data, headers, text)
        # request.path_url, request.method
        # response.request.headers получить заголовки запроса


# @pytest.fixture
# def api_client():
#     pet_store_url = "https://petstore.swagger.io/v2"
#     return APIRequest(base_url=pet_store_url)


# @pytest.mark.parametrize('endpoint', ['pet'])
# @pytest.fixture()
# def endpoint():
#     return "pet"

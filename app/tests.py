from rest_framework.test import APITestCase
from rest_framework.test import APIClient, APIRequestFactory

from app.utils.factory import UrlHistoryFactory
from app.views import UrlConverterView


class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        # self.user = self.setup_user()
        self.view = UrlConverterView.as_view()

        self.url_obj1 = UrlHistoryFactory(original_url="https://www.youtube.com/",
                                          converted_url="http://localhost:8000/short_url/?converted_url=xzq7jik3")

        self.url_obj1.save()

    def test_getting_existed_url(self):
        response = self.client.get(self.url_obj1.converted_url)

        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

        result = response.json()

        self.assertEqual(result[0]["original_url"], self.url_obj1.original_url,
                         'here'
                         .format(str(response.json())))

        self.assertEqual(result[0]["converted_url"], self.url_obj1.converted_url,
                         'here'
                         .format(str(response.json())))

    def test_getting_none_existed_url(self):
        converted_url = "http://localhost:8000/short_url/?converted_url=test"
        response = self.client.get(converted_url)

        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

        result = response.json()

        self.assertEqual(len(result), 0)


    def test_creating_new_url(self):
        url = "http://localhost:8000/short_url/"

        original_url = "https://gist.github.com/ahmad-amaniai/19d8f7e5c12cc2c4a3164b7c8da7c224"

        params = {
            "original_url": original_url,
        }

        response = self.client.post(url, params)

        self.assertEqual(response.status_code, 201)

        result = response.json()

        self.assertEqual(result["original_url"], original_url)

    def test_creating_attempting_existed_url(self):
        url = "http://localhost:8000/short_url/"
        params = {
            "original_url": self.url_obj1.original_url,
        }

        response = self.client.post(url, params)
        self.assertEqual(response.status_code, 200)

        result = response.json()

        self.assertEqual(result["original_url"], self.url_obj1.original_url)
        self.assertEqual(result["converted_url"], self.url_obj1.converted_url)

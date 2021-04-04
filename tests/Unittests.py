import unittest
import requests
import responses
from models.models import Contact
from models.models import Emails
import json


class Contacts(unittest.TestCase):
    host = "http://127.0.0.1:5000"
    endpoint = '{}/list/all/contacts'.format(host)
    second_endpoint = '{}/create/contact'.format(host)
    contacts = {
        "user_name": "Usama772",
        "first_name": "Usama",
        "last_name": "Ahmed",
        "phone_number": "+923074094938",
        "email_id": "Usama772@gmail.com"

    }

    def test_get_all_contacts(self):
        r = requests.get(Contacts.endpoint)
        self.assertEqual(r.status_code, 200)

    @responses.activate
    def test_create_contacts(self):
        responses.add(
            responses.POST,
            url=self.second_endpoint,
            body="200",
            match=[
                responses.urlencoded_params_matcher(self.contacts)
            ])
        r = requests.post(self.second_endpoint, data=self.contacts)

        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()

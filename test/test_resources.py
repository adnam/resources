# -*- coding: utf8 -*-
"""
"""
import unittest
from mock import Mock
from requests.models import Response as RResponse
from resources import Resource, JsonResource

class Response(object):
    status_code = 200
    text = ""
    def __init__(self, status=200, text=""):
        self.status_code, self.text = status, text

class NclientTestCase(unittest.TestCase):
    
    def setUp(self):
        self.client = Mock()

    def test_resources(self):
        url = "http://127.0.0.1"
        resource = Resource(url)
        self.assertEqual(url, str(resource))
        
        subresource = resource.subresource
        self.assertEqual("%s/subresource"%url, str(subresource))
    
        indexresource = subresource[123]
        self.assertEqual("%s/subresource/123"%url, str(indexresource))

    def test_resources_get(self):
        url = "http://localhost/api"
        client = Mock()
        fake_api = Resource(url, client=client)
        client.request.return_value = Response(200, "Hello")
        status, result = fake_api.get()
        self.assertEqual(200, status)
        self.assertEqual("Hello", result)


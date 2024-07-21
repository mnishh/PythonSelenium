# tests/test_example.py
import pytest
from selenium.webdriver.common.by import By
from pages.example_page import ExamplePage
import sys


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_search(self):
        self.driver.get("https://www.yatra.com/flights")
        page = ExamplePage(self.driver)
        page.search()
       

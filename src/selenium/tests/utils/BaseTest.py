from selenium import webdriver
import logging
import sys
import unittest


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)-15s %(levelname)-8s %(message)s")
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class BaseTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.close()

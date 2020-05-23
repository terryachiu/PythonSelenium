from src.selenium.tests.utils.BaseTest import BaseTest
from src.selenium.page_objects.DownloadPO import DownloadPO
from src.selenium.page_objects.GooglePO import GooglePO
import time


class QuickTest(BaseTest):

    def test_google(self):
        self.google_page = GooglePO(self.driver)
        self.google_page.go_to_homepage()

    def test_download(self):
        self.download_page = DownloadPO(self.driver)
        self.download_page.go_to_page()
        self.download_page.click_download_button()
        time.sleep(5)

from src.selenium.page_objects.utils.BasePO import BasePO
import os


class DownloadPO(BasePO):
    def go_to_page(self):
        self.driver.get("file://" + os.getcwd() + "/resources/download.html")

    def click_download_button(self):
        self.__get_download_button().click()

    def __get_download_button(self):
        return self.driver.find_element_by_css_selector('button.download')

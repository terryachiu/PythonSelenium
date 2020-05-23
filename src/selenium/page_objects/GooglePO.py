from src.selenium.page_objects.utils.BasePO import BasePO


class GooglePO(BasePO):
    def go_to_homepage(self):
        self.driver.get("http://www.google.com")


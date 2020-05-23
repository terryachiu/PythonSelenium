class BasePO(object):
    """ Base page object for all page objects to extend from """
    def __init__(self, driver):
        self.driver = driver
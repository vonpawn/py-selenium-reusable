from vonpawn.pyselenium.browser import Browser


class BasePage:
    def __init__(self, browser: Browser):
        self.browser = Browser
        self.locators = {}
        self.components = {}

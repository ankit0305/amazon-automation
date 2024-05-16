import logging

from playwright.sync_api import expect, Page
from locator import HomePageLocators

log = logging.getLogger(__name__)

class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def click_on_search(self):
        """
        """
        pass

    def is_logo_visible(self):
        """
        """
        expect(self.page.locator(HomePageLocators.NAV_LOGO)).to_be_visible()
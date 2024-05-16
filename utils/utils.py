import json, logging
from playwright.sync_api import Page

log = logging.getLogger(__name__)

class AllUtils:
    def __init__(self, page: Page) -> None:
        self.page = page

    def load_json_from_file(self):
        """
        Loads data from a json file
        return: A json object is returned
        """
        with open("testdata.json", "r") as f:
            json_obj = json.load(f)
        return json_obj
    
    def wait_for_selector(self, locator, timeout, state = "visible"):
        """
        Waits for a locator
        :param :locator waits for a locator
        :param :timeout waits for time in ms
        :param :state  default is visible, other values are hidden
        :returns :bool 
        """
        try:
            self.page.wait_for_selector(locator, timeout = timeout, state=state)
            return True
        except Exception as err:
            log.warning(f"Element not found {err}")
            return False

    
    def click_selector(self, locator, timeout=20000):
        """
        clicks a selector
        :param :locator clicks a locator
        :timeout default is 20000ms
        """
        self.wait_for_locator(locator, timeout = timeout)
        self.page.locator(locator).click()
import logging
from playwright.sync_api import expect
from locator import HomePageLocators

log = logging.getLogger(__name__)

from utils import AllUtils
utils_obj = AllUtils()

def test_launch_site(context, capture_test_name):
    """
    Launch a site
    """
    test_name = capture_test_name
    print(f"{test_name} being executed now")
    json_obj = utils_obj.load_json_from_file()
    url = json_obj["AMAZON_URL"]
    log.info(f"Navigating to URL: {url}")
    page = context.new_page()
    page.goto(url=url)
    expect(page.locator(HomePageLocators.NAV_LOGO)).to_be_visible()
    print(f"{test_name} executed successfully!")
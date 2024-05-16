import logging
from pages.home_page import HomePage

log = logging.getLogger(__name__)

from utils.utils import AllUtils


def test_launch_site(context, capture_test_name):
    """
    Launch a site
    """
    test_name = capture_test_name
    print(f"{test_name} being executed now")
    page = context.new_page()
    home_page = HomePage(page=page)
    utils_obj = AllUtils(page=page)
    json_obj = utils_obj.load_json_from_file()
    url = json_obj["AMAZON_URL"]
    log.info(f"Navigating to URL: {url}")
    page.goto(url=url)
    home_page.is_logo_visible()
    print(f"{test_name} executed successfully!")
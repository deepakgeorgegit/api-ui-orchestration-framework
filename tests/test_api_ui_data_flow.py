from api.auth_api import AuthAPI
from api.data_api import DataAPI
from pages.dashboard_page import DashboardPage


def test_api_created_data_is_visible_in_ui(driver):
    auth_api = AuthAPI()
    data_api = DataAPI()
    dashboard_page = DashboardPage(driver)

    
    response = auth_api.login("valid_user", "valid_password")
    cookies = auth_api.get_session_cookie(response)

    
    create_response = data_api.create_item(cookies)
    assert create_response.status_code == 201

    
    driver.get("https://example.com")
    for cookie in cookies:
        driver.add_cookie({
            "name": cookie.name,
            "value": cookie.value
        })
    driver.refresh()

    
    assert dashboard_page.is_item_visible("Test Item")

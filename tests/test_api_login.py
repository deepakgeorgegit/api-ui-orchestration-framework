from api.auth_api import AuthAPI
from api.data_api import DataAPI
from pages.dashboard_page import DashboardPage

def test_api_login_returns_session_cookie():
    auth_api = AuthAPI()
   
    response = auth_api.login("eve.holt@reqres.in","cityslicka")
    cookies = auth_api.get_session_cookie(response)
   
    assert response.status_code == 200
    assert len(cookies) > 0

def test_login_via_api_and_open_dashboard(driver):
    auth_api = AuthAPI() 
    dashboard_page = DashboardPage(driver)

    response = auth_api.login("eve.holt@reqres.in","cityslicka")
    cookies = auth_api.get_session_cookie(response)

    driver.get("https://example.com")
   
    for cookie in cookies:
        driver.add_cookie({
            "name": cookie.name,
            "value": cookie.value
        })
    driver.refresh()

    assert dashboard_page.is_loaded()
    
def test_api_created_data_is_visible_in_ui(driver):
    auth_api = AuthAPI()
    data_api = DataAPI()
    dashboard_page = DashboardPage(driver)

    response = auth_api.login("eve.holt@reqres.in","cityslicka")
    cookies = auth_api.get_session_cookie(response)

    create_response = data_api.create_item(cookies)
    assert create_response.status_code == 201

    item_id = create_response.json()["id"]

    try:
        
        driver.get("https://example.com")
        for cookie in cookies:
            driver.add_cookie({
                "name": cookie.name,
                "value": cookie.value
            })
        driver.refresh()

      
        assert dashboard_page.is_item_visible("Test Item")

    finally:
       
        delete_response = data_api.delete_item(item_id, cookies)
        assert delete_response.status_code == 204

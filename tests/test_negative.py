def test_access_inventory_without_login(driver, base_url):
    # Directly open inventory page without login
    driver.get(base_url + "/inventory.html")

    # Expect redirect to login page
    assert "login" in driver.current_url.lower()

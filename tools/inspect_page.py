from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://app.beemerbenzbentley.site/auth/signup')
    page.wait_for_load_state('networkidle')
    
    inputs = page.query_selector_all('input')
    print("Signup Inputs:")
    for i in inputs:
        print(f"Name: {i.get_attribute('name')}, Type: {i.get_attribute('type')}")
        
    browser.close()

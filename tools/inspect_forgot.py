from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://app.beemerbenzbentley.site/auth/forget-password')
    
    try:
        page.wait_for_selector('input', timeout=15000)
    except Exception as e:
        print("Timeout waiting for input on forgot password page.")
    
    inputs = page.query_selector_all('input')
    print(f"Found {len(inputs)} inputs:")
    for inp in inputs:
        print(f"  Type: {inp.get_attribute('type')}, Name: {inp.get_attribute('name')}, Placeholder: {inp.get_attribute('placeholder')}")
        
    buttons = page.query_selector_all('button')
    print(f"\nFound {len(buttons)} buttons:")
    for btn in buttons:
        print(f"  Text: {btn.inner_text().strip()}, Type: {btn.get_attribute('type')}")
        
    links = page.query_selector_all('a')
    print(f"\nFound {len(links)} links:")
    for link in links:
        print(f"  Text: {link.inner_text().strip()}, Href: {link.get_attribute('href')}")
        
    browser.close()

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://app.beemerbenzbentley.site/auth/login')
        page.fill('input[name="email"]', 'shivam@yopmail.com')
        page.fill('input[name="password"]', 'Pass@9988')
        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)
        import sys
        print('Current URL:', page.url)
        try:
            err = page.locator('.error-message, .alert-danger, [role="alert"], .text-danger, .Toastify__toast--error, .toast').first
            if err.is_visible(timeout=2000):
                print('Error text:', err.inner_text())
            else:
                print('No error visible.')
        except Exception as e:
            print('No error visible, exception:', e)
        
        browser.close()

if __name__ == "__main__":
    run()

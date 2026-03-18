from playwright.sync_api import sync_playwright
import time
from config.data import SIGNUP_EXISTING_EMAIL

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://app.beemerbenzbentley.site/auth/signup')
    page.wait_for_load_state('networkidle')
    
    page.fill('input[name="first_name"]', 'shivam')
    page.fill('input[name="last_name"]', 'srivastava')
    page.fill('input[name="email"]', 'shivam@yopmail.com')
    page.fill('input[name="password"]', 'Pass@9988')
    page.fill('input[name="password_repeat"]', 'Pass@9988')
    
    page.press('input[name="password_repeat"]', 'Enter')
    time.sleep(3)
    
    body = page.locator('body').inner_text()
    if 'already' in body.lower() or 'exist' in body.lower() or 'error' in body.lower():
        print("Found error text in body:")
        lines = [l for l in body.split('\n') if 'already' in l.lower() or 'exist' in l.lower() or 'error' in l.lower()]
        print(lines)
        
    toasts = page.query_selector_all('[role="alert"], .toast, .snackbar, .go3958317564')
    print(f"Found {len(toasts)} toasts/alerts:")
    for t in toasts:
        print(" ->", t.inner_text())
        
    browser.close()

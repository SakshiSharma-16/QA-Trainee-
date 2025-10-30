from playwright.sync_api import sync_playwright
import pytest

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def login(page):
    page.goto(URL)
    page.fill('input[name="username"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_selector('text=Dashboard')

def test_add_edit_delete_user(browser):
    page = browser.new_page()
    login(page)
    # Navigate to Admin → User Management
    page.click("text=Admin")
    page.wait_for_selector("text=System Users")

    # Add user
    page.click('button:has-text("Add")')
    page.select_option('select[role="listbox"]', label="ESS")
    page.fill('input[placeholder="Type for hints..."]', "Linda")
    page.wait_for_timeout(1000)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    page.fill('(//input[@class="oxd-input oxd-input--active"])[2]', "linda.demo1")
    page.fill('input[type="password"]', "Test@1234")
    page.fill('(//input[@type="password"])[2]', "Test@1234")
    page.click('button:has-text("Save")')
    page.wait_for_selector('text=Success')

    # Search user
    page.fill('input[placeholder="Type for hints..."]', "linda.demo1")
    page.click('button:has-text("Search")')
    page.wait_for_selector('text=linda.demo1')

    # Delete user
    page.click('i.bi-trash')
    page.click('button:has-text("Yes, Delete")')
    page.wait_for_selector('text=Successfully Deleted')

    page.close()

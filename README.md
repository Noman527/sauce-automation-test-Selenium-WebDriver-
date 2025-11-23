# SauceDemo Automation Framework (Python + Selenium + Pytest)

This repository contains an end-to-end test automation framework for the demo e-commerce site **[saucedemo.com](https://www.saucedemo.com/)**.

The framework is built using:

- **Python**
- **Selenium WebDriver**
- **Pytest** (test runner)
- **Page Object Model (POM)**
- **pytest-html** (HTML test report)
- **webdriver-manager** (for driver management)

This project was created as part of a **QA Automation Engineer 2-Day Technical Assessment**.

---

## 📌 Project Objectives

The goal of this framework is to automate the following key flows:

1. **Login Functionality**
   - Successful login with valid credentials
   - Unsuccessful login with invalid password
   - Assert correct error messages

2. **Add to Cart & Checkout**
   - Login and add two items to the cart
   - Verify items in cart
   - Complete checkout
   - Validate success message and empty cart

3. **Product Sorting**
   - Sort products from “Price (low to high)”
   - Verify products are sorted correctly
   - Capture screenshot of sorted page

4. **Negative Scenario**
   - Try accessing `/inventory.html` without login
   - Verify user is restricted and shown login page + proper message

5. **Screenshot on Failure**
   - Automatically capture screenshots when a test fails

6. **Test Reporting**
   - Generate an HTML test report using `pytest-html`

---

## 🧱 Tech Stack

- **Language:** Python  
- **Automation Tool:** Selenium WebDriver  
- **Test Runner:** Pytest  
- **Design Pattern:** Page Object Model (POM)  
- **Report:** pytest-html (HTML report)  
- **Driver Management:** webdriver-manager  

---

## 📁 Project Structure

```text
sauce-automation-test/
│
├── pages/
│   ├── base_page.py          # Common wrapper methods (click, type, wait, find, etc.)
│   ├── login_page.py         # Locators and actions for Login page
│   ├── products_page.py      # Product listing, sorting, add to cart
│   ├── cart_page.py          # Cart page actions, item count
│   ├── checkout_page.py      # Checkout information and confirmation
│
├── tests/
│   ├── test_login.py         # Login (valid + invalid)
│   ├── test_cart_checkout.py # Add to cart + checkout flow
│   ├── test_sorting.py       # Price sorting (low to high)
│   ├── test_negative.py      # Access inventory page without login
│
├── reports/
│   ├── report.html           # Auto-generated HTML report (pytest-html)
│   └── screenshots/          # Screenshots on failures / additional captures
│
├── conftest.py               # Pytest fixtures (driver setup, config, screenshots on failure)
├── config.json               # Base URL, browser type, credentials, headless mode flag
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

# CS406 Selenium Project

This is a simplified Selenium WebDriver + pytest project for the CS406 Software Quality Assurance assignment.

## Website Tested

[https://automationexercise.com/](https://automationexercise.com/)

## Final Test Scenario

The final suite keeps one assignment-relevant end-to-end scenario:

`test_search_blue_top_add_to_cart_e2e`

Steps and checks:

1. Open the Automation Exercise home page.
2. Verify the page title contains `Automation Exercise`.
3. Navigate to the Products page.
4. Type `Blue Top` in the search box.
5. Click the search button.
6. Verify the searched products section appears.
7. Verify `Blue Top` appears in the returned results.
8. Click `Add to cart` for the `Blue Top` product.
9. Open the Cart page from the add-to-cart modal, with the Cart menu as a fallback.
10. Verify the cart contains:
    - Product name: `Blue Top`
    - Price: `Rs. 500`
    - Quantity: `1`

## Test Count

There is 1 test scenario. The `driver` fixture runs it in both Chrome and Firefox, so a full run collects 2 pytest test cases.

## Project Structure

```text
pages/
  base_page.py
  home_page.py
  products_page.py
  cart_page.py

tests/
  test_cart.py

conftest.py
pytest.ini
requirements.txt
```

## Page Object Model

The project uses the Page Object Model pattern:

- `BasePage` stores shared Selenium helpers and explicit waits.
- `HomePage` handles home page navigation.
- `ProductsPage` handles product search, result verification, and add-to-cart actions.
- `CartPage` verifies cart page content.
- `tests/test_cart.py` contains the final E2E test scenario.

## Browser Support

The tests run on both Chrome and Firefox through the parametrized pytest fixture in `conftest.py`.

`webdriver-manager` downloads the matching ChromeDriver and GeckoDriver automatically.

## Wait Strategy

The project uses no fixed-delay calls. All synchronization is handled with Selenium `WebDriverWait` and `expected_conditions`.

## Installation

Use Python 3.8+ with Chrome and Firefox installed.

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Running Tests

Run the full suite:

```bash
python -m pytest -v
```

Run the syntax check:

```bash
python -m py_compile pages/*.py tests/*.py
```

Run only Chrome or Firefox:

```bash
python -m pytest -v -k chrome
python -m pytest -v -k firefox
```

## Generated Files

Generated files and folders such as `.venv/`, `__pycache__/`, `.pytest_cache/`, `.DS_Store`, and `reports/` are excluded with `.gitignore`.

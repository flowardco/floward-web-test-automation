
# Floward Web Automation Framework

This project is a Playwright-based automation framework designed for web testing. It includes support for test execution, reporting, and easy configuration, making it ideal for robust automated testing workflows.

## Features
- **Built with Playwright and Python** for modern, fast browser automation.
- **Allure Reports** for interactive and visually appealing test results.
- Configurable with **`pytest`** for test execution and flexibility.
- Modular and maintainable structure following the **Page Object Model (POM)** design pattern.

---

## Prerequisites
Ensure the following tools and dependencies are installed:
1. **Python** (>= 3.10): Download from [python.org](https://www.python.org/downloads/).
2. **Allure CLI**: 
   - For macOS:
     ```bash
     brew install allure
     ```
   - For Windows/Linux: Follow the instructions [here](https://docs.qameta.io/allure/).
3. **Node.js** (Optional, for Playwright browser setup):
   ```bash
   brew install node
   ```

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Floward_web_automation
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # Use myenv\Scripts\activate on Windows
   ```

3. **Install Dependencies**:
   Install all necessary Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright Browsers**:
   Install the required browsers:
   ```bash
   playwright install
   ```

---

## Running Tests

### Option 1: Run Tests and View Allure Report
Run the tests and serve the Allure report in one go:
```bash
pytest tests/ --alluredir=allure-results && allure serve allure-results
```

### Option 2: Run Tests Only
Run tests and generate raw Allure results:
```bash
pytest tests/
```

### Option 3: Generate Allure Report
If you have raw results in `allure-results`, generate the report:
```bash
allure generate allure-results -o allure-report --clean
```

---

## Project Structure

```plaintext
Floward_web_automation/
├── config/              # Contains global configuration (e.g., base URL)
│   └── config.json
├── tests/               # Test files organized by feature or functionality
│   ├── test_example.py
│   ├── conftest.py       # Shared fixtures and test setup
├── pages/               # Page Object Model (POM) classes
│   ├── base_page.py
│   ├── __init__.py
├── utils/               # Helper functions (e.g., config loading)
│   ├── helpers.py
├── pytest.ini           # Pytest configuration
├── requirements.txt     # Python dependencies
```

---

## Example Configuration
`config/config.json`:
```json
{
  "base_url": "https://example.com",
  "browser": "chromium"
}
```

---

## Dependencies
All dependencies are listed in `requirements.txt`. To install them:
```bash
pip install -r requirements.txt
```

---

## Allure Reports
Allure Reports provide detailed and graphical test results. The raw results are stored in `allure-results`, and reports are generated in `allure-report`.

To generate and view the report:
```bash
allure serve allure-results
```

---

## Contributing
Feel free to open issues or submit pull requests to improve the framework.

---

## Future Enhancements
- Add support for CI/CD pipelines.
- Implement environment-specific configurations.
- Extend test cases for comprehensive coverage.
```

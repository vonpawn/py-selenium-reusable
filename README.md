# py-selenium-reusable
A place to house my commonly used project setup and patterns for selenium automation

## Setup
### Python virtualenv + dependencies
```bash
cd py-selenium-reusable
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
### config
```

```

## Running
```bash
pytest ... 
  --html=pytest_report.html  #  visual report of test run
  --self-contained-html  # makes the html easier to transport to other service
  --junitxml  # If exporting to jenkins/ci pipeline
```

# TODO:
 - Research allure reporting
 - Add example implementation of page objects/test suite for a demo site (https://www.saucedemo.com/?)

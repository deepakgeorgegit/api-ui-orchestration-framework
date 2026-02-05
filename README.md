# API + UI Orchestration Automation Framework

## Overview
This project demonstrates **API-first test orchestration**, where backend APIs are used to prepare test state and the UI is used only for final validation.

The focus of this framework is **test strategy and responsibility separation**, not UI-heavy automation.

---

## Tech Stack
- Python
- PyTest
- Selenium
- REST APIs (requests)

## Project Structure

```
api-ui-orchestration-framework/
│
├── api/
│   ├── __init__.py
│   └── clients/
│       ├── __init__.py
│       └── auth_client.py
│
├── ui/
│   ├── __init__.py
│   └── pages/
│       ├── __init__.py
│       ├── base_page.py
│       └── dashboard_page.py
│
├── tests/
│   ├── test_api_login.py
│   └── test_api_ui_data_flow.py
│
├── conftest.py
├── pytest.ini
├── .gitignore
└── README.md
```


##  Test Scenarios Covered
- API-based authentication
- Backend data preparation using APIs
- UI validation of backend-prepared state
- End-to-end API + UI orchestration

---

##  Design Philosophy
- APIs are used for **setup and control**
- UI is used only for **verification**
- Page Objects are intentionally minimal
- Fixtures provide **system state**, not business logic

This approach improves test speed, reliability, and maintainability.

---

## How to Run Tests
```bash
pytest

 Scope

This project focuses on orchestration patterns.
Business-domain flows such as cart and checkout are implemented in a separate e-commerce project.




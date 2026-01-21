# QA API Tests – JSONPlaceholder

##  Project Overview

This project is a **pet project for API test automation** written in Python using **pytest**.
It is built on top of the public REST API **JSONPlaceholder**.

The goal of the project is to demonstrate:

* REST API testing (CRUD operations)
* clean and scalable test architecture
* positive and negative test scenarios
* realistic handling of non-standard API behavior


---

##  Tech Stack

* **Python 3.13**
* **pytest**
* **requests**
* **pydantic** (data validation)
* **pytest-html** (HTML reports)

---

##  Project Structure

```
QA-api-tests/
├── api/                # API endpoints (route abstraction)
│   ├── posts.py
│   └── users.py
│
├── models/             # Pydantic data models
│   ├── post.py
│   └── user.py
│
├── utils/              # Utilities
│   └── api_client.py   # Base HTTP client
│
├── tests/              # Test cases
│   ├── test_post.py
│   ├── test_posts.py
│   ├── test_post_update_put.py
│   ├── test_post_patch_negative.py
│   ├── test_post_delete.py
│   ├── test_post_delete_negative.py
│   ├── test_post_delete_negative_indempotency.py
│   ├── test_user.py
│   └── test_users_negative.py
│
├── config/
│   └── settings.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

##  Architecture Explanation

### API Layer (`api/`)

Encapsulates all API endpoints in one place.

Example:

```python
class PostsAPI:
    BASE = "/posts"

    @staticmethod
    def by_id(post_id: int) -> str:
        return f"{PostsAPI.BASE}/{post_id}"
```

This approach:

* avoids hardcoded URLs in tests
* improves readability
* simplifies maintenance when endpoints change

---

### API Client (`utils/api_client.py`)

A reusable HTTP client built on top of `requests`.

Responsibilities:

* base URL handling
* timeout configuration
* unified methods: `get`, `post`, `put`, `patch`, `delete`

Tests do not work with `requests` directly — they use this abstraction.

---

### Models (`models/`)

Pydantic models are used to validate API responses.

Benefits:

* schema validation
* type safety
* early detection of contract issues

---

### Tests (`tests/`)

Test cases cover:

* **CRUD operations** (POST, GET, PUT, PATCH, DELETE)
* **Positive scenarios**
* **Negative scenarios** (invalid IDs, invalid payloads)
* **Idempotency checks** (DELETE twice)

Markers are used to organize tests:

* `@pytest.mark.positive`
* `@pytest.mark.negative`
* `@pytest.mark.regression`

---

##  API Behavior Notes

JSONPlaceholder is a mock API, so it behaves differently from real production APIs:

* Returns `200 OK` even for non-existing IDs
* Does not persist changes
* Echoes partial payloads for PATCH requests

All tests are written to **match the real behavior of the API**, not assumptions.

---

##  How to Run Tests

1. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run all tests

```bash
pytest
```

4. Run only negative tests

```bash
pytest -m negative
```

---

##  Test Results

Current status:

* ✅ 17 automated API tests
* ✅ All tests passing

---

##  Next Steps

* Contract testing with `jsonschema`
* API mocking with `responses`
* CI integration (GitHub Actions)
* Reporting with Allure
* Transition to UI automation with Playwright

---

##  Author

Nazar — QA Automation Engineer (in progress)

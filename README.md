# 2025 Advent of Code Solutions in Python

## Setup

Install required dependencies:
```powershell
pip install -r requirements.txt
```

For development (including testing):
```powershell
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Running Solutions

To run each day's solution:
```powershell
python -m day_1.day_1
python -m day_2.day_2
```

## Running Tests

Run all tests:
```powershell
python -m pytest
```

Run tests with coverage report:
```powershell
python -m pytest --cov=. --cov-report=term-missing
```

Run tests for a specific day:
```powershell
python -m pytest day_1/test_solutions.py
```

Run tests for a specific day with coverage:
```powershell
python -m pytest day_1/ --cov=day_1 --cov-report=term-missing
```

Run tests in verbose mode:
```powershell
python -m pytest -v
```

## Dependencies

- `requests` - For fetching puzzle input from adventofcode.com
- `parsy` - Parser combinator library for parsing puzzle input

### Development Dependencies

- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting for pytest

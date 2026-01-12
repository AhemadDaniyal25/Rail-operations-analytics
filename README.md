# Rail Operations Data Validation Framework

## Overview
This repository implements a **Python-based data validation framework for rail operations data**, inspired by quality assurance workflows used in engineering tools and transportation systems.

The project focuses on **systematic verification, data quality checks, and automated testing**, rather than exploratory analytics or dashboards.

It is designed to demonstrate skills relevant to **Quality Assurance in Engineering Tools**, including rule-based validation, test automation, and structured reporting.

---

## Key Features

- **12 explicit validation rules** covering:
  - Numerical validity (e.g. delay bounds, energy constraints)
  - Data completeness (missing operational fields)
  - Consistency rules (route–region mapping, maintenance flags)
- **Validation engine** that executes all rules deterministically
- **Severity-based issue classification** (ERROR / WARNING)
- **Automated quality reports** (JSON output)
- **31+ automated pytest unit tests**
- Clean `src/` project layout, CI/CD–ready

---

## Validation Scope

Examples of implemented checks include:
- Non-negative and realistic delay bounds
- Positive energy consumption
- Asset age realism
- Mandatory operational fields (route, train ID, energy, delay)
- Route-to-region consistency
- Binary maintenance event flags
- Alphanumeric route identifiers

Each rule has:
- explicit pass/fail criteria
- clear error messages
- unit test coverage

---

## Architecture

- **Python**: validation rules, engine, reporting
- **pytest**: automated unit testing
- **Rule-based design**: similar to plugin validation frameworks used in engineering tools



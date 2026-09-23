
# Assignment 03 — CHANGES

**Name:** Kyaw San  **Student ID:** 6705140029

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.[cite: 1]

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.[cite: 1]

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Raw numbers (`0.07`, `100`, `10`, `0.03`) and `global TAXRATE` inside `calc()`[cite: 2] | Top-level named constants (`DEFAULT_TAX_RATE`, `BULK_QTY_THRESHOLD`, etc.)[cite: 2] | Encapsulation / Clean Code | Ran `python Assignment_03.py` → PASS[cite: 2] |
| 2 | Products stored as raw tuples `("Laptop", 1200.0, "electronics")`[cite: 2] | `Product` class with `name`, `price`, `category`, and `get_tax_rate()`[cite: 2] | Classes / Encapsulation | Ran `python Assignment_03.py` → PASS[cite: 2] |
| 3 | Repeated `if tier == ...` chains for discount rates and point multipliers[cite: 2] | `Customer` base class with `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses | Polymorphism / Inheritance | Ran `python Assignment_03.py` → PASS[cite: 2] |
| 4 | Tuple indices `(0, 1)` and direct product list indexing inside calculations[cite: 2] | `OrderItem` class containing a `Product` instance and `quantity` | Composition (has-a) | Ran `python Assignment_03.py` → PASS[cite: 2] |
| 5 | Monolithic `calc()` function mixing calculations and `print()` statements[cite: 2] | `Order` class with pure methods returning math values and separate `receipt()` formatting method[cite: 2] | Pure functions / Separation of concerns | Ran `python Assignment_03.py` → PASS[cite: 2] |

---

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?[cite: 1]

> Replacing the legacy tuple structures and `if/elif` tier chains with a polymorphic `Customer` family and composed `Order`/`OrderItem` classes improved the codebase the most[cite: 1, 2]. It transformed implicit, fragile data indexing into clear, type-safe object behaviors[cite: 2]. Where keeping the behavior identical forced me to be careful was floating-point arithmetic and string representation—specifically ensuring intermediate discount and tax calculations matched the exact rounding sequence of the original legacy script so `_check()` reported PASS without discrepancies[cite: 2].

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.[cite: 1]

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | *"Identify all magic numbers and global variables in the legacy calc function and define clean, named constants for them."*[cite: 1, 2] | Named top-level constants like `DEFAULT_TAX_RATE`, `BULK_QTY_THRESHOLD`, and `POINTS_DIVISOR`[cite: 1] | Accepted[cite: 1] | Ran `python Assignment_03.py` → PASS[cite: 2] |
| 2 | *"Create a Product class from the raw product tuples, including state validation for price and a method to determine tax based on category."*[cite: 1, 2] | `Product` class with validation in `__init__` and `get_tax_rate()` method[cite: 1] | Edited (added explicit type annotations)[cite: 1] | Instantiated products and verified price validation and tax logic[cite: 1] |
| 3 | *"Refactor the customer tier if/elif discount and points logic into a class hierarchy using polymorphism."*[cite: 1, 2] | Base `Customer` class with 3 subclasses overriding discount and point multiplier calculations[cite: 1] | Accepted[cite: 1] | Tested discount and points returned for each tier[cite: 1] |
| 4 | *"Design OrderItem and Order classes that use composition and provide pure calculation methods separate from receipt printing."*[cite: 1, 2] | `OrderItem` (Product + quantity) and `Order` (Customer + items list) with pure calculation methods and a `receipt()` generator[cite: 1] | Accepted[cite: 1] | Verified that calling `order.receipt()` produces exact legacy character output[cite: 1] |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*[cite: 1]

---

## 4 · Before-you-submit checklist

- [Yes] `python Assignment_03.py` prints **PASS**.[cite: 1, 2]
- [Yes] No tuples / parallel lists left — products, orders, and items are objects.[cite: 1]
- [Yes] No `if tier == ...` chains — tiers are a class family.[cite: 1]
- [Yes] Calculation methods **return** values and do not `print`; printing is separate.[cite: 1]
- [Yes] Constructors validate state; no leftover `global`; magic numbers are named.[cite: 1]
- [Yes] The change table and reflection above are filled in.[cite: 1]
- [Yes] The prompt log is complete and the ownership statement is signed.[cite: 1]
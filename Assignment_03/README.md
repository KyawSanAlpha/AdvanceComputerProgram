Assignment 03 — Refactor Store System

Refactored Python store system for 192-201 Advanced Computer Programming with Generative AI (Siam University).

Overview

Converted legacy Python code into clean Object-Oriented Architecture while maintaining identical output.

Features Applied

Classes & Composition: Product, OrderItem, Customer, and Order objects.

Polymorphism: Subclassed customer tiers (Silver, Gold, Platinum) to remove if/elif chains.

Clean Code: Named constants, constructor state validation, and pure calculation methods separate from receipt printing.

Usage

Run the script to verify the self-test:

python Assignment_03.py


Outputs PASS when refactored output perfectly matches legacy behavior.

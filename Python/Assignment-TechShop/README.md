# 🛒 TechShop Collections Project (Python)

## 📌 Project Overview

This is a **TechShop inventory and order management system** implemented using **Python collections and OOP principles**.

It simulates the core functionalities of a gadget store — including managing products, orders, payments, and inventory — using built-in Python data structures like lists, dictionaries, and custom exceptions.

---

## 🚀 Features Implemented

✅ **Product Management**
- Add, update, and remove products
- Duplicate product handling

✅ **Order Management**
- Add new orders with product details
- Update order statuses (e.g., pending, shipped, canceled)
- Remove canceled orders

✅ **Inventory Management**
- Inventory tracking using `SortedList` concept via Python `dict`
- Automatic stock deduction during order placement
- Exception handling for insufficient stock

✅ **Order Sorting**
- Orders sorted by order date (ascending/descending)

✅ **Product Search**
- Search products by name (case-insensitive)
- Error raised for no match

✅ **Payment Handling**
- Record and update payment status
- Link payments to orders

✅ **Data Integrity**
- Validates product availability in inventory before placing order
- Prevents deleting products involved in existing orders

---

## 📂 Project Structure


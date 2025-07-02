from entity.Product import Product
from entity.Order import Order
from entity.OrderDetail import OrderDetail
from entity.Inventory import Inventory
from entity.Payment import Payment

from exception.DuplicateProductException import DuplicateProductException
from exception.ProductNotFoundException import ProductNotFoundException
from exception.InsufficientStockException import InsufficientStockException
from exception.InvalidSearchCriteriaException import InvalidSearchCriteriaException

from datetime import datetime

# ========== DATA COLLECTIONS ==========
product_list = []
order_list = []
order_detail_list = []
payment_list = []
inventory_dict = {}  # key: product_id, value: Inventory object

# ========== PRODUCT FUNCTIONS ==========

def add_product(product):
    for p in product_list:
        if p.product_id == product.product_id or p.name.lower() == product.name.lower():
            raise DuplicateProductException("Product with same ID or name exists.")
    product_list.append(product)
    print("✅ Product added.")

def update_product(product_id, new_name):
    found = False
    for p in product_list:
        if p.product_id == product_id:
            p.name = new_name
            found = True
            print("✅ Product updated.")
            break
    if not found:
        raise ProductNotFoundException("Product not found.")

def remove_product(product_id):
    for detail in order_detail_list:
        if detail.product_id == product_id:
            raise Exception("❌ Cannot remove: Product has existing orders.")
    global product_list
    product_list = [p for p in product_list if p.product_id != product_id]
    inventory_dict.pop(product_id, None)
    print("✅ Product removed.")

def search_products(keyword):
    results = [p for p in product_list if keyword.lower() in p.name.lower()]
    if not results:
        raise InvalidSearchCriteriaException("No products found.")
    for p in results:
        print(f"{p.product_id}: {p.name} - ₹{p.price}")

# ========== ORDER FUNCTIONS ==========

def add_order(order, order_details):
    # Update inventory
    for detail in order_details:
        if detail.product_id not in inventory_dict:
            raise ProductNotFoundException("Product not in inventory.")
        inv = inventory_dict[detail.product_id]
        if inv.quantity_in_stock < detail.quantity:
            raise InsufficientStockException("Stock too low for product.")
        inv.quantity_in_stock -= detail.quantity
    order_list.append(order)
    order_detail_list.extend(order_details)
    print("✅ Order placed.")

def update_order_status(order_id, new_status):
    for o in order_list:
        if o.order_id == order_id:
            o.status = new_status
            print("✅ Order status updated.")
            return
    print("❌ Order not found.")

def remove_canceled_orders():
    global order_list
    order_list = [o for o in order_list if o.status.lower() != "canceled"]
    print("✅ Canceled orders removed.")

def sort_orders(ascending=True):
    sorted_orders = sorted(order_list, key=lambda o: o.order_date, reverse=not ascending)
    for o in sorted_orders:
        print(f"{o.order_id} - {o.order_date} - {o.status}")

# ========== INVENTORY FUNCTIONS ==========

def update_inventory(product_id, quantity, last_updated):
    inventory_dict[product_id] = Inventory(product_id, quantity, last_updated)
    print("✅ Inventory updated.")

# ========== PAYMENT FUNCTIONS ==========

def record_payment(payment):
    payment_list.append(payment)
    print("✅ Payment recorded.")

# ========== DEMO / TEST DATA ==========

if __name__ == "__main__":
    # Add products
    try:
        add_product(Product(101, "Smartphone", "Android phone", 15000))
        add_product(Product(102, "Laptop", "Gaming laptop", 70000))
        update_inventory(101, 10, "2025-06-30")
        update_inventory(102, 5, "2025-06-30")
    except Exception as e:
        print(e)

    # Search product
    try:
        print("\n🔍 Search Results:")
        search_products("phone")
    except Exception as e:
        print(e)

    # Place order
    try:
        order1 = Order(201, 1, datetime.strptime("2025-07-01", "%Y-%m-%d"))
        details1 = [OrderDetail(301, 201, 101, 2)]
        add_order(order1, details1)
    except Exception as e:
        print(e)

    # Sort orders
    print("\n📅 Sorted Orders:")
    sort_orders(ascending=True)

    # Record payment
    record_payment(Payment(401, 201, 30000, "Paid"))

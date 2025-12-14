def build_sales_log(sales_list):
    my_dict= {}
    for sale in sales_list:
        parts = sale.split("|")
        employee_id = parts[0]
        prices = float(parts[2])
        if employee_id not in my_dict:
            my_dict[employee_id] = 0.0
        my_dict[employee_id]+=prices
    return my_dict
def find_top_performer(sales_dict):
    print("Sales Report:")
    for employee_id, total_price in sales_dict.items():
        print(f"{employee_id}: ${total_price}")
    print("-"*40)
    highest_id = ''
    highest_price = 0.0
    for sales_id in sales_dict:
            current_total = sales_dict[sales_id]
            if current_total>highest_price:
                highest_price = current_total
                highest_id = sales_id
    print(f"Top Performer is {sales_id} with ${highest_price}")

sales_list = [
    "E101|Laptop|1200.00",
    "E102|Mouse|25.50",
    "E101|Monitor|300.00",
    "E103|Headphones|150.00",
    "E102|Keyboard|50.00",
    "E103|Laptop|1000.00",
    "E101|Mousepad|15.00"
]
# print(build_sales_log(sales_list))
find_top_performer(build_sales_log(sales_list))
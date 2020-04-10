__version__ = '0.1.0'


menu = {
    "appetizers": {
        "aings": 0, 
        "cookies": 0, 
        "spring rolls": 0
    },
    "entrees": {
        "salmon": 0, 
        "steak": 0, 
        "meat": 0, 
        "tornado": 0, 
        "a literal garden": 0
    },
    "desserts": {
        "ice cream": 0, 
        "cake": 0, 
        "pie": 0
    },
    "drinks": {
        "coffee": 0, 
        "tea": 0, 
        "unicorn tears": 0
    }
}

welcome_prompt = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""

order_prompt = """
***********************************
** What would you like to order? **
***********************************
"""

def print_welcome():
    print(welcome_prompt)
    
def print_menu():
    for course in menu:
        print(f"\n{course}\n----------")
        for item_name in menu[course]:
            print(to_title_case(item_name))

def print_order_prompt():
    print(order_prompt)

def to_title_case(item):
    return item.title()

def confirm_order(order):
    is_order_in_menu = False
    for course in menu:
        for item in menu[course]:
            if item.lower() == order.lower():
                is_order_in_menu = True
                menu[course][item] += 1
                print(f"\n** {menu[course][item]} order of {item.title()} have been added to your meal **")
                break
    if not is_order_in_menu:
        print(f"\n** Not in the menu **")
    
def main():
    print_welcome() 
    print_menu() 
    input_value = input(order_prompt)
    while input_value != "quit":
        confirm_order(input_value)
        input_value = input(order_prompt)

if __name__ == "__main__":
    main()    
    
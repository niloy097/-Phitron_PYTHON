from menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Checf, Customer, Server, Manager
from Order import Order
def main():
    menu = Menu()
    pizza_1 = Pizza("Sutki Pizza", 600, 'large', ['sutki', 'onion'])
    menu.add_menu_items('pizza', pizza_1)
    pizza_2 = Pizza("Alur Vorta Pizza", 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_items('pizza', pizza_2)
    pizza_3 = Pizza("Dal pizza", 500, 'large', ['dal', 'oil'])
    menu.add_menu_items('pizza', pizza_3)
    
    #add burger to the menue
    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_items('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_menu_items('burger', burger_2)
    
    # add drinks to the menu
    coke = Drinks('Coke', 50, True)
    menu.add_menu_items('drinks', coke)
    coffee = Drinks('Mocha Coffee', 300, False)
    menu.add_menu_items('drinks', coffee)
    
    
    # show Menu
    # menu.show_menu()
    
    restaurant = Restaurant("Sai Baba Restaurant", 2000, menu)
    
    #add employees
    manager = Manager("Kala Chan Manager", 555, 'kalachan@gmail.com', 'kalapur', 1500, 'Jan 1 2020', 'core')
    restaurant.add_employee('manager', manager)
    
    chef = Checf("Rustom Baburchi", 666, 'chupa@gmai.com', 'rustomnagar', 3500, 'Feb 1 2020', 'Chef', 'everything')
    restaurant.add_employee('chef', chef)
    
    server = Server("Chotu server", 777, 'nia@jai.com', 'restaurant', 200, 'March 1 2020', 'server')
    restaurant.add_employee('server', server)
    
    #show employees
    # restaurant.show_employees()
    
    # customer 1 Placing an order
    customer_1 = Customer("Shakib Khan", 5552, 'king@khan.com', 'Bonani', 100000)
    order_1  = Order(customer_1, [pizza_3, coke, burger_1, pizza_3, coffee])
    customer_1.place_order(order_1)
    restaurant.add_order(order_1)
    
    #customer 1 paying for order_1
    restaurant.receive_payment(order_1, 20000, customer_1)
    
    print('Revenue and Balance after first customer', restaurant.revenue, restaurant.balance)
    
    # customer 2 Placing an order
    customer_2 = Customer("Shakib Al Khan", 5552, 'king@khan.com', 'Bonani', 100000)
    order_2  = Order(customer_2, [pizza_1, burger_2, burger_1, pizza_2, coffee])
    customer_2.place_order(order_2)
    restaurant.add_order(order_2)
    
    #customer 1 paying for order_1
    restaurant.receive_payment(order_2, 10000, customer_2)
    
    print('Revenue and Balance after second customer', restaurant.revenue, restaurant.balance)
    
    # pay rent 
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('After Rent', restaurant.revenue, restaurant.balance, restaurant.expense)
    
    #paying salary
    restaurant.pay_salary(chef)
    print('After giving salary', restaurant.revenue, restaurant.balance, restaurant.expense)

# call the main
if __name__ == '__main__':
    main()
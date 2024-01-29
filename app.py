from models import (Base, session, Product, engine)
from datetime import datetime
import csv
import time


def app():
    customer_input = input ('''
    \n**Inventory Management System**
    \rType "v" to view product
    \rType "a" to add product
    \rType "b" to backup inventory
    \rType "exit" to exit
    \r******************************  ''')

    if customer_input.lower() == "v":
        view_product()
    elif customer_input.lower() == "a":
        add_product()
    elif customer_input.lower() == "b":
        backup_file()
    elif customer_input.lower() == "exit":
        exit()
    else: input("That is not a valid answer. Please re read the menu and enter an option from above. Press Enter to try again.  ")

def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        for row in data:
            product_in_db = session.query(Product).filter(Product.product_name == row[0]).order_by(Product.date_updated.desc()).first()
            if product_in_db == None:
                product_name = row[0].replace('"', '')
                product_price = clean_price(row[1])
                product_quantity = clean_quantity(row[2])
                date_updated = clean_date(row[3])
                new_product = Product(product_name = product_name, product_price = product_price,
                                    product_quantity = product_quantity, date_updated = date_updated)
                session.add(new_product)
            elif product_in_db != None:
                if product_in_db.date_updated < clean_date(row[3]):
                    product_in_db.date_updated = clean_date(row[3])
                    product_in_db.product_price = clean_price(row[1])
                    product_in_db.product_quantity = clean_quantity(row[2])
            session.commit()
            

def create_list():
    all_info = session.query(Product).all()
    product_list = []
    for item in all_info:
        product_dict = {'Product ID' : item.product_id,
                        'Product Name' : item.product_name,
                        'Product Price' : item.product_price,
                        'Product Quantity' : item.product_quantity,
                        'Date Updated' : item.date_updated
                        }
        product_list.append(product_dict)
    return(product_list)

def clean_price(price_string):
    try:cleaned_price = int(float(price_string.replace('$', '')) * 100)
    except:
        input('''
        \n******Price Error**********
        \rPlease input a valid price
        \rPress Enter to try again''')
    else:
        return cleaned_price

def clean_quantity(quantity_string):
    try:
        cleaned_quantity = int(quantity_string)
    except:
        input('''
        \n *****Quantity Error*****
        \rEnter a numerical value
        \rusing WHOLE numbers!
        \rPress Enter to try again''')
    else:
        return cleaned_quantity
        
def clean_date(date_string):
    date_format = '%m/%d/%Y'
    cleaned_date = datetime.strptime(date_string, date_format).date()
    return cleaned_date

def view_product():
    products = session.query(Product.product_id, Product.product_name).all()
    for product in products:
        print(f"{product.product_id}: {product.product_name}")
    print("\n")
    app_running = True
    while app_running:
        try:
            product_number = input('''Which product would you like more information about??
                                    \rType 'menu' to go back!
                                    \rType 'print' to reprint list!
                                    \rOr enter number HERE ----- >  ''')

            if product_number.lower() == "menu":
                app_running = False
            elif product_number.lower() == "print":
                products = session.query(Product.product_id, Product.product_name).all()
                for product in products:
                    print(f"{product.product_id}: {product.product_name}")
                print("\n")
            else:
                query = session.query(Product).filter(Product.product_id == product_number).first()
                print(f"\n**** There are {query.product_quantity} units of {query.product_name} in stock at a price of ${query.product_price / 100:.2f} each! This is as of {query.date_updated} ****\n")
        except: 
            print("That is not a valid option, please read the list/menu above and try again\n")
    app()

def add_product():
    add_name = input("What is the name of your product? Example: Juice - V8 Splash.  ")
    add_price = input("What is the current price of this product? Example : $5.23  ")
    add_quantity = input("How many units are you adding to inventory? Example : 32  ")

    add_product = Product(product_name=(add_name), product_price = clean_price(add_price), product_quantity = clean_quantity(add_quantity), date_updated = (datetime.now))
    session.add(add_product)
    session.commit()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    

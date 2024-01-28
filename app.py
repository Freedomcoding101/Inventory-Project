from models import (Base, session, Product, engine)
from datetime import datetime
import csv
import time

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

    for item in all_info:
        product_list = []
        product_dict = {'Product ID' : {item.product_id},
                        'Product Name' : {item.product_name},
                        'Product Price' : {item.product_price},
                        'Product Quantity' : {item.product_quantity},
                        'Date Updated' : {item.date_updated}
                        }
        product_list.append(product_dict)
        print(product_list)


def clean_price(price_string):
    try:cleaned_price = int(float(price_string.replace('$', '')) * 100)
    except:
        input('''
        \n *****Price Error*****
        \rPlease input a valid price
        \rPress Enter to try again
        *******''')
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
        \rPress Enter to try again
        *******''')
    else:
        return cleaned_quantity
        
def clean_date(date_string):
    date_format = '%m/%d/%Y'
    cleaned_date = datetime.strptime(date_string, date_format).date()
    return cleaned_date

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    

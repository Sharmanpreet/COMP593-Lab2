from sys import argv, exit
import os
from datetime import date

def get_sales_csv():

    # Check whether command line parameters was provided
    if len(argv >= 2):
        sales_csv = argv[1]

        # Check whether the CSV path is an existing file
        if os.path.isfile(sales_csv):
            return sales_csv
        else:
            print('Error: CSV file does not exist')  
            exit('Script execution aborted')  
    else:
        print('Error: No CSV file path provided')
        exit('Script execution aborted')

def get_order_dir(sales_csv):

    # Get directory path of sales data CSV file
    sales_dir = os.path.dirname(sales_csv)

    # Determine orders directory name (Orders_YYYY-MM-DD)
    todays_date = date.today().isoformat()
    order_dir_name = 'Orders_' + todays_date

    # Build the full path of the orders directory
    order_dir = os.path.join(sales_dir, order_dir_name)

    # Make the orders directory if it does not already exist
    if not os.path.exists(order_dir):
        os.makedirs(order_dir)

    return order_dir    


sales_csv = get_sales_csv()
order_dir = get_order_dir(get_order_dir)

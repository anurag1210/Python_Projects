import datetime
import random
import sys
import time
import requests

url = 'https://api.exchangerate.host/live?access_key=272d8a20da846218e259d85d8bc3e35e'


def open_account(user_name,opening_balance):
     account_opening_date=datetime.datetime.now()
     print(f'Welcome {user_name} to Zenna Bank')
     print(f'This is your account balance ${opening_balance:.2f} on your account opening date {account_opening_date}')
     user_choice=input('Do you want to check your account balance ? Choose [Y] or [N] :')
     if user_choice =='Y':
         check_balance(opening_balance)
     else:
         print('okay seems you want to puchase an item ! please go ahead to purchase the item !')
         purchase_item(item_cost,opening_balance_us_dollars,user_name,item_name)


def purchase_item(item_cost,opening_balance,user_name,item_name):
    purchase_reference=random.randint(1000,50000)
    print(f'This is the ${item_cost} of the item name {item_name} purchased whose reference number is {purchase_reference}')
    print('Please allow a moment for the transaction to process through')
    time.sleep(3)
    if opening_balance >= item_cost:
        new_balance=(opening_balance-item_cost)
        check_balance(new_balance)
    else:
        print(f'You dont have sufficient balance in your account Mr {user_name}')


def check_balance(opening_balance):
    print(f'The balance of your bank account is ${opening_balance} at the moment of {datetime.datetime.now()}')
    print(f'Have a great day {user_name} !')



def currency_conversion(opening_balance):
    response = requests.get(url)
    data = response.json()
    converted_value = data['quotes']['USDGBP']
    print(f'The current USD to GBP conversion rate is {converted_value}')
    opening_balance_us_dollars = opening_balance * converted_value
    return opening_balance_us_dollars



if __name__ == "__main__":
    user_name = input('What is the account holder''s name:')
    if user_name.isalpha():
        opening_balance = float(input('How much would you like to deposit on your bank account, please input a number:'))
        currency=input('Is the amount input a U.S dollar or a British pound ?, Currently only two currencies are allowed in the Zenna Bank Choose [GBP] or [USDollar] :')
        item_name = input('What is the item you need to purchase: ')
        item_cost = float(input('What is the price of the item  in USDollars : '))
        if currency=='USDollar':
            print('No currency conversion required we accept USDollar $')
            open_account(user_name, opening_balance)
        else:
            print('GBP to US Dollar currency conversion required')
            opening_balance_us_dollars=currency_conversion(opening_balance)
            open_account(user_name, opening_balance_us_dollars)
    else:
         print('Invalid input, exiting the program')
         sys.exit()


purchase_item(item_cost,opening_balance_us_dollars,user_name,item_name)
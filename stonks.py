#!/usr/bin/env python3

def calc_actual_gain(cost_of_stock, purchased_number_shares):
    actual_gain = price - cost_of_stock

def calc_purchased_shares(purchased_usd_amount, stock_purchase_price):
    purchased_shares_amount = purchased_usd_amount / stock_purchase_price
    return purchased_shares_amount
    
def calc_potential_gains(current_stock_price, purchased_number_shares, cost_of_stock):
    potential_gains = (purchased_number_shares * current_stock_price) - cost_of_stock
    return potential_gains

def stock_cost(stock_purchase_price, purchased_number_shares):
    cost_of_stock = stock_purchase_price * purchased_number_shares
    return cost_of_stock
    
try:
    current_stock_price = float(input("Enter current price of stock in USD: "))
    stock_purchase_price = float(input("Enter price at which stock was purchased: "))
    purchased_usd_amount = float(input("Enter amount in USD that is being purchased: "))
    
    purchased_number_shares = calc_purchased_shares(purchased_usd_amount, stock_purchase_price)
    cost_of_stock = stock_cost(stock_purchase_price, purchased_number_shares)
    total_current_stock_value = purchased_number_shares * current_stock_price
    net_gain = total_current_stock_value - cost_of_stock
    
    print("Number of shares purchased:", purchased_number_shares)
    print("Cost of stock was:", cost_of_stock)
    print("Total current stock value:", total_current_stock_value)
    print("Net gain:", net_gain)
    
except:
    print("Enter a valid integer")

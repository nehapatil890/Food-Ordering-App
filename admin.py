# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:59:55 2022

@author: HP
"""


admin_keys={"amruta":"amruta@345"}
inven={1:{"itemname":"pavbhaji","itemid":1,"price":250,"stock":14,"discount":12,"quantity":'300gm'},
       2:{"itemname":"cake","itemid":2,"price":150,"stock":20,"discount":13,"quantity":'400gm'},
       3:{"itemname":"paneer tikka","itemid":3,"price":350,"stock":7,"discount":14,"quantity":'2gm'},
       4:{"itemname":"dal fry",'itemid':4,"price":200,'stock':8,"discount":30,"quantity":'50gm'},
       5:{"itemname":"Tandori chicken","itemid":8,"quantity":"4 pices","discount":11,"price":240},
       6:{"itemname":"vegan burger","itemid":11,"quantity":"1 piece","discount":15,"price":320}}


def add_new_item():
  itemname=input("Enter the item name:")
  itemid=int(input("enter the itemid:"))
  price=int(input("Enter the price of the item:"))
  stock=int(input("Enter the stock value of item:"))
  quantity=int(input("Enter the quantity value of item:"))
  discount=int(input("Enter the discount value of item:"))
  
  inven[itemid]={"itemname":itemname,"itemid":itemid,"price":price,"stock":stock,"quantity":quantity,"discount":discount}
  print(f"the item{itemname}is successfully added")
  return inven
def edit_from_item():
  item=int(input("enter the itemid which you want to edit:"))
  a=input("Enter the item name:")
  b=input(input("Enter the price of item:"))
  c=int(input("Enter the stock of item:"))
  inven[item]["itemname"]=a
  inven[item]["price"]=b
  inven[item]["stock"]=c
  print('Edited item successfully')
  return inven

def price_cal(item):
    item = int(input("Enter item:"))
    k= inven[dish]["price"]
    d= inven[dish]["discount"]
    n= k-(k*d/100)
    return n
  
def show_inven():
  print("here us the inventory of sukhkarta ")
  for i in inven:
    print('itemName:',inven[i]["itemname"])
    print('price:',inven[i]['price'])
    print("itemid:",inven[i]["itemid"])
    print("quantity:",inven[i]["quantity"])
    print("discount:",inven[i]["discount"])
    
def remove_item():
  d=int(input("enter the itemid which you want to exit"))
  inven.pop(d)
  print("remove item successfully")
  return inven



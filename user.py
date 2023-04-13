# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:12:46 2022

@author: HP
"""

import admin as ad
class user:
  login_info={"Neha":"Neha@7517"}
  def __init__(self,name,phoneno,email,address,password):
    self.name=name
    self.number=phoneno
    self.email=email
    self.address=address
    self.password=password
    user.login_info[self.name]=self.password
    self.profile={'name':name}
    self.order_history={}
  @classmethod
  def login(cls,username,password):
    if cls.login_info.get(username)==password:
      print("You are successfully logged in...")
      return True
    else:
      print("sorry!there are the wrong credential!!!")
  def place_order(self):
    print("What you want to order here in the Inventory")
    print(ad.show_inven())
    user_choice=int(input("If you want to order the select 1.yes 2.No"))
    if user_choice==1:
      n=int(input('enter how many items do you want to order'))
      x=0
      for i in range(n):
        itemid=int(input("Enter the itemid here"))
        quan=int(input("Enter the quantity of the item:"))
        price=ad.price_cal(itemid)
        print(price)
        x+=ad.inven[itemid]['price']*quan
      again_ask=input("are you still want to orderthis enter Yes or No")
      if again_ask=="Yes":
        print(f,'''your item name is {ad.inven[itemid]['Itemname']}''')
        print(f,'''price of your item is {ad.inven[itemid]['price']}''')
        print(f,'''this is your quantity{quan}''')
        print(f,'''It costs you {x}INR in total''')
        print(f,'''you are all set for this order''')
        self.order_history[itemid]={
            "itemname":ad.inven[itemid]["itemname"],
            "price":ad.inven[itemid]['price'],
            "quantity":quan
        }
        final_stock=ad.inven[itemid]['stock']-quan
        ad.inven[itemid]['stock']-final_stock
        print('Your order is successfully placed')
      elif again_ask=='No':
        print("This order is cancelled!!You can look once more")
      else:
        print("Invalid choice")
    elif user_choice==2:
      print("you select 2 option so we cancelled this")
    else:
      print('Enter the invalid choice')
  def display(self):
            print("name:",self.name)
            print("number:",self.number)
            print("email:",self.email)
            print("address:",self.address)
            print("password:",self.password)
            print("login_info:",user.login_info)


  def account_register():
    cs = user(input("name: "),int(input("enter phoneno: ")),input("email_id: "),input("enter_adress: "),input("enter password: "))
    return cs.display()

  def account_update():
    cs = user(input("name: "),int(input("enter phoneno: ")),input("email_id: "),input("enter_adress: "),input("enter password: "))
    return cs.display()
  




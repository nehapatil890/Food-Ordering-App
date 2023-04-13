# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 13:20:28 2022

@author: HP
"""

import admin as aa
from user import user
uhh=user(str,str,str,str,str)
inp=int(input('where you want to login select 1.admin 2.user 3.Exit'))
if inp==1:
  username=input('Enter the username of admin:')
  password=input("enter the password of admin")
  if aa.admin_keys[username]==password:
    print('***you are successfully logged in****')
    admin_crawler=True
    while admin_crawler:
      adm_choice=int(input("choose the options of admin pannel 1.Add new item,2.Edit item,3.list the item,4.Remove item, 5.Exit"))
      if adm_choice==1:
        aa.add_new_item()
      elif adm_choice==2:
        aa.edit_from_item()
      elif adm_choice==3:
       aa.show_inven()
      elif adm_choice==4:
        aa.remove_item()
      elif adm_choice==5:
        print(f"you are exit to the admin pannel{username}")
        admin_crawler=False
      else:
        print("This is the wrong selection please select valid option:")
  else:
    print("This is the wrong credentials!SORRY!!!")
elif inp==2:
  print("welcome to the user dashboard,Register yourself")
  user.account_register()
  print("welcome to the user panel")
  username=input('Enter the username of user:')
  password=input("enter the password of user:")
  if user.login(username,password):
      print(f'you are successfully logged in {username}****')
      user_crawler=True
      while user_crawler:
        user_choice=int(input(f"{username},choose the options 1.place new order 2.Order history 3.exit:"))
        if user_choice==1:
          uhh.place_order()
        elif user_choice==2:
          print(f"Here is your order history, {username}")
          uhh.order_history()
           
        elif user_choice==3:
           user_crawler=False
          
        
        else:
          print("You are successfully logged out")
          
  else:
    print("This is the wrong credentials!SORRY!!!")
    
else:
  exit()


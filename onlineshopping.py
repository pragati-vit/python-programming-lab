from easygui import *
import sys

while 1:
    msgbox("Welcome to online shopping")

    msg =("Which site would you prefer?")
    title =("Online diwali shopping")
    choices =["amazon","flipkart","myntra","snapdeal"]
    choice = choicebox(msg,title,choices)
 if Choice=="amazon":
    print(continue):
    msg1 ="What do you want on this diwali?"  
    title1 ="Online diwali shopping"
    choices1 =["electronics","fashion","home and furniture","tv","toys","clothes")
    choice1 =choicebox(msg1,title1,choices1)
 if Choices1=="electronics":
        
    msgbox("you chose:" +str(choice),"Survey Result")
 
    msg ="Do you want to continue?"
    title ="Please confirm"
 if ccbox(msg, title):
     pass
 else:
      sys.exit(0)

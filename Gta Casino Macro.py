import time
import random
from pynput.keyboard import Key,Controller
from colorama import Fore

time.sleep(1)
keyboard = Controller()
test = 0
spins = 0
tijd = 0
aantal_spins = 0
aantal_gedaan = 0
money = 0
money_done = 0
wins = 0
keuze = 0
keuze2 = 0

tekst1 = ("""
    _____                                __           
   /     |                              /  |          
   $$$$$ |  ______    ______    ______  $$/   ______  
      $$ | /      \  /      \  /      \ /  | /      \ 
 __   $$ | $$$$$$  |/$$$$$$  |/$$$$$$  |$$ |/$$$$$$  |
/  |  $$ | /    $$ |$$ |  $$ |$$ |  $$ |$$ |$$    $$ |
$$ \__$$ |/$$$$$$$ |$$ |__$$ |$$ |__$$ |$$ |$$$$$$$$/ 
$$    $$/ $$    $$ |$$    $$/ $$    $$/ $$ |$$       |
 $$$$$$/   $$$$$$$/ $$$$$$$/  $$$$$$$/  $$/  $$$$$$$/ 
                    $$ |      $$ |                    
                    $$ |      $$ |                    
                    $$/       $$/                     \n""")
print(Fore.BLUE + tekst1)
print(Fore.GREEN + "simple gta macro made by bruhjasper#0001\n\n")


keuze = input(Fore.WHITE + "always lose macro = 1\nsometimes win macro = 2\nmake a choise: ")
if keuze == "1":
    while test == 0:
        wachtijd = random.randint(1, 9)
        sleep = str("5.")+str(wachtijd)
        time.sleep(float(sleep))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        spins += 1
        tijd += float(sleep)
        print(Fore.RED + "spins: "+str(spins)+"   total time: "+str(tijd)+"   time waited: "+str(sleep))
        continue
if keuze == "2":
    time.sleep(1)
    while True:
        money = input("How much money, already in million.   Type 0 if you want unlimited:  ")
        if money.isdigit():
            money = int(money)
        else:
            print("type a full number")
            continue
        
        confirm = input(str(money)+" mil   is this right? yes/no:  ")
        if confirm == "yes":
            break
        else:
            continue

    while True:
        range1 = 0
        range2 = 0
        print("Sometimes the number wont work, try other numbers then")
        range1 = input("minimal number of spins = ")
        range2 = input("maximal number of spins = ")
        if range1>range2 or range1 == range2:
            print("Range1 is bigger/even then range2")
            continue

        if range1.isdigit():
            range1 = int(range1)
        else:
            print("range1 is not a full number")
            continue

        if range2.isdigit():
            range2 = int(range2)
            
        else:
            print("range2 is not a full number")
            continue
        
        break

    print("macro starting")
    time.sleep(5)
    aantal_spins = random.randint(range1, range2)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(1)

    while float(money_done) < float(money) or money == 0:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        wachtijd = random.randint(1, 9)
        sleep = str("5.")+str(wachtijd)
        time.sleep(float(sleep))
        aantal_gedaan += 1
        spins += 1
        tijd = (int(wins)*7)+(int(spins)*5)

        print(Fore.RED + "\ndone_spins = "+str(aantal_gedaan)+"   goal_spins = "+str(aantal_spins)+"   money_goal = "+str(money)+" mil"+"   money_done = "+str(money_done)+"   waittime = "+str(sleep)+" s"+"   total time = "+str(tijd)+"s")
        if aantal_gedaan < aantal_spins:
            continue
        else:
            time.sleep(1)
            print("spins done, winning...")
            keyboard.press(Key.up)
            keyboard.release(Key.up)
            keyboard.press(Key.f1)
            keyboard.release(Key.f1)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(1)
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            keyboard.press(Key.f1)
            keyboard.release(Key.f1)
            wins += 1
            money_done += 2.5
            aantal_spins = 0
            aantal_gedaan = 0
            aantal_spins = random.randint(range1, range2)
            time.sleep(7)
else:
    print("wrong input")
    exit()

time.sleep(1)
print(Fore.GREEN + "\n\ndone\nmade "+str(money_done)+" million in "+str(tijd)+" seconds")
print(Fore.RED + "closing...")
time.sleep(10)
print(Fore.RED + "done")


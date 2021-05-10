from tkinter import Tk
from tkinter import filedialog
from colorama import Fore
import os
from tqdm import tqdm

os.system("cls" or "clear")

choice = 0
combolist_path_list = []
setofCombos = set()
amt_combos = 0

def select_combolists():
    Tk().withdraw()
    amt_combolist = 0
    #setofCombos.clear()
    finished_loading_combolist = False
    while finished_loading_combolist == False:
        print(Fore.YELLOW + "How many combolists are you wanting to combine and filter?" + Fore.WHITE)
        try:
            amt_combolist = int(input(Fore.LIGHTCYAN_EX + "Amount: " + Fore.WHITE))
            if amt_combolist > 20:
                continue
            if amt_combolist < 0:
                continue
        except ValueError:
            print("Please input a number up to 20")
            continue
        
        print(f'{Fore.LIGHTGREEN_EX}Amount of combolists: {amt_combolist}{Fore.WHITE}')
        finished_loading_combolist = True
        print(Fore.YELLOW + "Select your combolists!" + Fore.WHITE)

        for i in range(0, amt_combolist):
            i =  filedialog.askopenfilename(initialdir = "", title = "Select file", filetype=(("text file", "*.txt"), ("all files", "*.*")))
            os.system("cls" or "clear")
            print (i)
            if i != "":
                if i not in combolist_path_list:
                    combolist_path_list.append(i)
                else:
                    print(Fore.RED + "Please only choose one of each combolist" + Fore.WHITE)
                    pass
        print(f'{Fore.LIGHTMAGENTA_EX}All combolists: {combolist_path_list}{Fore.WHITE}')
        print(Fore.LIGHTGREEN_EX + "Finished Loading Combolists." + Fore.WHITE)
    return combolist_path_list

def combine_combolists():
    os.system("cls" or "clear")
    amt_duplicates = 0
    amt_combos = 0
    for combolist in combolist_path_list:
        try:
            loaded_combolist = open(f'{combolist}', 'r', encoding='UTF-8', errors='ignore')
        except FileNotFoundError:
            continue

        for comboline in tqdm(loaded_combolist):#here's tqdm
            try:
                comboline_fixed = comboline.strip('\n')
                #comboline_fixed.decode('utf-8', errors='ignore').encode('utf-8')
                if comboline_fixed in setofCombos:
                    #print(f'{comboline_fixed} is a duplicate!')
                    amt_duplicates = amt_duplicates + 1
                    pass
                else:
                    setofCombos.add(comboline_fixed)
                    #print(f'added: {comboline}')
                    amt_combos = amt_combos + 1
            except (UnicodeDecodeError, UnicodeError):
                pass

        loaded_combolist.close

    print(Fore.LIGHTGREEN_EX + "Finished" + Fore.WHITE)
    print(f'{Fore.LIGHTMAGENTA_EX}---> {Fore.LIGHTCYAN_EX}{amt_duplicates}{Fore.LIGHTMAGENTA_EX} <--- duplicates were removed{Fore.WHITE}')
    print(f'{Fore.LIGHTMAGENTA_EX}---> {Fore.LIGHTCYAN_EX}{amt_combos}{Fore.LIGHTMAGENTA_EX} <--- new combos are in the updated combolist{Fore.WHITE}')
    
    return amt_combos
    #print(setofCombos)

def save_new_combolist(amt_combos):
    os.system("cls" or "clear")
    filename = 'GothScript - ' + str(amt_combos) + ' combos - @ (Cracked.to)'
    print(f'{Fore.YELLOW}Saving: {Fore.LIGHTCYAN_EX}{amt_combos} {Fore.YELLOW}combos to file: {Fore.LIGHTCYAN_EX}{filename}.{Fore.WHITE}')
    #print(f'{Fore.LIGHTGREEN_EX}Finished Saving: {Fore.LIGHTCYAN_EX}{amt_combos} {Fore.LIGHTGREEN_EX}combos to file: {Fore.LIGHTCYAN_EX}{filename}.{Fore.WHITE}')
    try:
        new_save_file = open(f'{filename}.txt', 'w+', encoding='UTF-8-sig')
        for line in setofCombos:
            new_save_file.write(f'{line}\n')
        print(f'{Fore.LIGHTGREEN_EX}Finished Saving: {Fore.LIGHTCYAN_EX}{amt_combos} {Fore.LIGHTGREEN_EX}combos to file: {Fore.LIGHTCYAN_EX}{filename}.{Fore.WHITE}')
    except FileExistsError:
        print(Fore.RED + "Couldn't Save file." + Fore.WHITE)
        pass
    #print(Fore.LIGHTGREEN_EX + "Finished saving." + Fore.WHITE)

while choice != 4:
    text = f'\nLoaded Combolists: {len(combolist_path_list)}'
    if len(combolist_path_list) == 0:
        print(Fore.LIGHTRED_EX + text + Fore.WHITE)
    else:
        print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)
    print(Fore.YELLOW+"1 - Select Combolist\n2 - Combine Combolists & Remove Duplicates\n3 - Save New Combolist\n4 - Exit"+Fore.WHITE)

    try:
        choice = int(input(Fore.LIGHTCYAN_EX + "Choice: "+ Fore.WHITE))
        os.system("cls" or "clear")
    except ValueError:
        os.system("cls" or "clear")
        print("Please input a choice 1-4!")
        continue

    if choice == 1:
        print("Selecting Combolists...")#Select combolist(s)
        select_combolists()
    elif choice == 2:
        print(Fore.YELLOW + "Combining Combolists & Removing Duplicate Entries" + Fore.WHITE)#Loop through and check for duplicates
        amt_combos = combine_combolists()
    elif choice == 3:
        if amt_combos == 0:
            print("Please load a combolist before exporting.")
        else:
            print("Saving Combolists") #Save the new combolist
            save_new_combolist(amt_combos)
    elif choice == 4:
        print("Exiting the program...")
        break
    else:
        print("Please input a choice 1-4!")
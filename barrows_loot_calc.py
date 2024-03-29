# imports
import random
import time

# constants
BROTHERS_LIST = ["Torag", "Dharok", "Ahrim", "Guthan", "Karil", "Verac"]
AHRIM_LOOT = ["Ahrim's Hood", "Ahrim's Robetop", "Ahrim's Robeskirt", "Ahrim's Staff"]
DHAROK_LOOT = ["Dharok's Helm", "Dharok's Platebody", "Dharok's Platelegs", "Dharok's Greataxe"]
GUTHAN_LOOT = ["Guthan's Helm", "Guthan's Platebody", "Guthan's Chainskirt", "Guthan's Warspear"]
KARIL_LOOT = ["Karil's Coif", "Karil's Leathertop", "Karil's Leatherskirt", "Karil's Crossbow"]
TORAG_LOOT = ["Torag's Helm", "Torag's Platebody", "Torag's Platelegs", "Torag's Hammers"]
VERAC_LOOT = ["Verac's Helm", "Verac's Brassard", "Verac's Plateskirt", "Verac's Flail"]
DIFFICULTY_MOD = {"Coin_Diff": 2.03, "Mind_Diff": 1.5, "Chaos_Diff": 4.5, "Death_Diff": 9.15, "Blood_Diff": 20.44, "Bolt_Diff": 25.14}

# for saving multiple sims loot
s_save_loot = []
s_coin_amt, s_mind_rune_amt, s_chaos_rune_amt, s_death_rune_amt, s_blood_rune_amt, s_bolt_amt = 0, 0, 0, 0, 0, 0
multi_input = 0

# functions
def add_loot_and_rwd_potential(brother_name, list_const, reward): # add loot to table, calc rwd potential
    global rwd_potential
    if brother_name in bros_killed_list:
        for x in list_const:
            item_rwd_list.append(x)
        rwd_potential = rwd_potential + reward

def roll_for_runes(min_roll, roll, max_roll, ratio): # roll for rune amts
    if max_roll >= roll >= min_roll:
        if diary_flag:
            roll += (roll * 0.5)
        return roll / ratio
    else:
        return 0

def add_to_chest(amt, title, save = 0): # add item to final chest
    if amt != 0:
        amt = int(amt)
        if save == 0:
            final_loot_list.append(str(amt) + " " + title)
        else:
            s_save_loot.append(str(amt) + " " + title)

def add_to_save_loot(): # add items to saved loot
    add_to_chest(s_coin_amt, "Coins", 1) # add coins
    add_to_chest(s_mind_rune_amt, "Mind Runes", 1) # add mind runes
    add_to_chest(s_chaos_rune_amt, "Chaos Runes", 1) # add chaos runes
    add_to_chest(s_death_rune_amt, "Death Runes", 1) # add death runes
    add_to_chest(s_blood_rune_amt, "Blood Runes", 1) # add chaos runes
    add_to_chest(s_bolt_amt, "Bolt Racks", 1)

def repeat_simulation(bros_killed_list, item_rwd_list, rwd_potential, diary_flag, save = 0): # funct for performing multiple sims
    def r_roll_for_runes(min_roll, roll, max_roll, ratio):
        if max_roll >= roll >= min_roll:
            if diary_flag:
                roll += (roll * 0.5)
            return roll / ratio
        else:
            return 0
    def r_add_to_chest(amt, title):
        if amt != 0:
            amt = int(amt)
            r_final_loot_list.append(str(amt) + " " + title)
    
    for x in range(1, len(bros_killed_list) + 2): # add items to loot table
        r_item_roll = 0
        r_items_loot = 450 - (58 * len(bros_killed_list)) # calculating barrows item chance
        r_item_roll = random.randint(1, r_items_loot) # roll for chance
        if r_item_roll == 1: # award barrows loot
            r_reward_item = item_rwd_list[random.randint(0, len(item_rwd_list) - 1)] # roll for item
            if r_reward_item not in r_final_loot_list: # can't have same item in chest twice
                r_final_loot_list.append(r_reward_item)
                if save == 1:
                    s_save_loot.append(r_reward_item)
        else:
            r_misc_roll = 0
            r_misc_roll = random.randint(1, rwd_potential) # roll for misc loot
            r_mind_rune_amt += r_roll_for_runes(381, r_misc_roll, 505, DIFFICULTY_MOD["Mind_Diff"]) # roll mind runes
            if save == 1:
                s_mind_rune_amt = s_mind_rune_amt + int(r_mind_rune_amt)
            r_chaos_rune_amt += r_roll_for_runes(506, r_misc_roll, 630, DIFFICULTY_MOD["Chaos_Diff"]) # roll chaos runes
            if save == 1:
                s_chaos_rune_amt = s_chaos_rune_amt + int(r_chaos_rune_amt)
            r_death_rune_amt += r_roll_for_runes(631, r_misc_roll, 755, DIFFICULTY_MOD["Death_Diff"]) # roll death runes
            if save == 1:
                s_death_rune_amt = s_death_rune_amt + int(r_death_rune_amt)
            r_blood_rune_amt += r_roll_for_runes(756, r_misc_roll, 880, DIFFICULTY_MOD["Blood_Diff"]) # roll blood runes
            if save == 1:
                s_blood_rune_amt = s_blood_rune_amt + int(r_blood_rune_amt)
            if 380 >= r_misc_roll >= 1: # roll for coins
                r_coin_amt += (r_misc_roll * DIFFICULTY_MOD["Coin_Diff"])
                if save == 1:
                    s_coin_amt = s_coin_amt + int(r_coin_amt)
            elif 881 >= r_misc_roll >= 1005: # roll bolt racks
                r_bolt_amt += (r_misc_roll / DIFFICULTY_MOD["Bolt_Diff"])
                if save == 1:
                    s_bolt_amt = s_bolt_amt + int(r_bolt_amt)
            elif 1006 >= r_misc_roll >= 1011: # roll key half
                r_key_roll = random.randint(1, 2)
                if r_key_roll == 1:
                    r_lh_key_flag = True
                else:
                    r_th_key_flag = True
            elif r_misc_roll == 1012:
                r_d_med_flag = True
        
    # add misc items to loot list
    r_add_to_chest(r_coin_amt, "Coins") # add coins
    r_add_to_chest(r_mind_rune_amt, "Mind Runes") # add mind runes
    r_add_to_chest(r_chaos_rune_amt, "Chaos Runes") # add chaos runes
    r_add_to_chest(r_death_rune_amt, "Death Runes") # add death runes
    r_add_to_chest(r_blood_rune_amt, "Blood Runes") # add chaos runes
    r_add_to_chest(r_bolt_amt, "Bolt Racks") # add chaos runes
    if r_lh_key_flag:
        r_final_loot_list.append("Loop Half of Key") # add key loop half
        if save == 1:
            s_save_loot.append("Loop Half of Key")
    elif r_th_key_flag:
        r_final_loot_list.append("Tooth half of Key") # add key tooth half
        if save == 1:
            s_save_loot.append("Tooth half of Key")
    if r_d_med_flag:
        r_final_loot_list.append("Dragon Med Helm")
        if save == 1:
            s_save_loot.append("Dragon Med Helm")

    # add clue scroll to loot
    r_clue_chance = random.randint(1, int(200 / len(bros_killed_list)))
    if r_clue_chance == 1:
        r_final_loot_list.append("Clue Scroll (elite)")

    # print final chest
    if save == 0:
        print(f"Your chest contains: {r_final_loot_list}")

def brothers_inputs(bros_killed_list):
    bros_killed_loop = True
    bros_list_in = ""
    # barrows brothers killed input loop
    print("Which Barrows brothers have you killed?")
    while(bros_killed_loop):
        bros_list_in = str(input("\nType one brothers name, all for all brothers, none, or done: "))
        if bros_list_in == str("none").lower().strip(): # if none end loop
            bros_killed_loop = False
        elif bros_list_in == str("done").lower().strip(): # if done end loop
            bros_killed_loop = False
        elif bros_list_in == "all":
            for x in BROTHERS_LIST:
                bros_killed_list.append(x.capitalize())
            bros_killed_loop = False
        elif bros_list_in.capitalize() not in BROTHERS_LIST: # if input not brother, print
            print("Not an acceptible input.")
        elif bros_list_in.capitalize() in bros_killed_list: # if already input, print
            print("You have already input this brother.")
        else: # if valid input, add to list, print list, restart
            bros_killed_list.append(bros_list_in.capitalize())
            print("You have input the following brothers: ")
            print(f"{', '.join(map(str, bros_killed_list))}")
        if len(bros_killed_list) == 6: # end loop if all six brothers added manually
            bros_killed_loop = False
    return bros_killed_list

def rwd_inputs(rwd_potential):
    rwd_loop = True
    rwd_in = ""
    # rewards potential input loop
    print("\nWhat is your reward potential?")
    while(rwd_loop):
        try: # catching input exception if not valid float
            rwd_in = float(input("Type number without '%' sign: "))
        except ValueError:
            print("Invalid input.")
            continue
        if (rwd_in < 0) or (rwd_in > 100): # if outside range, print
            print("Invalid value.")
        else: # if valid input, add to reward potential, end loop
            rwd_potential += int(rwd_in) * 10
            rwd_loop = False
        return rwd_potential

def diary_inputs():
    diary_loop, diary_flag = True, False
    diary_in = ""
    # morytania hard diary completion flag
    print("\nHave you completed the Morytania Hard diaries?")
    while(diary_loop):
        diary_in = str(input("Type Y or N: "))
        if (diary_in.lower() != "y") and (diary_in.lower() != "n"): # if not valid input
            print("Invalid input.")
        elif diary_in.lower() == "y":
            diary_flag = True
            diary_loop = False
        return diary_flag

def get_inputs(bros_killed_list, rwd_potential):
    brothers_inputs(bros_killed_list)
    rwd_inputs(rwd_potential)
    diary_inputs()
    
# main sim prgm
def main(save = 0):
    total_loop = True
    while total_loop: # main prgm loop

        # global variabes
        global s_coin_amt, s_mind_rune_amt, s_chaos_rune_amt, s_death_rune_amt, s_blood_rune_amt, s_bolt_amt
        global s_save_loot

        # resettable variablesstart_over_loop = True, True
        d_med_flag, lh_key_flag, th_key_flag = False, False, False
        bros_killed_list, item_rwd_list, final_loot_list = [], [], []
        rwd_in = 0.0
        rwd_potential, misc_roll = 0, 0
        coin_amt, mind_rune_amt, chaos_rune_amt, death_rune_amt, blood_rune_amt, bolt_rack_amt = 0, 0, 0, 0, 0, 0

        # flag and loot table functions
        add_loot_and_rwd_potential("Torag", TORAG_LOOT, 115)
        add_loot_and_rwd_potential("Dharok", DHAROK_LOOT, 115)
        add_loot_and_rwd_potential("Ahrim", AHRIM_LOOT, 98)
        add_loot_and_rwd_potential("Guthan", GUTHAN_LOOT, 115)
        add_loot_and_rwd_potential("Karil", KARIL_LOOT, 98)
        add_loot_and_rwd_potential("Verac", VERAC_LOOT, 115)

        # calculate final rewards potential
        if rwd_potential > 1000:
            rwd_potential -= rwd_potential % 1000
        rwd_potential += len(bros_killed_list) * 2

        # add items to loot, rng rolls
        for x in range(1, len(bros_killed_list) + 2): # add items to loot table
            item_roll = 0
            items_loot = 450 - (58 * len(bros_killed_list)) # calculating barrows item chance
            item_roll = random.randint(1, items_loot) # roll for chance
            if item_roll == 1: # award barrows loot
                reward_item = item_rwd_list[random.randint(0, len(item_rwd_list) - 1)] # roll for item
                if reward_item not in final_loot_list: # can't have same item in chest twice
                    final_loot_list.append(reward_item)
            else:
                misc_roll = 0
                misc_roll = random.randint(1, rwd_potential) # roll for misc loot
                mind_rune_amt += roll_for_runes(381, misc_roll, 505, DIFFICULTY_MOD["Mind_Diff"]) # roll mind runes
                chaos_rune_amt += roll_for_runes(506, misc_roll, 630, DIFFICULTY_MOD["Chaos_Diff"]) # roll chaos runes
                death_rune_amt += roll_for_runes(631, misc_roll, 755, DIFFICULTY_MOD["Death_Diff"]) # roll death runes
                blood_rune_amt += roll_for_runes(756, misc_roll, 880, DIFFICULTY_MOD["Blood_Diff"]) # roll blood runes
                if 380 >= misc_roll >= 1: # roll for coins
                    coin_amt += (misc_roll * DIFFICULTY_MOD["Coin_Diff"])
                elif 881 >= misc_roll >= 1005: # roll bolt racks
                    bolt_rack_amt += (misc_roll / DIFFICULTY_MOD["Bolt_Diff"])
                elif 1006 >= misc_roll >= 1011: # roll key half
                    key_roll = random.randint(1, 2)
                    if key_roll == 1:
                        lh_key_flag = True
                    else:
                        th_key_flag = True
                elif misc_roll == 1012:
                    d_med_flag = True
            
        # add misc items to loot list
        add_to_chest(coin_amt, "Coins") # add coins
        add_to_chest(mind_rune_amt, "Mind Runes") # add mind runes
        add_to_chest(chaos_rune_amt, "Chaos Runes") # add chaos runes
        add_to_chest(death_rune_amt, "Death Runes") # add death runes
        add_to_chest(blood_rune_amt, "Blood Runes") # add chaos runes
        add_to_chest(bolt_rack_amt, "Bolt Racks") # add chaos runes
        if lh_key_flag:
            final_loot_list.append("Loop Half of Key") # add key loop half
        elif th_key_flag:
            final_loot_list.append("Tooth half of Key") # add key tooth half
        if d_med_flag:
            final_loot_list.append("Dragon Med Helm")

        # add clue scroll to loot
        clue_chance = random.randint(1, int(200 / len(bros_killed_list)))
        if clue_chance == 1:
            final_loot_list.append("Clue Scroll (elite)")

        # print final chest
        print(f"Your chest contains: {final_loot_list}")

main_loop = True
while main_loop:
    multi_input = int(input("\nHow many simulations do you want to run: "))
    print("\nDo you want to see one final loot chest, or many individual chests?")
    num_chests = str(input("Type 'one' or 'many': "))
    if num_chests.lower() == "one":
        for x in range(1, multi_input):
            main(1)
            # repeat_simulation(bros_killed_list, item_rwd_list, rwd_potential, diary_flag, 1)
            add_to_save_loot()
        print(f"\nYour total loot chest is: {s_save_loot}")
    elif num_chests.lower() == "many":
        for x in range(1, multi_input):
            main()
            # repeat_simulation(bros_killed_list, item_rwd_list, rwd_potential, diary_flag)
            time.sleep(.1)
    else:
        print("Invalid value.")

    return_to_start = True
    # start over request
    while return_to_start:
        print("\nRun another simulation?")
        return_to_start = str(input("Type Y or N: "))
        match return_to_start.lower():
            case "y":
                return_to_start = False
            case "n":
                print("Farewell!")
                main_loop = False
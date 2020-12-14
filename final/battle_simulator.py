'''
(Problem 3) [20 pts.] Battle Simulator
You MUST SUBMIT your code to get the score. Please debug your code before submitting because the submission result shows limited error information.

image

We will implement a simple Battle Simulator. The simulator evaluates the power of a troop quantitatively, calculates training costs, simulates a battle, and reports the result from the battle.
Of course, the most difficult part is simulation. But don’t worry, I already implemented the simulation part, so your job is just implementing some assist functions.

Read the following description carefully and write functions: make_soldier_objects(), evaluate_power() , calculate_training_cost(), and report_result().

Task 1. Parse data of a force and make Infantry / Archers / Cavalry objects (5 pts.)
For a given .csv file, convert into Soldier objects and append to soldier_list, in the make_soldier_objects() function .

The code for reading and parsing the CSV format file is already implemented in the skeleton code.
https://docs.python.org/3/library/csv.html
image

The attribute typecode represents the type of a soldier. (INF : infantry, ARC : archers, CVL : cavalry)
The attribute weapon represents proficiency with a weapon of a soldier.
The attribute armor represents proficiency in armor of a soldier.
The attribute vitality represents the current degree of injury of a soldier.
You have to make a Soldier object for each row of the csv file. Please take a look at the .csv files first and figure out which field belongs to which attribute.
Task 2. Evaluate power of a force (5 pts.)
For a given list of Soldier objects, count the number of soldiers and calculate average weapon and armor proficiencies in the evaluate_power() function.

The statistics must be calculated separately on each type ( Infantry / Archers / Cavalry ).

Your task is to implement calculation of the values below. The values will be returned at the end of the function.
inf_count : the number of infantry
inf_avg_weapon : average weapon of infantry
inf_avg_armor : average armor of infantry
arc_count : the number of archers
arc_avg_weapon : average weapon of archers
arc_avg_armor : average armor of archers
cvl_count : the number of cavalry
cvl_avg_weapon : average weapon of cavalry
cvl_avg_armor : average armor of cavalry

When ???_count = 0, ???_avg_weapon and ???_avg_armor also should be 0.

Task 3. Calculate training costs of forces (5 pts.)
For a given Soldier list, calculate total_cost for all soldiers in the calculate_training_cost() function.

The calculation must follow the criteria below.
image

If a soldier’s vitality < 0.35, the soldier is considered as irreversibly injured and never going to recover the full performance. In this case, the assessed cost becomes 50% of the original value.
For example, for a Soldier (typecode : ‘INF’, weapon : 1.2, armor : 3.0, vitality : 0.25), training cost should be calculated as below.
(1.2 \times 2.5 + 3.0 \times 1.0) \times 0.5 = 3.0(1.2×2.5+3.0×1.0)×0.5=3.0

Task 4. Report result of battle (5 pts.)
For given four Soldier lists that represent two troops before / after a battle, report the calculation of the cost for all soldiers in the report_result() function.

Four Soldier lists represents below
force_a_before : a soldier list of A force before the battle
force_b_before : a soldier list of B force before the battle
force_a_after : a soldier list of A force after the battle
force_b_after : a soldier list of B force after the battle

Your task is calculating the values below. The values will be returned at the end of the function.
damage_a : reduction in the cost of A force through battle ( > 0.0)
damage_b : reduction in the cost of B force through battle ( > 0.0)

Note:

Getting a pass on sample inputs does not guarantee that your code will also get a full mark in grading.
Please implement each task in the corresponding function. You must not modify the function names.
We do not recommend modifying codes outside the area marked by #### YOUR CODE HERE #### ~ ####…####
You must not change the order of soldier lists. It may influence the simulation results.
'''

from typing import List
import csv
import time
import simulation as sim
import answers


class Soldier:
    """Solder class."""
    typecode: str   # 'INF', 'ARC' or 'CVL'
    weapon: float
    armor: float
    vitality: float # 0.0 ~ 1.0
    
    def __init__(self, typecode: str, weapon: float, armor: float, vitality: float):
        """
        Initialize new Soldier

        Args:
            typecode (str): personnel type, 'INF'(Infantry), 'ARC'(Archery) or 'CVL'(Cavalry)
            weapon (float): rating of proficiency on weapon
            armor (float) : rating of proficiency on armor
            vitality (float) : current degree of injury (the higher, the healthier)
        """
        self.typecode = typecode
        self.weapon = weapon
        self.armor = armor
        self.vitality = vitality

def make_soldier_objects(data_dir: str) -> List[Soldier]:
    """

    Read the given CSV file and return list of parsed Soldier objects.

    Args:
        data_dir (str)

    Returns:
        List[Soldier]

    """
    soldier_list = []
    
    with open(data_dir, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        print(reader.__next__()) # print header
        for row in reader:
    ################################# YOUR CODE HERE #################################
            typecode, wp, armor, vitality = row
            if typecode not in ["INF", "ARC", "CVL"]:
                continue
            wp, armor, vitality = float(wp), float(armor), float(vitality)
            soldier = Soldier(typecode, wp, armor, vitality)
            soldier_list.append(soldier)
    ##################################################################################
    return soldier_list



def evaluate_power(soldier_list: List[Soldier]):
    """

    Count the numbers of soldiers and calculate average weapon and armor rating for each type,
    then return.

    Args:
        soldier_list (List[Soldier])

    Returns:
        tuples of tuples on type X (count, avg weapon, avg armor)

    """
    inf_count = 0
    inf_avg_weapon = 0.0
    inf_avg_armor = 0.0
    arc_count = 0
    arc_avg_weapon = 0.0
    arc_avg_armor = 0.0
    cvl_count = 0
    cvl_avg_weapon = 0.0
    cvl_avg_armor = 0.0
    
    for soldier in soldier_list:
    ################################# YOUR CODE HERE #################################
        if soldier.typecode == "ARC":
            arc_count += 1
            arc_avg_armor += soldier.armor
            arc_avg_weapon += soldier.weapon
        elif soldier.typecode == "INF":
            inf_count += 1
            inf_avg_armor += soldier.armor
            inf_avg_weapon += soldier.weapon
        elif soldier.typecode == "CVL":
            cvl_count += 1
            cvl_avg_armor += soldier.armor
            cvl_avg_weapon += soldier.weapon
    if arc_count != 0:
        arc_avg_armor /= arc_count
        arc_avg_weapon /= arc_count

    if cvl_count != 0:
        cvl_avg_armor /= cvl_count
        cvl_avg_weapon /= cvl_count

    if inf_count != 0:
        inf_avg_armor /= inf_count
        inf_avg_weapon /= inf_count
    ##################################################################################
    return (inf_count, inf_avg_weapon, inf_avg_armor), (arc_count, arc_avg_weapon, arc_avg_armor), (cvl_count, cvl_avg_weapon, cvl_avg_armor)



def calculate_training_cost(soldier_list: List[Soldier]):
    """
    
    For a given Soldier list, calculate total training cost for the whole soldiers, then return.

    Args:
        soldier_list (List[Soldier])

    Returns:
        total_cost (float)

    """
    total_cost = 0.0
    
    for soldier in soldier_list:
    ################################# YOUR CODE HERE #################################
        if soldier.typecode == "INF":
            cost = 2.5 * soldier.weapon + 1.0 * soldier.armor
        elif soldier.typecode == "ARC":
            cost = 1.5 * soldier.weapon + 3.0 * soldier.armor
        elif soldier.typecode == "CVL":
            cost = 4.0 * soldier.weapon + 6.0 * soldier.armor
        if soldier.vitality < 0.35:
            cost *= 0.5
        total_cost += cost
    ##################################################################################
    return total_cost



def report_result(force_a_before, force_b_before, force_a_after, force_b_after):
    """
    
    For a given four Soldier lists that represent two troops before / after battle,
    report cost decrease for the two troops, then return.

    Args:
        soldier_list (List[Soldier])

    Returns:
        total_cost (float)

    """
    damage_a = 0.0
    damage_b = 0.0
    ################################# YOUR CODE HERE #################################
    damage_a = calculate_training_cost(force_a_before) - calculate_training_cost(force_a_after)
    damage_b = calculate_training_cost(force_b_before) - calculate_training_cost(force_b_after)
    ##################################################################################
    return damage_a, damage_b



def main():
    force_case1 = 'data/force_case1.csv' # Balanced in cost, With elite CVL
    force_case2 = 'data/force_case2.csv' # Balanced in cost, With recruit CVL
    force_case3 = 'data/force_case3.csv' # Balanced in cost, With elite CVL, Tired troop
    force_case4 = 'data/force_case4.csv' # Infantry only
    force_case5 = 'data/force_case5.csv' # Archers Only
    force_case6 = 'data/force_case6.csv' # Elite cavalry only
    force_case7 = 'data/force_case7.csv' # High cost elite troop
    force_case8 = 'data/force_case8.csv' # Low cost recruit troop
    force_case9 = 'data/force_case9.csv' # Zombies (injured infantry only huge troop)
    force_case0 = 'data/force_case0.csv' # Sword master (a heroic infantry)
    ############################## TRY VARIOUS OPTIONS ###############################
    force_a_csv = force_case1   # FORCE A data
    force_b_csv = force_case2   # FORCE B data
    max_turns = 100             # Maximum turns in the battle simulation
    log_delay = 0.1             # Logging delay between turns in the battle simulation 
    sample_test = True          # Turn on/off test with the sample inputs
    ##################################################################################
    force_a_before = make_soldier_objects(force_a_csv)
    force_b_before = make_soldier_objects(force_b_csv)
    
    force_a_after, force_b_after = sim.simulate_battle(force_a_before, force_b_before, evaluate_power, max_turns, log_delay)   
    damage_a, damage_b = report_result(force_a_before, force_b_before, force_a_after, force_b_after)
    print('FORCE A lost %.2f points' % damage_a)
    print('FORCE B lost %.2f points' % damage_b)
    
    # Sample input is tested only for the case1 and case2
    if sample_test:
        print('\nChecking results on the sample inputs...')
        time.sleep(log_delay * 5)
        print('Task 1. make_soldier_objects() : ', end = '')
        if not answers.check_answer1(make_soldier_objects): return
        print('Task 2. evaluate_power() : ', end = '')
        answers.check_answer2(evaluate_power)
        print('Task 3. calculate_training_cost() : ', end = '')
        if not answers.check_answer3(calculate_training_cost): return
        print('Task 4. report_result() : ', end = '')
        answers.check_answer4(report_result)
    
    
    
if __name__ == "__main__":
    main()
    
# File: Vendingmachine.py
# Description: Simulates a vending machine.
# Assignment number: 8
#
# Name: Rebecca Moore
# EID: rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader: Skyler
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other students.

import random


# Models a Vending Machine. All transactions are in cents.
class VendingMachine:
    # this makes the class.
    def __init__(self, initial_num_drinks, price_per_drink, capacity):
        # sets initial number of drinks
        self.num_drinks = initial_num_drinks
        # sets price of a single drink
        self.price_per_drink = price_per_drink
        # the max drinks the machine can hold
        self.capacity = capacity
        # the amount of money inserted by the user
        self.inserted_money = 0


    # This incriments the money inserted by the amount
    def insert_money(self, amount):
        self.inserted_money += amount


    # returns if enough drinks are avalible and if money is enough
    def can_dispense(self):
        return self.num_drinks >= 1 and \
                self.inserted_money >= self.price_per_drink


    # This dispenses a drink and returns "ENJOY" if enough money was
    # inserted and there are enough drinks avalible. If not enough money
    # was inserted but there are enough drinks, returns "INSUFFICIENT
    # FUNDS" else, returns "EMPTY"
    def dispense(self):
        if self.num_drinks >= 1 and \
                self.inserted_money < self.price_per_drink:
            return "INSUFFICIENT FUNDS"
        elif self.can_dispense():
            self.num_drinks -= 1
            self.inserted_money -= self.price_per_drink
            return "ENJOY"
        else:
            return "EMPTY"


    # returns amount of money currently in machine and sets inserted
    # money to zero
    def get_change(self):
        inserted_money = self.inserted_money
        self.inserted_money = 0
        return inserted_money


    #sets drinks avalible to machines capacity
    def refill(self):
        self.num_drinks = self.capacity


# Run a simulation using the Vending Machine objects.
def main():
    if input('Run simple tests? ') == 'y':
        simple_tests()
    stress_tests()


# Simple operations with a single Vending Machine with a capacity of
# 5 drinks, currently has 2 drinks, and it costs 50 cents per drink.
def simple_tests():
    print('***** SIMPLE TESTS *****')
    vend1 = VendingMachine(2, 50, 5)
    vend1.insert_money(25)
    vend1.insert_money(10)
    vend1.insert_money(10)
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    vend1.insert_money(10)
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    print('can dispense:', vend1.can_dispense())
    print('get change:', vend1.get_change())
    print('get change:', vend1.get_change())
    vend1.insert_money(100)
    vend1.insert_money(25)
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    vend1.refill()
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    print('get change:', vend1.get_change())
    print()


# Run stress tests. Given the same number of machines, the same
# number of operations, and the same initial seed, output will
# be the same.
def stress_tests():
    # Get the seed, number of operations, and number of machines from the user.
    random.seed(eval(input('Enter random seed: ')))
    num_operations = eval(input('Enter the number of operations: '))
    num_machines = eval(input('Enter the number of machines: '))
    print('\n***** STRESS TESTS *****')

    # Create the required number of machines and run the tests.
    machines = create_machines(num_machines, 10)
    perform_stress_tests_ops(machines, num_operations)


# Run the actual operations for the stess tests.
def perform_stress_tests_ops(machines, num_operations):
    # Only allow US coins, excluding pennies! (We should get rid of pennies!)
    COINS = [5, 10, 25, 50, 100]
    LAST_COIN_INDEX = len(COINS) - 1
    LAST_MACHINE_INDEX = len(machines) - 1

    # Pick a random operation.
    # 55% chance of insert_money.
    # 20% chance of can dispense.
    # 21% chance of dispense. (If we dispense, there is a 80% chance dispense
    #       is called directly after.)
    #  3% chance of get_change.
    #  1% chance of refill.
    for i in range(1, num_operations + 1):
        print('Operation =', i)
        machine_number = random.randint(0, LAST_MACHINE_INDEX)
        print('Machine =', machine_number)
        machine = machines[machine_number]

        random_op = random.randint(1, 100)
        if random_op <= 55:
            coin = COINS[random.randint(0, LAST_COIN_INDEX)]
            print('Insert money, amount =', coin)
            machine.insert_money(coin)
        elif random_op <= 75:
            print('Can dispense:', machine.can_dispense())
        elif random_op <= 96:
            result = machine.dispense()
            print('Dispense:', result)
            if result == 'ENJOY':
                # Do they remember their change? 80% chance of yes.
                if random.randint(1, 5) <= 4:
                    print('Get change, amount =', machine.get_change())
                else:
                    print('Forgot change after dispense.')
        elif random_op <= 99:
            print('Get change, amount =', machine.get_change())
        else:
            print('Refill.')
            machine.refill()
        print()


# Create a list with the required number of machines.
# I expect num_machines > 0.
# The first machine always has a price of 25, 1 drink, and a capacoty of 3.
# All machines will have a price between 25 and 200 in multiples of 25.
# All machines will have a capcity between 2 and max_capacity.
# The relatively small capacity is for simple tests.
def create_machines(num_machines, max_capacity):
    PRICE_MULTIPLIER = 25
    machines = [VendingMachine(1, PRICE_MULTIPLIER, 3)]
    print('Machine 0: price = 25, capacity = 3, initial drinks = 1')
    for i in range(1, num_machines):
        price = random.randint(1, 8) * PRICE_MULTIPLIER
        capacity = random.randint(2, max_capacity)
        drinks = random.randint(0, capacity)
        print('Machine ', i, ': price = ', price, ', capacity = ', capacity,
              ', initial drinks = ', drinks, sep='')
        machines.append(VendingMachine(drinks, price, capacity))
    print()
    return machines


main()

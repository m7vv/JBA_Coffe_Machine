class CoffeeMachine:
    prompt = {
        'choosing an action': 'Write action (buy, fill, take, remaining, exit):',
        'choosing a type of coffee': 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:',
        'filling water': 'Write how many ml of water do you want to add:',
        'filling milk': 'Write how many ml of milk do you want to add:',
        'filling beans': 'Write how many ml of milk do you want to add:',
        'filling cups': 'Write how many disposable cups of coffee do you want to add:'
    }
    types_of_coffee = {
        'espresso': (250, 0, 16, 4),
        'latte': (350, 75, 20, 7),
        'cappuccino':(200, 100, 12, 6)
    }

    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.money = money
        self.cups = cups
        self.state = "choosing an action"

    def __repr__(self):
        state: str = ('The coffee machine has:\n' +
                      f'{self.water} of water\n' +
                      f'{self.milk} of milk\n' +
                      f'{self.beans} of coffee beans\n' +
                      f'{self.cups} of disposable cups\n' +
                      f'${self.money} of money')
        return state

    def make_coffee(self, water_norm, milk_norm, beans_norm, price):
        cups_from_water = (self.water // water_norm) if water_norm != 0 else 1
        cups_from_milk = (self.milk // milk_norm) if milk_norm != 0 else 1
        cups_from_beans = (self.beans // beans_norm) if beans_norm != 0 else 1
        cups_possible = min(cups_from_beans, cups_from_milk, cups_from_water)
        if cups_possible >= 1 and self.cups >= 1:
            self.water -= water_norm
            self.milk -= milk_norm
            self.beans -= beans_norm
            self.cups -= 1
            self.money += price
            print("I have enough resources, making you a coffee!")
        else:
            print("Sorry, not enough resources!")

    def get_command(self, command: str):
        if self.state == 'choosing an action':
            if command == 'buy':
                self.state = 'choosing a type of coffee'
            elif command == 'fill':
                self.state = 'filling water'
            elif command == 'take':
                print('I gave you ${}'.format(self.money))
                self.money -= self.money
            elif command == 'remaining':
                print(self)
            elif command == 'exit':
                self.state = 'exit'
        elif self.state == 'filling water':
            self.water += int(command)
            self.state = 'filling milk'
        elif self.state == 'filling milk':
            self.milk += int(command)
            self.state = 'filling beans'
        elif self.state == 'filling beans':
            self.beans += int(command)
            self.state = 'filling cups'
        elif self.state == 'filling cups':
            self.cups += int(command)
            self.state = 'choosing an action'
        elif self.state == 'choosing a type of coffee':
            if '1' == command:
                self.make_coffee(*self.types_of_coffee['espresso'])
            elif '2' == command:
                self.make_coffee(*self.types_of_coffee['latte'])
            elif '3' == command:
                self.make_coffee(*self.types_of_coffee['cappuccino'])
            elif 'back' == command:
                pass
            self.state = 'choosing an action'


''' changed to using dictionary
    def get_prompt(self):
        if self.state == 'choosing an action':
            return 'Write action (buy, fill, take, remaining, exit):'
        elif self.state == 'choosing a type of coffee':
            return 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'
        elif self.state == 'filling water':
            return 'Write how many ml of water do you want to add:'
        elif self.state == 'filling milk':
            return 'Write how many ml of milk do you want to add:'
        elif self.state == 'filling beans':
            return 'Write how many grams of coffee beans do you want to add:'
        elif self.state == 'filling cups':
            return 'Write how many disposable cups of coffee do you want to add:'
        elif self.state == 'choosing a type of coffee':
            return 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'
'''

cm = CoffeeMachine()
while True:
    if cm.state == 'exit':
        break
    print(cm.prompt[cm.state])
    cm.get_command(input())

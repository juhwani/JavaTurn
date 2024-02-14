class CoffeeGroup:
    def __init__(self):
        self.coworkers = {} # list of all the coworkers
        self.menu = {
    'Black': 2.0,
    'Espresso': 2.5,
    'Latte': 3.5,
    'Americano': 2.75,
    'Cappuccino': 3.5,
    'Mocha': 4.0,
    'Cafe Au Lait': 3.0,
    'Macchiato': 3.0,
    'Caramel Macchiato': 3.75,
    'Flat White': 3.75,
    'Irish Coffee': 5.0,
    'Frappe': 4.5,
    'Cold Brew': 3.5,
    'Affogato': 4.5,
    'Red Eye': 3.25,
    'Vietnamese Coffee': 4.0
} # menu
        self.menus = "Coffee Menu\n\nBlack Coffee         $2.00\nEspresso             $2.50\nLatte                $3.50\nAmericano            $2.75\nCappuccino           $3.50\nMocha                $4.00\nCafe Au Lait         $3.00\nMacchiato            $3.00\nCaramel Macchiato    $3.75\nFlat White           $3.75\nIrish Coffee         $5.00\nFrappe               $4.50\nCold Brew            $3.50\nAffogato             $4.50\nRed Eye              $3.25\nVietnamese Coffee    $4.00\n"
    def add_coworker(self, name, favorite_coffee):
        if name in self.coworkers:
            print(f"{name} is already in the system.")
        if favorite_coffee not in self.menu:
            print(f"{favorite_coffee} is not in the system. Press the menu button for reference")

        else:
            self.coworkers[name] = {'favorite_coffee': favorite_coffee, 'total_paid': 0, 'average_cost': self.menu[favorite_coffee]}

    def update_payment(self, name, amount):
        if name in self.coworkers:
            self.coworkers[name]['total_paid'] += amount
        else:
            print(f"{name} not found in the system.")

    def calculate_total(self):
        res = 0
        for name, info in self.coworkers.items():
            res += info['average_cost']
        return res

    def next_to_pay(self):
        min_paid_ratio = float('inf')
        next_payer = None
        for name, info in self.coworkers.items():
            paid_ratio = info['total_paid'] / info['average_cost']
            if paid_ratio < min_paid_ratio:
                min_paid_ratio = paid_ratio
                next_payer = name
        return next_payer


    def add_new_coworker(self, name, favorite_coffee, average_cost):
        # Adding a new coworker with a calculated starting total_paid 
        # to ensure fairness with others based on the average cost of their coffee.
        average_total_paid = sum([info['total_paid'] for info in self.coworkers.values()]) / len(self.coworkers)
        self.coworkers[name] = {'favorite_coffee': favorite_coffee, 'total_paid': average_total_paid, 'average_cost': average_cost}

    def delete_coworker(self, name):
        if name not in self.coworkers:
            print(f"{name} not found in the system.")
            return

        del self.coworkers[name] # Removing the coworker from the group

        # Recalculate and adjust payments among the remaining coworkers

        if len(self.coworkers) > 0:
            average_total_paid = sum([info['total_paid'] for info in self.coworkers.values()]) / len(self.coworkers)
            for info in self.coworkers.values():
                info['total_paid'] = average_total_paid
        else:
            print("No coworkers left in the system.")



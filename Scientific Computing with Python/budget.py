class Category:

    def __init__(self, category) -> None:
        self.category = category
        self.ledger = []
        self.balance = 0
    
    def __repr__(self) -> str:
        return_str = [self.category.center(30, '*')]
        return_str.extend(
            [f"{transaction['description'][:23]:23}{transaction['amount']:7.2f}" for transaction in self.ledger])
        return_str.append(f'Total:{self.balance:7.2f}')
        return '\n'.join(return_str)
    
    def deposit(self, deposit, description=''):
        self.ledger.append({"amount": deposit, "description": description})
        self.balance += deposit
    
    def withdraw(self, withdraw, description=''):
        if (self.balance - withdraw)>0:
            self.ledger.append({"amount": -1*withdraw, "description": description})
            self.balance -= withdraw
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, transfer, another_category):
        if (self.balance - transfer) > 0:
            description = f'Transfer to {another_category.category}'
            self.withdraw(transfer, description)
            another_category.deposit(transfer, f'Transfer from {self.category}')
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else: 
            return True
        

def create_spend_chart(categories:list):
    output_str = 'Percentage spent by category\n'
    categories_spend = []
    category_char_split = []

    # Calculate percentage
    for category in categories:
        category_char_split.append(list(category.category))
        curr_category_spend = 0
        for each_transaction in category.ledger:
            if (amount := each_transaction['amount'])<0:
                curr_category_spend -= amount
        categories_spend.append(curr_category_spend)
    sum_spend = sum(categories_spend)
    percentage_category_spend = [
        int(each_category_spend*10//sum_spend)*10 for each_category_spend in categories_spend]
    # print(percentage_category_spend)

    # bar chart at percentage
    spaces = len(percentage_category_spend) *3
    for index in range(11):
        percent_value = 100-index*10
        curr_line_str = f"{percent_value:>3}| {spaces * ' '}\n"
        match_percent = [
            index for index, value in enumerate(percentage_category_spend) 
            if value>=percent_value]
        if match_percent:
            for index in match_percent:
                curr_line_str = curr_line_str[:5+index*3] + 'o' + curr_line_str[6+index*3:]
        output_str += curr_line_str
 
    # dashed bar
    output_str += f"    -{spaces * '-'}"

    # category's name
    max_iter = max([len(char) for char in category_char_split])
    for index in range(max_iter):
        curr_line_str = '\n     '
        for each_category_char_split in category_char_split:
            try:
                char = each_category_char_split[index]
            except:
                char = ' '
            curr_line_str += (char+'  ')
        output_str += curr_line_str
    return output_str




        




if __name__ == '__main__':
    # food = Category('food')
    # food.deposit(900, "deposit")
    # food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    
    # entertainment = Category('entertainment')
    # entertainment.deposit(500, 'deposit')
    # entertainment.withdraw(3990.12, 'withdraw wwwwwwwwwwwwwwwwwww')
    # entertainment.transfer(5, food)
    # print(food, entertainment, sep='\n\n\n\n')

    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(create_spend_chart([food, clothing, auto]))
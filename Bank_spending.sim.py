# Bank simulator/spending limit

class BankAccount:
    def __init__(self, monthly_income, fixed_costs, wants_budget, savings_budget):
        self.monthly_income = monthly_income
        self.fixed_costs = fixed_costs
        self.wants_budget = wants_budget
        self.savings_budget = savings_budget
        self.remaining_income = monthly_income - fixed_costs
        self.daily_spending = 0
        self.spent_on_wants = 0
        self.ytd_wants_spending = 0
        self.ytd_other_spending = 0
        self.mtd_wants_spending = 0
        self.mtd_other_spending = 0

    def spend(self, amount, category):
        if category == "wants":
            if self.spent_on_wants + amount > self.wants_budget:
                print(f"Warning: Exceeding your wants budget by ${self.spent_on_wants + amount - self.wants_budget:.2f}")
            self.spent_on_wants += amount
            self.mtd_wants_spending += amount
            self.ytd_wants_spending += amount
        elif category == "other":
            self.mtd_other_spending += amount
            self.ytd_other_spending += amount
        
        self.daily_spending += amount
        self.remaining_income -= amount

    def reset_daily_spending(self):
        self.daily_spending = 0

    def reset_mtd_spending(self):
        self.mtd_wants_spending = 0
        self.mtd_other_spending = 0

    def get_status(self):
        return {
            "Remaining Income": self.remaining_income,
            "Daily Spending": self.daily_spending,
            "Spent on Wants": self.spent_on_wants,
            "Wants Budget": self.wants_budget,
            "Savings Budget": self.savings_budget,
            "YTD Wants Spending": self.ytd_wants_spending,
            "YTD Other Spending": self.ytd_other_spending,
            "MTD Wants Spending": self.mtd_wants_spending,
            "MTD Other Spending": self.mtd_other_spending
        }

    def get_ytd_spending(self):
        return {
            "YTD Wants Spending": self.ytd_wants_spending,
            "YTD Other Spending": self.ytd_other_spending
        }

    def get_mtd_spending(self):
        return {
            "MTD Wants Spending": self.mtd_wants_spending,
            "MTD Other Spending": self.mtd_other_spending
        }

def main():
    # Updated values
    monthly_income = 7500
    fixed_costs = 5480  # Includes rent, food, gas, subscriptions, utilities, and automobile payment
    wants_budget = 1374
    savings_budget = 646

    account = BankAccount(monthly_income, fixed_costs, wants_budget, savings_budget)

    while True:
        print("\nCurrent Status:")
        status = account.get_status()
        for key, value in status.items():
            print(f"{key}: ${value:.2f}")

        action = input("\nEnter 'spend' to add spending, 'reset' to reset daily spending, 'ytd' to view YTD spending, 'mtd' to view MTD spending, or 'exit' to quit: ").lower()

        if action == 'spend':
            try:
                amount = float(input("Enter spending amount: $"))
                category = input("Enter spending category (wants/other): ").lower()
                if category not in ['wants', 'other']:
                    print("Invalid category. Please enter 'wants' or 'other'.")
                else:
                    account.spend(amount, category)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action == 'reset':
            account.reset_daily_spending()
        elif action == 'ytd':
            ytd_spending = account.get_ytd_spending()
            print("\nYear-to-Date Spending:")
            for key, value in ytd_spending.items():
                print(f"{key}: ${value:.2f}")
        elif action == 'mtd':
            mtd_spending = account.get_mtd_spending()
            print("\nMonth-to-Date Spending:")
            for key, value in mtd_spending.items():
                print(f"{key}: ${value:.2f}")
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()

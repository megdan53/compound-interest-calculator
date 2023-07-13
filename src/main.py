class compoundCal:
    def __init__(self, principal, interest_rate, timePeriod, compound_freq):
        self.principal = principal
        self.interest_rate = interest_rate
        self.timePeriod = timePeriod
        self.compound_freq = compound_freq

    def interest_compound(self):
        amount = self.principal * (1 + (self.interest_rate / self.compound_freq)) ** (self.compound_freq * self.timePeriod)
        interestAmt = amount - self.principal
        return interestAmt

principal = float(input("principal amount: "))
interest_rate = float(input("interest rate: "))
timePeriod = float(input("timePeriod: "))
compound_freq = float(input("compounding frequency: "))

calculatorint = compoundCal(principal, interest_rate, timePeriod, compound_freq)
total_interest = calculatorint.interest_compound()
print("total interest accumulate: ", round(total_interest, 2))
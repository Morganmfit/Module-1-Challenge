loan_costs = [500, 600, 200, 1000, 450]
len(loan_costs)
print("The total amount of outstanding loans is")
print(len(loan_costs))
sum(loan_costs)
print ("The total value of all outstanding loans is:") 
print(sum(loan_costs))
sum(loan_costs)/len(loan_costs)
print("The average cost of each loan is")
print(sum(loan_costs)/len(loan_costs))
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
print("The future value of this loan is")
print(loan.get('future_value'))
print("The number of months remaining on this loan is")
print(loan.get('remaining_months'))
remaining_months = 9
future_value = 1000
present_value = future_value / (1+ 0.20/12)**9
fair_value = 861.77
print("The fair value of the loan is currently")
print(present_value)
if present_value > (loan["loan_price"]):
     print("This loan is worth buying")
else : present_value < (loan["loan_price"]),
print("This loan is too expensive and not worth the price")
def calculate_present_value (future_value = 1000, remaining_months = 9, annual_discount_rate= 0.20 ):
    present_value = future_value / (1+ annual_discount_rate/12)**remaining_months
    return calculate_present_value
print(f"The present value of the loan is: {present_value}")
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
inexpensive_loans = []
for loan_price in [loans]:
    if loan_price < 500 :
     inexpensive_loans.append(i)
print(inexpensive_loans)
import csv
with open ('loan_analyzer.csv', 'w','newline=') as f:
    csvwriter = csv.writer(f)

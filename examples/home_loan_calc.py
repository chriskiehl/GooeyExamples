"""
This is the
"""
import csv
import zipfile
from gooey import Gooey, GooeyParser

import os
from io import TextIOWrapper

path = os.path.join(os.path.dirname(__file__), 'sample_data', 'worldcities.zip')

with zipfile.ZipFile(path) as zf:
    with zf.open('worldcities.csv', 'r') as f:
        reader = csv.reader(TextIOWrapper(f, 'utf-8'))
        locations = ['{} - {}'.format(x[4], x[1]) for x in reader][1:][:1000]


@Gooey(program_name='Home Loan Calculator')
def loan_calculator():
    parser = GooeyParser(
        description='Welcome to the Home Loan EMI Calculator . Calculate anytime, anywhere !')

    calculator = parser.add_argument_group('Calculate Your EMI on Home Loan', gooey_options={
        'show_border': True
    })

    calculator.add_argument(
        'loan_amount',
        metavar='Loan Amount',
        help='Loan Amount',
        gooey_options={'show_help': False, 'label_color': '#2e2424'})
    calculator.add_argument(
        'tenure',
        metavar='Tenure(Years)',
        help='Tenure(Years)',
        gooey_options={'show_help': False, 'label_color': '#2e2424'})
    calculator.add_argument(
        'interest_rate',
        metavar='Interest Rate (% P.A.)',
        help='Interest Rate (% P.A.)',
        gooey_options={'show_help': False, 'label_color': '#2e2424'})

    args = parser.parse_args()
    print(args)
    print('Loan Amount :', args.loan_amount);
    print('Tenure(Years) :', args.tenure);
    print('Interest Rate (% P.A.) :', args.interest_rate);
    #rate_of_int = Annual Rate of interest/12/100
    interest_rate = float(args.interest_rate)
    rate_of_int = (interest_rate / 12) / 100
    loan_amount = float(args.loan_amount)
    tenure = int(args.tenure)
    #EMI = P x R x (1+R)^N / [(1+R)^N-1]
    # P = Principal loan amount = 10,00,000
    # R = Monthly interest rate = 7.2/12/100 = 0.006
    # N = Loan tenure in months = 10 Y = 120 Months
    #i.e ₹10,00,000 * 0.006 * (1 + 0.006)120 / ((1 + 0.006)120 - 1)
    #P = 1000000  # Principal amount
    #R = 0.006  # Interest rate
    #N = 120    # Number of periods
    #result = P * R * ((1+R)**N) / (((1+R)**N) - 1)
    emi = loan_amount * rate_of_int * ((1 +rate_of_int)**tenure) / (((1+rate_of_int)**tenure) - 1)
    print ('EMI : ', float(emi))
    # ... rest of program



if __name__ == '__main__':
    loan_calculator()
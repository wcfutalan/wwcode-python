""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

total = float(input('How much is your total bill?: '))
payment = float(input('How much is your payment? '))
change = payment - total
print('Hi! Your change is {}'.format(change))
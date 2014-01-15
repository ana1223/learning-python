car_cost = 20000
monthly_payment = 200
insurance = 100
total_monthly = monthly_payment + insurance
car_age = 13
amount_paid = monthly_payment * car_age
amount_left = car_cost - amount_paid
months_left = amount_left / monthly_payment
years_left = months_left / 12
bonus = 5 ** 18

print "My car cost", car_cost, "dollars."
print "I've had my car for", car_age, "months."
print "My monthly payment is", monthly_payment, "plus insurance, so it ends up being", total_monthly, "a month."
print "I've already paid %d of my car and have %d left." % (amount_paid, amount_left)
print "I have %d months left until I've paid off my car, which is %d years." % (months_left, years_left)
print bonus
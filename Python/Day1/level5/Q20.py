bal = float(input("Enter current bank balance: "))
wt_draw = float(input("Enter amount to withdraw"))

bal_left = bal - wt_draw

print("Remaining available balance is", f'{bal_left}')
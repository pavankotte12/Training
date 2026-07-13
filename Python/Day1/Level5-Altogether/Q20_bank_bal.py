bal = float(input("Enter current bank balance: "))
wt_draw = float(input("Enter amount to withdraw: "))

bal_left = bal - wt_draw

print(f"Remaining available balance is {bal_left}."
      f" Is the remaining balance negative? {bal_left < 0}"
      )
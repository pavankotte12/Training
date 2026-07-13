# Accepting list of hobbies from two persons and displaying their unique hobbies
pavan_hobbies = set(input("Enter your pavan's hobbies: ").split(","))
kumar_hobbies = set(input("Enter your kumar's hobbies: ").split(","))

print(f"List of pavan's hobbies {pavan_hobbies}")
print(f"List of kumar's hobbies {kumar_hobbies}")

# Pavan's Unique Hobbies
pavan_unique = pavan_hobbies - kumar_hobbies

# Kumar's  Unique Hobbies
kumar_unique = kumar_hobbies - pavan_hobbies

# Display results
print(f"Pavan's unique hobbies: {pavan_unique}")

print(f"Kumar's unique hobbies: {kumar_unique}")
   

    
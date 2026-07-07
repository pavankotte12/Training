# Take list of comma separated items, each item cleaned up on its own line and print with rejoined " -> "
try:
    items = [" pen ",  " book",  "bag "]
    print(items[0].strip())
    print(items[1].strip())
    print(items[2].strip())
    delimeter = '->'
    print(delimeter.join(items))
    print(delimeter.join(item.strip() for item in items)
)
except IndexError:
    print("Error: The list does not contain enough items.")

except TypeError:
    print("Error: All items in the list must be strings.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
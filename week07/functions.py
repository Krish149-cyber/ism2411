# AI Disclosure: I used AI on some of Exercise 5.
#
# Self-Assessment
# 1. The first error I saw was that the total was overwritten each time. I saw it by
# reading through the code. This shows that I can sometimes find an error just by
# skimming through the code.
#
# 2. apply_discount(price, tier) takes the price and the customer’s tier for discounts.
# Then it applies the discount of that tier (15% for gold, 10% for silver, 5% for
# bronze, and no discount for other tiers) and returns the price after discount.
# A colleague could figure out the general purpose from the function name and inputs,
# but would need the tier rates documented to know which values to use.
#
# 3. I used AI on some of Exercise 5. It helped me understand what I was missing, as
# well as understanding why what I'm missing matters in the code.
# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")

# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

with_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${with_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    return discounted_price + calculate_tax(discounted_price, tax_rate)


print(
    f'final_price(200, "gold", 0.07) = '
    f'${final_price(200, "gold", 0.07):.2f}'
)

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

    # --- Exercise 5 ---
sales = [120, 80, 250, 175, 90]

# Add each sale to the running total.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Count each sale in the list.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Stop before the index reaches the list length.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

    # --- Exercise 6 ---
x = 100  # global variable


def double_it():
    x = 999  # local variable; it exists only inside this function
    return x * 2


print(x)
print(double_it())
print(x)

# Scope means a variable created inside a function is separate from a global variable with the same name.
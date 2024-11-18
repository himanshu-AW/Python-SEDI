# Question 4- Write a program to calculate cost price if selling price and loss percentage are given:
# CP = ( SP * 100 ) / ( 100 – percentage loss )

sp = 3452
lp = 25
print(f"Selling price (SP): {sp}")
print(f"Loss Percentage (LP): {lp}")
cp= (sp * 100) / (100 - lp)
print(f"Cost Price (CP): {cp}")

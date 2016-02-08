# Use a loop to display Celsuis and Farenheit equivalent values from 0 to 20
# Kadar Anwar
# Python 3.4
# FCloop.py
# 2/27/2015 - ISAT 252

# Initialize and declare variables
c = 0.0
f = 0.0

# Display Celsius temperatures 0 through 20
print("Temperatures in Celsius:")
for c in range(0,21,1):
    print(c, end=' ')
print()

# Display Celsius temperatures converted to Farenheit
print("Temperatures in Farenheit:")
for i in range(0,21):
    f = ((1.8*i)+32)
    print(format(f, '.2f'), end=' ')
print()

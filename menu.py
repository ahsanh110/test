# Resturant Menu

menu, qty, stotal, total = 0,0,0,0
tax=7.05

print('       WELCOME TO GIT TRAINING')
print('1) Beef Gyro Sandwich......... $7.99')
print('2) Chicken Gyro Sandwich...... $6.99')
print('3) Gyro Platter .............. $10.29')
print('4) Chicken Platter............ $9.99')

menu = int(input('Please enter your choice  (1 to 4)' ))
qty = int(input("Enter Quantity: " )) 

if menu == 1:
    stotal = qty * 7.99
    
if menu == 2:
    stotal = qty * 6.99

if menu == 3:
    stotal = qty * 10.29

if menu == 4:
    stotal = qty * 9.99

tax = round((stotal * tax) / 100,2)
total = round(stotal + tax, 2)

print ('SUBTOTAL     ' +'$'+str(stotal))
print ('TAX 8.25%    ' +'$'+str(tax))
print ('TOTAL        ' +'$'+str(total))









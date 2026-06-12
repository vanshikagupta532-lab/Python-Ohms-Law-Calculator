print("===== OHM'S LAW CALCULATOR =====")

print("1. Calculate Voltage (V)")
print("2. Calculate Current (I)")
print("3. Calculate Resistance (R)")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    current = float(input("Enter Current (A): "))
    resistance = float(input("Enter Resistance (Ohm): "))

    voltage = current * resistance

    print("Voltage =", voltage, "Volts")

elif choice == 2:
    voltage = float(input("Enter Voltage (V): "))
    resistance = float(input("Enter Resistance (Ohm): "))

    current = voltage / resistance

    print("Current =", current, "Amperes")

elif choice == 3:
    voltage = float(input("Enter Voltage (V): "))
    current = float(input("Enter Current (A): "))

    resistance = voltage / current

    print("Resistance =", resistance, "Ohms")

else:
    print("Invalid Choice")
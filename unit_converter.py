def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'F':
            return value * 9/5 + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5/9
        elif to_unit == 'K':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9/5 + 32
    return None

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'kg': 1,
        'g': 1000,
        'lb': 2.20462,
        'oz': 35.274
    }
    if from_unit in conversion_factors and to_unit in conversion_factors:
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])
    return None

def convert_height(value, from_unit, to_unit):
    conversion_factors = {
        'm': 1,
        'cm': 100,
        'ft': 3.28084,
        'in': 39.3701
    }
    if from_unit in conversion_factors and to_unit in conversion_factors:
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])
    return None

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Unit Converter")
    print("1. Temperature")
    print("2. Weight")
    print("3. Height")
    
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    if choice == '1':
        print("\nTemperature Conversion")
        value = get_numeric_input("Enter the temperature value: ")
        from_unit = get_valid_input("From unit (C/F/K): ", ['c', 'f', 'k']).upper()
        to_unit = get_valid_input("To unit (C/F/K): ", ['c', 'f', 'k']).upper()
        result = convert_temperature(value, from_unit, to_unit)
    
    elif choice == '2':
        print("\nWeight Conversion")
        value = get_numeric_input("Enter the weight value: ")
        from_unit = get_valid_input("From unit (kg/g/lb/oz): ", ['kg', 'g', 'lb', 'oz'])
        to_unit = get_valid_input("To unit (kg/g/lb/oz): ", ['kg', 'g', 'lb', 'oz'])
        result = convert_weight(value, from_unit, to_unit)
    
    elif choice == '3':
        print("\nHeight Conversion")
        value = get_numeric_input("Enter the height value: ")
        from_unit = get_valid_input("From unit (m/cm/ft/in): ", ['m', 'cm', 'ft', 'in'])
        to_unit = get_valid_input("To unit (m/cm/ft/in): ", ['m', 'cm', 'ft', 'in'])
        result = convert_height(value, from_unit, to_unit)
    
    if result is not None:
        print(f"\nConversion Result: {value} {from_unit} = {result:.2f} {to_unit}")
    else:
        print("\nError: Invalid conversion units selected.")

if __name__ == "__main__":
    main()

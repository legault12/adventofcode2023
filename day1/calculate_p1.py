def calculate_calibration_sum_from_file(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next((char for char in reversed(line) if char.isdigit()), None)
            
            if first_digit and last_digit:
                total_sum += int(first_digit + last_digit)
    
    return total_sum

input_file_path = 'input.txt'
result = calculate_calibration_sum_from_file(input_file_path)
print("Total sum of calibration values:", result)
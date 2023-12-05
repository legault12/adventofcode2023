import re

def convert_word_to_number(word):
    number_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, 
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    return number_words.get(word.lower(), None)

def find_numbers_in_string_advanced(s):
    number_regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

    matches = [match for match in re.finditer(number_regex, s, re.IGNORECASE) if match.group(1)]

    if not matches:
        return None, None

    first_match = matches[0].group(1)
    last_match = matches[-1].group(1)

    first_number = first_match if first_match.isdigit() else convert_word_to_number(first_match)
    last_number = last_match if last_match.isdigit() else convert_word_to_number(last_match)

    return first_number, last_number

def calculate_calibration_sum_from_file(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            first_number, last_number = find_numbers_in_string_advanced(line)
            
            if first_number is not None and last_number is not None:
                calibration_value = int(first_number) * 10 + int(last_number) if first_number != last_number else int(first_number) * 11
                total_sum += calibration_value
    
    return total_sum

input_file_path = 'input.txt'
result = calculate_calibration_sum_from_file(input_file_path)
print("Total sum of calibration values:", result)

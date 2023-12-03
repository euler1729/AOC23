## Part 1
def extract_calibration_part_one(line):
    calibration_sum = 0
    
    with open(line, 'r') as file:
        for line in file:
            line = line.strip()
            
            if line:
                first_digit = next((char for char in line if char.isdigit()), None)
                last_digit = next((char for char in line[::-1] if char.isdigit()), None)
                
                if first_digit and last_digit:
                    calibration_value = int(first_digit + last_digit)
                    calibration_sum += calibration_value
    
    return calibration_sum
print("Part 1: ", extract_calibration_part_one('d1.txt'))

## Part 2
word_to_digit = {
    'zero': '0', 
    'one': '1', 
    'two': '2', 
    'three': '3', 
    'four': '4',
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9',
    '0': '0', 
    '1': '1', 
    '2': '2', 
    '3': '3', 
    '4': '4',
    '5': '5', 
    '6': '6', 
    '7': '7', 
    '8': '8', 
    '9': '9',
}

def convert_to_digit(word):
    return int(word_to_digit.get(word, word))

def find_first_last_digits(s):
    first, fpos, last, lpos = -1, 9999, -1, -1
    for k in word_to_digit:
        if k in s:
            first_digit = s.find(k)
            last_digit = s.rfind(k)
            if first_digit < fpos:
                fpos = first_digit
                first = convert_to_digit(k)
            if last_digit > lpos:
                lpos = last_digit
                last = convert_to_digit(k)
    return first*10 + last

def extract_calibration_part_two(line):
    calibration_sum = 0
    with open(line, 'r') as file:
        for line in file:
            line = line.strip()
            calibration_sum = calibration_sum + find_first_last_digits(line)
    return calibration_sum

print("Part 2: ",extract_calibration_part_two('d1.txt'))

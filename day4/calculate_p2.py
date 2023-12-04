def parse_scratchcards(data):
    scratchcards = []

    for line in data:
        parts = line.strip().split('|')
        winning_numbers = list(map(int, parts[0].split(':')[1].split()))
        your_numbers = list(map(int, parts[1].split()))
        scratchcards.append({"winning_numbers": winning_numbers, "your_numbers": your_numbers})

    return scratchcards

def calculate_total_scratchcards(scratchcards):
    total_scratchcards = 0
    card_copies = [1] * len(scratchcards)

    for i in range(len(scratchcards)):
        for j in range(card_copies[i]):
            matches = set(scratchcards[i]["winning_numbers"]) & set(scratchcards[i]["your_numbers"])
            for k in range(1, len(matches) + 1):
                if i + k < len(scratchcards):
                    card_copies[i + k] += 1

    total_scratchcards = sum(card_copies)
    return total_scratchcards

file_path = 'input.txt'
with open(file_path, 'r') as file:
    scratchcard_data = file.readlines()

parsed_scratchcards = parse_scratchcards(scratchcard_data)
total_scratchcards = calculate_total_scratchcards(parsed_scratchcards)
print(f"Total scratchcards: {total_scratchcards}")

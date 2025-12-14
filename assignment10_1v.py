def parse_grades(raw_data):
    my_dict = {}
    for data in raw_data:
        parts = data.split(",")
        subject = parts[1]
        score = int(parts[2])
        if subject not in my_dict:
            my_dict[subject] = []
        my_dict[subject].append((score))
    return my_dict

def print_averages(grade_dict):
    for subject in grade_dict:
        average_score = 0
        total = 0
        for scores in grade_dict[subject]:
            single_score = scores
            total+=single_score
            average_score = total/((len(grade_dict[subject])))
        print(f"{subject} average: {average_score:.2f} ")    
            

raw_data = [
    "Alice,Math,85",
    "Bob,Physics,70",
    "Charlie,Math,90",
    "David,Chemistry,60",
    "Eve,Physics,88",
    "Frank,Math,75",
    "Grace,Chemistry,82",
    "Heidi,Physics,95"
]
average = parse_grades(raw_data)
print_averages(average)
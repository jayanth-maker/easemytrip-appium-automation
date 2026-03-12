import json
import random

cities = ["Chennai", "Mumbai", "Delhi", "Bangalore"]
invalid_inputs = ["INVALIDCITY", "123ABC", ""]

test_cases = []

# Generate positive test cases
for i in range(3):

    from_city = random.choice(cities)
    to_city = random.choice(cities)

    # ensure cities are different
    while to_city == from_city:
        to_city = random.choice(cities)

    test_cases.append({
        "from_city": from_city,
        "to_city": to_city,
        "type": "positive"
    })

# Generate negative test cases
for invalid in invalid_inputs:
    test_cases.append({
        "from_city": invalid,
        "to_city": "Mumbai",
        "type": "negative"
    })

with open("test_data/ai_generated_tests.json", "w") as file:
    json.dump(test_cases, file, indent=4)

print("AI generated test cases successfully")

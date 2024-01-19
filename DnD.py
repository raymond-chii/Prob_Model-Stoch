import random 
# Question 1 

trials = 10000
count = 0 # the number of successful rolls

for _ in range(trials):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    if d1+d2+d3 == 18:
        count += 1 # when it is a success, count goes up by 1
prob = count/trials

print("part a: The probability of rolling a 18 is", prob)

for _ in range(trials):
    max_score = 0
    
    for _ in range(3):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d3 = random.randint(1, 6)
        
        score = d1 + d2 + d3
        max_score = max(max_score, score)
        
    if max_score == 18:  
        count += 1

prob = count / trials

print("part b: The probability of the fun method is", prob)

perfect_count = 0

for _ in range(trials):
    scores = []
    for _ in range(6):
        max_score = 0

        for _ in range(3):
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            d3 = random.randint(1, 6)
        
            score = d1 + d2 + d3
            max_score = max(max_score, score)

        scores.append(max_score) # add max score to list, which doesnt matter if its not 18
                                # since the perfect_count only goes up when all 6 scores are 18
    if all(score == 18 for score in scores): # check if all 6 scores are 18
        perfect_count += 1 # if so, the perfect_count goes up by 1

prob = perfect_count / trials

print("part c: The probability of the fun method and to be perfect is", prob)

average_count = 0

for _ in range(trials):
    scores = []
    for _ in range(6):
        max_score = 0

        for _ in range(3):
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            d3 = random.randint(1, 6)
        
            score = d1 + d2 + d3
            max_score = max(max_score, score)

        scores.append(max_score) 
    if all(score == 9 for score in scores): 
        average_count += 1 

prob = average_count / trials

print("part d: The probability of the fun method and to be average is", prob)



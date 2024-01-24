import random 



#### Question 1 ####
print("QUESTION 1:")
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


count = 0
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




#### Question 2 ####
print("\n\nQUESTION 2:")


averageTrollHits = (1+2+3+4)/4
# print("part a: The average number of Troll hits is", averageTrollHits)
averageFireballHits = (1+2)/2+(1+2)/2
# print("part a: The average number of fireball hits is", averageFireballHits)
count = 0
for _ in range(trials):
    d1 = random.randint(1, 2)
    d2 = random.randint(1, 2)
    if d1 + d2 > 3:
        count += 1

prob = count / trials

print("part a: The average number of Troll hit points is %d, \nand the average number of fireball hits is %d" % (averageTrollHits, averageFireballHits))
print("and the probability of getting at least 3 hits is", prob)

fireballPmf = 1/2*1 + 1/2*2 + 1/2*1 + 1/2*2
trollPmf = 1/4*1 + 1/4*2 + 1/4*3 + 1/4*4
print("part b: The PMF of Fireball is %d, and the PMF of Troll is %d" % (fireballPmf, trollPmf))

count = 0
dcount = 0
trolls = []
sumofHP = 0 
for _ in range(trials):
    wizD1 = random.randint(1, 2)
    wizD2 = random.randint(1, 2)

    trollD1 = random.randint(1, 4)
    trollD2 = random.randint(1, 4)
    trollD3 = random.randint(1, 4)
    trollD4 = random.randint(1, 4)
    trollD5 = random.randint(1, 4)
    trollD6 = random.randint(1, 4)
    trolls = [trollD1, trollD2, trollD3, trollD4, trollD5, trollD6]
    
    if (wizD1 + wizD2) >= max(trolls):
        count += 1
    
    result_list = [troll for troll in trolls if troll > (wizD1 + wizD2)]
    

    if len(result_list) == 1:
        dcount += 1
        sumofHP += result_list[0]

    
prob = count / trials
partdprob = sumofHP/dcount

print("part c: The probability of the Wizard slaying all is", prob)
print("part d: The probability of remain one troll alive of the expected HP is", partdprob)


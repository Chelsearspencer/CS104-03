numberOfScores = 0
score = 0
total = 0
average = 0.0
scoreCount = 0
numberOfScores = int(input("Please enter number of scores you want to average: "))

#What python loop structure could we use to repeat the next 3 lines
while numberOfScores > scoreCount:
    score = int(input("Please enter a test score: "))
    total = total + score
    scoreCount = scoreCount + 1 
    #If numberOfScores == scoreCount:
        #Break
    
average = (total) / numberOfScores
print("The average of the scores you entered is:")
print(average)



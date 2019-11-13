#
#
#


numJudges = 7
numCom = 0
numCompetitors =int (input ('Enter number of competitors between 3 and 16 inc...'))
numCom = numCom + numCompetitors
totalscore=0

for i in range (0, numCom-1):
    for i in range (0, numJudges):
        score = int (input("Give a score between 0 and 10.."))
        totalscore += score
    averageScore = totalscore/numJudges
    print("Score for competitor is ",averageScore)

print("The End")



	

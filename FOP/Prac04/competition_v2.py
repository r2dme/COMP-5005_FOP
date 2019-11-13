#
#
#


numJudges = 7
numCompetitors =int (input ('Enter number of competitors between 3 and 16 inc...'))
while numCompetitors<3 && numCompetitors>16:
   numCompetitors =int (input ('Enter number of competitors between 3 and 16 inc...'))

totalscore=0

for i in range (0, numCompetitors):
    for j in range (0, numJudges):
        score = int (input('Give a score between 0 and 10..'))
        totalscore += score
    averageScore = totalscore/numJudges
    print("Score for competitor ",i,"is ",averageScore)
    totalscore = 0
print("The End")



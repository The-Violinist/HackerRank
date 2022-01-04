import bisect 

ranked = [1000,990,980,970,940,560,542,432,421,400,380,350,320,300,290,280,260,250,230,200,190,160,155,150,145,140,135,130,125,120,115,110,105,100,100,50,40,40,20,10]
player = [5,25,50,120,150,190,280,350,480,600,610,700,800,900,940,990,1005]


def climbingLeaderboard(ranked, player):
    scores = []
    last = 0
    ranked = set(ranked)
    ranked = list(ranked)
    ranked.sort()
    for score in player:
        print(last)
        if score in ranked:
            scores.append(len(ranked) - ranked.index(score))
            last = ranked.index(score)
        else:
            bisect.insort(ranked, score, last, len(ranked))
            scores.append(len(ranked) - ranked.index(score))
            last = ranked.index(score)
    return scores

print(climbingLeaderboard(ranked, player))
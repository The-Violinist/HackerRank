ranked = [1000,990,980,970,940,560,542,432,421,400,380,350,320,300,290,280,260,250,230,200,190,160,155,150,145,140,135,130,125,120,115,110,105,100,100,50,40,40,20,10]
player = [5,25,50,120,150,190,280,350,480,600,610,700,800,900,940,990,1005]
def climbingLeaderboard(ranked, player):
    scores = []
    ranked = set(ranked)
    ranked = list(ranked)
    ranked.sort(reverse = True)
    last = len(ranked)
    for score in player:
        if score in ranked:
            scores.append(ranked.index(score) + 1)
            last = ranked.index(score)
        elif score not in ranked:
            for rank in reversed(ranked[:last + 1]):
                if score < rank:
                    ranked.insert(ranked.index(rank) + 1, score)
                    scores.append(ranked.index(score) + 1)
                    last = ranked.index(score)
                    break
                elif score > rank and ranked.index(rank) == 0:
                    ranked.insert(0, score)
                    scores.append(ranked.index(score) + 1)
                    last = ranked.index(score)
                    break
                else:
                    continue
    return scores

print(climbingLeaderboard(ranked,player))

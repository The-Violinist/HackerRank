ranked = [1000,990,980,970,940,560,542,432,421,400,380,350,320,300,290,280,260,250,230,200,190,160,155,150,145,140,135,130,125,120,115,110,105,100,100,50,40,40,20,10]
player = [5,25,50,120,150,190,280,350,480,600,610,700,800,900,940,990,1005]
import math
def climbingLeaderboard(ranked, player):
    scores = []
    # player_i = 0
    ranked = set(ranked)
    ranked = list(ranked)
    ranked.sort(reverse=True)
    median = math.floor(len(ranked)/2)
    for item in player:
        if all(x > item for x in ranked):
            ranked.append(item)
            scores.append(len(ranked))
        elif item in ranked:
            scores.append(ranked.index(item) + 1)
        elif item > ranked[median]:
            for rank_item in ranked:
                if item > rank_item:
                    ranked.insert(ranked.index(rank_item), item)
                    scores.append(ranked.index(rank_item))
                    break
                else:
                    continue
        elif item <= ranked[median]:
            for second_item in ranked[median:]:
                if item > second_item:
                    ranked.insert(ranked.index(second_item), item)
                    scores.append(ranked.index(second_item))
                    break
        else:
            break
    return scores

print(climbingLeaderboard(ranked,player))
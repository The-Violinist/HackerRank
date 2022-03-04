import bisect

# ranked = [100,90,90,80]
# player = [70,80,105]

# ranked = [100,100,50,40,40,20,10]
# player = [5,25,50,120]

ranked = [100,90,90,80,75,60]
player = [50,65,77,90,102]

def climbingLeaderboard(ranked, player):
    scores = []                                                                 # The final scores array
    ranked = set(ranked)                                                        # 
    ranked = list(ranked)
    ranked.sort()
    for item in player:
        if item in ranked:
            scores.append(len(ranked) - ranked.index(item))
        else:
            bisect.insort(ranked, item)
            scores.append(len(ranked) - ranked.index(item))
        print(ranked)
    return scores

print(climbingLeaderboard(ranked, player))
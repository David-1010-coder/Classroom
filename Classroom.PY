team1 = 120
team2 = 95
team3 = 140
team4 = 110
team5 = 85
 
total = team1 + team2 + team3 + team4 + team5
average = total / 5
 
print("Combined Class Points:", total)
print("Mean Team Score      :", average)
 
stars_per_point = 2
reward_stars = total * stars_per_point
print("Grand Total Stars    :", reward_stars)
 
boxes = reward_stars // 25
leftover = reward_stars % 25
 
print("Completed Star Boxes :", boxes)
print("Remaining Loose Stars:", leftover)
 
last_week = 500
 
print("Did we beat last week's record? :", total > last_week)
print("Did we tie last week's record?  :", total == last_week)
print("Did we meet or beat the record? :", total >= last_week)
 
total += 30
print("Score with Bonus Points Applied :", total)
 
total -= 15
print("Score after Penalty Deduction   :", total)
 
reward_stars = total * stars_per_point
boxes = reward_stars // 25
 
print("Final Box Count for Rewards     :", boxes)

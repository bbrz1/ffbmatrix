# Fantasy matrix

import numpy as np

# generate fake data
#fbdata = np.random.uniform(75, 150, size=(17, 10))
#fbdata = np.around(fbdata, decimals=4, out=fbdata)
#
#np.savetxt('fbdata.csv', fbdata, delimiter=",", fmt='%8.3f')

fbdata = np.loadtxt("fbdata.csv", delimiter=",", dtype=float)

print(fbdata)

week1_scores = fbdata[0]
week2_scores = fbdata[1]
week3_scores = fbdata[2]
week4_scores = fbdata[3]
week5_scores = fbdata[4]
week6_scores = fbdata[5]
week7_scores = fbdata[6]
week8_scores = fbdata[7]
week9_scores = fbdata[8]
week10_scores = fbdata[9]
week11_scores = fbdata[10]
week12_scores = fbdata[11]
week13_scores = fbdata[12]
week14_scores = fbdata[13]
week15_scores = fbdata[14]
week16_scores = fbdata[15]
week17_scores = fbdata[16]

#print(week1_scores)
#for i in range(0, len(week1_scores)):
#    print(week1_scores[i])


mask = week1_scores[:, None] > week1_scores
#print(mask[~np.eye(week1_scores.size, dtype=bool)])

mask2 = week2_scores[:, None] > week2_scores
#print(mask[~np.eye(week2_scores.size, dtype=bool)])


# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

#Split weekly wins/losses from matrix
#remove self comparisons
n = 9
wk1_recs = list(divide_chunks(mask[~np.eye(week1_scores.size, dtype=bool)], n))
wk2_recs = list(divide_chunks(mask2[~np.eye(week2_scores.size, dtype=bool)], n))
#print (wk1_recs)

tm1_wk1_rec = wk1_recs[0]
tm2_wk1_rec = wk1_recs[1]
tm3_wk1_rec = wk1_recs[2]
tm4_wk1_rec = wk1_recs[3]
tm5_wk1_rec = wk1_recs[4]
tm6_wk1_rec = wk1_recs[5]
tm7_wk1_rec = wk1_recs[6]
tm8_wk1_rec = wk1_recs[7]
tm9_wk1_rec = wk1_recs[8]
tm10_wk1_rec = wk1_recs[9]

tm1_wk2_rec = wk2_recs[0]
tm2_wk2_rec = wk2_recs[1]
tm3_wk2_rec = wk2_recs[2]
tm4_wk2_rec = wk2_recs[3]
tm5_wk2_rec = wk2_recs[4]
tm6_wk2_rec = wk2_recs[5]
tm7_wk2_rec = wk2_recs[6]
tm8_wk2_rec = wk2_recs[7]
tm9_wk2_rec = wk2_recs[8]
tm10_wk2_rec = wk2_recs[9]

#Print rec table by week
print (tm1_wk1_rec)
print (tm2_wk1_rec)
print (tm3_wk1_rec)
print (tm4_wk1_rec)
print (tm5_wk1_rec)
print (tm6_wk1_rec)
print (tm7_wk1_rec)
print (tm8_wk1_rec)
print (tm9_wk1_rec)
print (tm10_wk1_rec)

print ("")

print (tm1_wk2_rec)
print (tm2_wk2_rec)
print (tm3_wk2_rec)
print (tm4_wk2_rec)
print (tm5_wk2_rec)
print (tm6_wk2_rec)
print (tm7_wk2_rec)
print (tm8_wk2_rec)
print (tm9_wk2_rec)
print (tm10_wk2_rec)

print("")

#Count wins and losses for week 1
tm1_wk1_wins = np.count_nonzero(tm1_wk1_rec)
tm1_wk1_losses = np.size(tm1_wk1_rec) - np.count_nonzero(tm1_wk1_rec)

tm2_wk1_wins = np.count_nonzero(tm2_wk1_rec)
tm2_wk1_losses = np.size(tm2_wk1_rec) - np.count_nonzero(tm2_wk1_rec)

tm3_wk1_wins = np.count_nonzero(tm3_wk1_rec)
tm3_wk1_losses = np.size(tm3_wk1_rec) - np.count_nonzero(tm3_wk1_rec)

tm4_wk1_wins = np.count_nonzero(tm4_wk1_rec)
tm4_wk1_losses = np.size(tm4_wk1_rec) - np.count_nonzero(tm4_wk1_rec)

tm5_wk1_wins = np.count_nonzero(tm5_wk1_rec)
tm5_wk1_losses = np.size(tm5_wk1_rec) - np.count_nonzero(tm5_wk1_rec)

tm6_wk1_wins = np.count_nonzero(tm6_wk1_rec)
tm6_wk1_losses = np.size(tm6_wk1_rec) - np.count_nonzero(tm6_wk1_rec)

tm7_wk1_wins = np.count_nonzero(tm7_wk1_rec)
tm7_wk1_losses = np.size(tm7_wk1_rec) - np.count_nonzero(tm7_wk1_rec)

tm8_wk1_wins = np.count_nonzero(tm8_wk1_rec)
tm8_wk1_losses = np.size(tm8_wk1_rec) - np.count_nonzero(tm8_wk1_rec)

tm9_wk1_wins = np.count_nonzero(tm9_wk1_rec)
tm9_wk1_losses = np.size(tm9_wk1_rec) - np.count_nonzero(tm9_wk1_rec)

tm10_wk1_wins = np.count_nonzero(tm10_wk1_rec)
tm10_wk1_losses = np.size(tm10_wk1_rec) - np.count_nonzero(tm10_wk1_rec)

#Count wins and losses for week 2
tm1_wk2_wins = np.count_nonzero(tm1_wk2_rec)
tm1_wk2_losses = np.size(tm1_wk2_rec) - np.count_nonzero(tm1_wk2_rec)

tm2_wk2_wins = np.count_nonzero(tm2_wk2_rec)
tm2_wk2_losses = np.size(tm2_wk2_rec) - np.count_nonzero(tm2_wk2_rec)

tm3_wk2_wins = np.count_nonzero(tm3_wk2_rec)
tm3_wk2_losses = np.size(tm3_wk2_rec) - np.count_nonzero(tm3_wk2_rec)

tm4_wk2_wins = np.count_nonzero(tm4_wk2_rec)
tm4_wk2_losses = np.size(tm4_wk2_rec) - np.count_nonzero(tm4_wk2_rec)

tm5_wk2_wins = np.count_nonzero(tm5_wk2_rec)
tm5_wk2_losses = np.size(tm5_wk2_rec) - np.count_nonzero(tm5_wk2_rec)

tm6_wk2_wins = np.count_nonzero(tm6_wk2_rec)
tm6_wk2_losses = np.size(tm6_wk2_rec) - np.count_nonzero(tm6_wk2_rec)

tm7_wk2_wins = np.count_nonzero(tm7_wk2_rec)
tm7_wk2_losses = np.size(tm7_wk2_rec) - np.count_nonzero(tm7_wk2_rec)

tm8_wk2_wins = np.count_nonzero(tm8_wk2_rec)
tm8_wk2_losses = np.size(tm8_wk2_rec) - np.count_nonzero(tm8_wk2_rec)

tm9_wk2_wins = np.count_nonzero(tm9_wk2_rec)
tm9_wk2_losses = np.size(tm9_wk2_rec) - np.count_nonzero(tm9_wk2_rec)

tm10_wk2_wins = np.count_nonzero(tm10_wk2_rec)
tm10_wk2_losses = np.size(tm10_wk2_rec) - np.count_nonzero(tm10_wk2_rec)

#Print week 1 records
print("Week 1 records")
print("Team 1", tm1_wk1_wins, "Wins")
print("      ", tm1_wk1_losses, "Losses")

print("Team 2", tm2_wk1_wins, "Wins")
print("      ", tm2_wk1_losses, "Losses")

print("Team 3", tm3_wk1_wins, "Wins")
print("      ", tm3_wk1_losses, "Losses")

print("Team 4", tm4_wk1_wins, "Wins")
print("      ", tm4_wk1_losses, "Losses")

print("Team 5", tm5_wk1_wins, "Wins")
print("      ", tm5_wk1_losses, "Losses")

print("Team 6", tm6_wk1_wins, "Wins")
print("      ", tm6_wk1_losses, "Losses")

print("Team 7", tm7_wk1_wins, "Wins")
print("      ", tm7_wk1_losses, "Losses")

print("Team 8", tm8_wk1_wins, "Wins")
print("      ", tm8_wk1_losses, "Losses")

print("Team 9", tm9_wk1_wins, "Wins")
print("      ", tm9_wk1_losses, "Losses")

print("Team 10", tm10_wk1_wins, "Wins")
print("       ", tm10_wk1_losses, "Losses")

print("")

#Print week 2 records
print("Week 2 records")
print("Team 1", tm1_wk2_wins, "Wins")
print("      ", tm1_wk2_losses, "Losses")

print("Team 2", tm2_wk2_wins, "Wins")
print("      ", tm2_wk2_losses, "Losses")

print("Team 3", tm3_wk2_wins, "Wins")
print("      ", tm3_wk2_losses, "Losses")

print("Team 4", tm4_wk2_wins, "Wins")
print("      ", tm4_wk2_losses, "Losses")

print("Team 5", tm5_wk2_wins, "Wins")
print("      ", tm5_wk2_losses, "Losses")

print("Team 6", tm6_wk2_wins, "Wins")
print("      ", tm6_wk2_losses, "Losses")

print("Team 7", tm7_wk2_wins, "Wins")
print("      ", tm7_wk2_losses, "Losses")

print("Team 8", tm8_wk2_wins, "Wins")
print("      ", tm8_wk2_losses, "Losses")

print("Team 9", tm9_wk2_wins, "Wins")
print("      ", tm9_wk2_losses, "Losses")

print("Team 10", tm10_wk2_wins, "Wins")
print("       ", tm10_wk2_losses, "Losses")

print("")

print("Cumulative")
print("Team 1", tm1_wk1_wins + tm1_wk2_wins, "Wins")
print("      ", tm1_wk1_losses + tm1_wk2_losses, "Losses")

print("Team 2", tm2_wk1_wins + tm2_wk2_wins, "Wins")
print("      ", tm2_wk1_losses + tm2_wk2_losses, "Losses")

print("Team 3", tm3_wk1_wins + tm3_wk2_wins, "Wins")
print("      ", tm3_wk1_losses + tm3_wk2_losses, "Losses")

print("Team 4", tm4_wk1_wins + tm4_wk2_wins, "Wins")
print("      ", tm4_wk1_losses + tm4_wk2_losses, "Losses")

print("Team 5", tm5_wk1_wins + tm5_wk2_wins, "Wins")
print("      ", tm5_wk1_losses + tm5_wk2_losses, "Losses")

print("Team 6", tm6_wk1_wins + tm6_wk2_wins, "Wins")
print("      ", tm6_wk1_losses + tm6_wk2_losses, "Losses")

print("Team 7", tm7_wk1_wins + tm7_wk2_wins, "Wins")
print("      ", tm7_wk1_losses + tm7_wk2_losses, "Losses")

print("Team 8", tm8_wk1_wins + tm8_wk2_wins, "Wins")
print("      ", tm8_wk1_losses + tm8_wk2_losses, "Losses")

print("Team 9", tm9_wk1_wins + tm9_wk2_wins, "Wins")
print("      ", tm9_wk1_losses + tm9_wk2_losses, "Losses")

print("Team 10", tm10_wk1_wins + tm10_wk2_wins, "Wins")
print("       ", tm10_wk1_losses + tm10_wk2_losses, "Losses")


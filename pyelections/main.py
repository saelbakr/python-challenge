import os
import csv

csvpath = os.path.join("Election Data.csv")


Candidate = []
VoterID = []

with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#print(csvreader)


    csv_header = next(csvreader)
    ##print(f"CSV Header: {csv_header}")
    for row in csvreader:
        
        Candidate.append(row[0])
        VoterID.append(row[2])

cd_names = (list(set(Candidate)))
voter_id = (list(set(VoterID)))


#print(len(VoterID))
from collections import Counter
total_votes = dict(Counter(Candidate))


percentage = {}
for cand in total_votes :
    percent_votes = (total_votes[cand]/241032*100)
    percent = round(percent_votes,2)
    percentage[cand] = percent
#print(percentage)


full_summary = []
for name in cd_names:
    full_summary.append(f'{name} {percentage[name]}% ({total_votes[name]} votes)')

all_info = zip(full_summary)

output_path = os.path.join("Election Summary.csv")
with open(output_path, 'w') as datafile:
    csvwriter = csv.writer(datafile)


    csvwriter.writerow(["Houston Mayoral Election Results:"])
    csvwriter.writerow(["-------------------------------------"])

    csvwriter.writerow(["Total Votes:"])
    csvwriter.writerow([f'{len(VoterID)} votes'])

    csvwriter.writerow(["---------------------"])

    csvwriter.writerows(all_info)
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
print(f'Total Votes: {len(VoterID)}')

#print(len(VoterID))
from collections import Counter
total_votes = dict(Counter(Candidate))


candidate_name,integer = [],[]
percentage = {}
for cand in total_votes :
    percent_votes = (total_votes[cand]/241032*100)
    percent = round(percent_votes,2)
    percentage[cand] = percent
    integer.append(int(total_votes[cand]))
    candidate_name.append(cand)

## First Advancing Candidate:
index_advance = integer.index(max(integer))
Candidate_to_Advance = candidate_name[index_advance]
print(f'First Advancing Candidate: {Candidate_to_Advance}: {max(integer)} votes')

## Second Advancing Candidate:
second_max = []
for second in integer:
    if second != max(integer):
        second_max.append(second)

second_cand = []
for second_place in candidate_name:
    if second_place != candidate_name[index_advance]:
        second_cand.append(second_place)

index_second = second_max.index(max(second_max))
Candidate_Second_Advance = (second_cand[index_second])
print(f'Second Advancing Candidate: {Candidate_Second_Advance}: {max(second_max)} votes')


full_summary = []
for name in cd_names:
    full_summary.append(f'{name}, {percentage[name]}%, ({total_votes[name]} votes)')
    full_summary.sort()

for final in full_summary:
    print(f'{final}')
all_info = zip(full_summary)

output_path = os.path.join("Election Summary.csv")
with open(output_path, 'w') as datafile:
    csvwriter = csv.writer(datafile)


    csvwriter.writerow(["Houston Mayoral Election Results:"])
    csvwriter.writerow(["-------------------------------------"])

    csvwriter.writerow(["Total Votes:"])
    csvwriter.writerow([f'{len(VoterID)} votes'])

    csvwriter.writerow(["--------------------------------------"])

    csvwriter.writerows(all_info)
    csvwriter.writerow(["---------------------------------------"])

    csvwriter.writerow(["First Advancing Candidate: " f'{Candidate_to_Advance} ({max(integer)} votes)'])
    csvwriter.writerow(["Second Advancing Candidate: " f'{Candidate_Second_Advance} ({max(second_max)} votes)'])
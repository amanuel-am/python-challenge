# start here
import csv

# creat variables
file_path='PyPoll\Resources\election_data.csv'
print('project work')
total_votes=0
candidates=[]
candidate_votes =[]
winning_candidate =''
winning_candidate_votes=0


#open the file
with open (file_path) as election_file:
    csv_file=csv.reader(election_file)
    #skips a row in the file (first row = header row)
    next(csv_file)

    # read every row in the file
    for row in csv_file:
        total_votes += 1
        # Ballot ID,County,Candidate
        ballot_id=row[0]
        county=row[1]
        candidate=row[2]
        
        #check if candidate exist
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes.append(1)
        else:
            candidate_id= candidates.index(candidate)
            candidate_votes[candidate_id] += 1

# print result to Terminal
print('---------------------------------')
print(f'Total Votes = {total_votes}')
print('---------------------------------')
print(candidates)
print(candidate_votes)
print('---------------------------------')

# find the winning candidate
for candidate in candidates:
    current_candidate_votes = candidate_votes[candidates.index(candidate)]
    current_vote_pct= (current_candidate_votes/total_votes )*100
    print(f'{candidate}:{round(current_vote_pct,2)}% ({current_candidate_votes})')
    print('---------------------------------')
    print(f'The winning candidate is {winning_candidate}')
    print('---------------------------------')

for candidate in candidates:
    current_votes= candidate_votes[candidates.index(candidate)]
    if current_votes> winning_candidate_votes:
        winning_candidate=candidate
        winning_candidate_votes=current_votes

# print the result to file
out_file_path='PyPoll\Resources\election_data.txt'
with open (out_file_path,'w') as file_out:
    file_out.write('Election Results\n')
    file_out.write('---------------------------------\n')
    file_out.write(f'Total Votes = {total_votes}\n')
    file_out.write('---------------------------------\n')

    for candidate in candidates:
        current_candidate_votes = candidate_votes[candidates.index(candidate)]
        current_vote_pct= (current_candidate_votes/total_votes )*100
        file_out.write(f'{candidate}:{round(current_vote_pct,2)}% ({current_candidate_votes})\n')
    file_out.write('---------------------------------\n')
    file_out.write(f'Winner: {winning_candidate}\n')
    file_out.write('---------------------------------\n')

#End here

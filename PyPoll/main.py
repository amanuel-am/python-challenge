# start here
import csv

# creat variables
file_path='PyPoll\Resources\election_data.csv'
print('project work')
total_votes=0
candidates=[]
candidate_votes =[]

#open thre file
with open (file_path) as election_file:
    csv_file=csv.reader(election_file)
    #skips a row in the file (first row = header row)
    next(csv_file)
    for row in csv_file:
        #print(row)
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
            # do nothing


# print result to screen
print('---------------------------------')
print(f'Total Votes = {total_votes}')
print('---------------------------------')
print(candidates)
print(candidate_votes)
# read row in the file
# add to total votes

# print the result to file
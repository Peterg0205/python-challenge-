import os 
import csv


csvpath=os.path.join('Resources','election_data.csv')

print(csvpath)

total_vote = 0
candidate_votes = {}
candidate_list = []
votes_count = []
percentage_voted_list = []
winner = ""
winner_votes_count = 0
cleaned_output = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    file_header = next(csvreader)


    for row in csvreader:
        
        total_vote = total_vote + 1
        
        
    candidate_name = row[2]
        
        
    if candidate_name in candidate_list:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

         
    else:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 1

        
    for key, value in candidate_votes.items():
            votes_count.append(value)
            votes = candidate_votes[candidate_name]
            percentage_voted = round((int(value)/ total_vote * 100),2)
            percentage_voted_list.append(percentage_voted)

       
    if (value > winner_votes_count):
            winner_votes_count = value
            winner= key
    
    
    cleaned_output = zip(candidate_list,percentage_voted_list, votes_count)
    cleaned_output = list(cleaned_output)

    # Show the result in terminal
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes :  {total_vote}')
    print("-------------------------")
    for item in cleaned_output:
            print(f'{item[0]} : {item[1]}00% ({item[2]})')
            print("-------------------------")
            print(f'Winner : {winner}')
            print("-------------------------")

# Create an output file
    # output_file = os.path.join("pybank_ result.csv")
    # with open(output_file,"w",newline="") as datafile:
    #     writer = csv.writer(datafile)

# # Export the result as csv file
# output_file = os.path.join("pypoll_result.csv")
# with open(output_file,"w",newline="") as datafile:
#     csvwriter = csv.writer(datafile)

#     csvwriter.writerow(["Election Results"])
#     csvwriter.writerow(["-------------------------"])
#     csvwriter.writerow([f'Total Votes :  {total_vote}'])
#     csvwriter.writerow(["-------------------------"])
#     for item in cleaned_output:
#         csvwriter.writerow([f'{item[0]} : {item[1]}00% ({item[2]})'])
#     csvwriter.writerow(["-------------------------"])
#     csvwriter.writerow([f'Winner : {winner}'])
#     csvwriter.writerow(["-------------------------"])
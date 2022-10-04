import os
import csv

#declare variable
t_votes=[]
p_name=[]
d_w={}

#find csv table
polldata_csv= os.path.join('..','PyPoll','Resources','election_data.csv')

#Reading/starting the election_data
with open(polldata_csv,'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)#holds header row

#loop through the election data to read and store the values in each index
    for row in csvreader:
        tot_votes=row[0]
        t_votes.append(tot_votes)
        politician_name=row[2]
        p_name.append(politician_name)
        v_count=len(t_votes)#the total voter count

#determining votes per politician as well as vote percentage
    Charles_v=p_name.count('Charles Casper Stockham')
    Diana_v=p_name.count('Diana DeGette')
    Raymon_v=p_name.count('Raymon Anthony Doane')
    Charles_p = (Charles_v/v_count * 100)
    Diana_p =(Diana_v/v_count * 100)
    Raymon_p =(Raymon_v/v_count * 100)

#initiate dictionary for politician to their vote amount, as a key:value   
d_w={
    'Charles Casper Stockham': Charles_v,
    'Diana DeGette': Diana_v,
    'Raymon Anthony Doane': Raymon_v
    }
#Figured out how to obtain the key based on the highest value
# https://datagy.io/python-get-dictionary-key-with-max-value/#:~:text=a%20Python%20dictionary.-,How%20to%20Get%20the%20Max%20Value%20of%20a%20Python%20Dictionary,maximum%20value%20of%20any%20iterable.
highest_v=[key for key, value in d_w.items() if value == max(d_w.values())]
winner = str(highest_v)[2:-2]

#output results into terminal
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(v_count))
#round to nearest thousandth
print("Charles Casper Stockham: " + str(round(Charles_p,3)) + '% (' + str(Charles_v) + ')')
print("Diana DeGette: " + str(round(Diana_p,3)) + '% (' + str(Diana_v) + ')')
print("Raymon Anthony Doane: " + str(round(Raymon_p,3)) + '% (' + str(Raymon_v) + ')')
print('-------------------------')
print('winner: ' + winner)
print('-------------------------')

#output results into text file
file = open('PyPoll Results','w')
file.write('Election Results')
file.write('\n')
file.write('-------------------------')
file.write('\n')
file.write('Total Votes: ' + str(v_count))
file.write('\n')
file.write("Charles Casper Stockham: " + str(round(Charles_p,3)) + '% (' + str(Charles_v) + ')')
file.write('\n')
file.write("Diana DeGette: " + str(round(Diana_p,3)) + '% (' + str(Diana_v) + ')')
file.write('\n')
file.write("Raymon Anthony Doane: " + str(round(Raymon_p,3)) + '% (' + str(Raymon_v) + ')')
file.write('\n')
file.write('-------------------------')
file.write('\n')
file.write('winner: ' + winner)
file.write('\n')
file.write('-------------------------')
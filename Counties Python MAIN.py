counties = ["Arapahoe","Denver","Jefferson"]

counties_dict = {
    "Arapahoe":422829,
    "Denver":463353,
    "Jefferson":432438
}
voting_data = [
    {"county":"Arapahoe", "registered_voters" : 422829},
    {"county":"Denver", "registered_voters" : 463353},
    {"county":"Jefferson", "registered_voters" : 432438}
]

#for voters in counties_dict.values():
#    print(voters) 

#for i in range(len(counties)):
#    print(i)

#for county in counties_dict.keys():
#    print(county)

#for county in counties_dict:
#    print(counties_dict.get(county))

#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters")

#for county_dict in voting_data:
#    print(county_dict)

#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

# candidate_votes = int(input("how many votes did the candidate get in the election?"))
# total_votes = int(input("What is the total number of votes in the election?"))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes."
#     f"The total number of votes was {total_votes:,}."
#     f"You received {candidate_votes/total_votes*100:,.2f}% of the total votes."
# )

#print(message_to_candidate)

# for county, voters in voting_data.items():
#     print(f"{county} county has {voters} registered voters")

for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']} has {voting_data[i]['registered_voters']} registered voters")
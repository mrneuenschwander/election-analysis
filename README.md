# Election-Analysis
First dive into Python scripts


## Project Overview
The primary purpose of this project is to write a script capable of certifying the local congressional election for a State of Colorado Board of Elections. This project, as will be explained, may be easily modified for use in other elctions as well, making it more versatile and reliable than other methods of certification.

## Primary Objectives:
1.    Calculate the total number of votes cast.  

This was achieved by writing a section of the script to independently identify each vote as an integer - divorced from any other details - and add them to a counter that would then be displayed in the terminal and saves to the text file of results: 

![Screenshot 2022-11-20 at 3 26 49 PM](https://user-images.githubusercontent.com/116296092/202929668-9c8e6375-0fff-4474-b54c-85aa9127242f.png)

![Screenshot 2022-11-20 at 3 29 29 PM](https://user-images.githubusercontent.com/116296092/202929789-99b11cbe-c5a1-4541-9e7b-a43a058399ca.png)

![Screenshot 2022-11-20 at 3 37 43 PM](https://user-images.githubusercontent.com/116296092/202930145-9d6de804-db53-46e5-9b6a-9ed9d419c4f3.png)

2.    Get a complete list of Candidates who received votes.

This was achieved by writing a section that was able to identify and save (or assign) the name of all running Candidates to a list, that was then able to be referenced by other subsections later on: 
        
![Screenshot 2022-11-20 at 3 27 41 PM](https://user-images.githubusercontent.com/116296092/202929697-f31112fe-2160-44c7-b388-9544d2290e3c.png)

![Screenshot 2022-11-20 at 3 28 24 PM](https://user-images.githubusercontent.com/116296092/202929737-b9b67cc6-84b9-4635-ac50-602aefcd4100.png)


3.    Calculate the total number of votes each Candidate received.

Found in similar fashion to the total vote count, a section of script was created that used the same framework as previously, but added an extra line to assign the votes to each Candidate correctly as they were loaded into a Dictionary (again, to be used later as reference): 

![Screenshot 2022-11-20 at 3 31 38 PM](https://user-images.githubusercontent.com/116296092/202929868-c4a9da88-c2cc-4bab-aabd-bf987ee86efc.png)


4.    Calculate the percentage of votes each candidate won.

A simple section that took the assigned votes generated on the section above and divided them by the total votes that had been found earlier, based on section 1:

![Screenshot 2022-11-20 at 3 34 25 PM](https://user-images.githubusercontent.com/116296092/202929975-25b39f98-357a-4a7f-878f-067fd0a46712.png)


5.    Determine the winner of the election based on popular vote.

Using a few unfilled variables:
        
![Screenshot 2022-11-20 at 3 34 53 PM](https://user-images.githubusercontent.com/116296092/202929989-1f2884fa-172a-462c-bbbe-f02157a2bfb5.png)


The script takes the votes counted and stored for each candidate and compares them with the unfilled variables sequentially. If the next candidate's value is higher than the last, their numbers then take the place of the "winning" variable, and so on until a winner is decided and displayed:

![Screenshot 2022-11-20 at 3 35 38 PM](https://user-images.githubusercontent.com/116296092/202930012-a1cde54f-45d1-4e07-b578-4bdfe2882eb4.png)

![Screenshot 2022-11-20 at 3 35 55 PM](https://user-images.githubusercontent.com/116296092/202930024-33cfafd9-dc6c-4d4a-aacc-bf699a7eeba2.png)

## Resources

-   Data Source: election_results.csv
-   Software: Python 3.7.6, Visual Studio Code, 1.73.1
-   MacOS 13.0.1  
## Summary

The analysis of the election show that:
-   There were 369,711 votes cast in the election.
-   There were three (3) counties polled for voting.

The Candidates were:
-   Charles Casper Stockham
-   Diana DeGette
-   Raymon Anthony Doane

The individual candidate's results:

-   Charles Casper Stockham received 23% of the vote and 85,213 votes.
-   Diana DeGette received 73.8% of the vote and 272,892 votes.
-   Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

The winner of the election was:

-   Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Challenge Overview
    
The challenge was intended to do much the same as the rest of the script, but adds the information block that shows the individual county's voter counts, as well as the largest turnout:

![Screenshot 2022-11-20 at 3 43 30 PM](https://user-images.githubusercontent.com/116296092/202930389-f7bf5dc5-b1d6-4ef6-89c8-23b8a6784bbc.png)

![Screenshot 2022-11-20 at 3 43 44 PM](https://user-images.githubusercontent.com/116296092/202930402-0b547653-c197-48d9-852b-c486bbfe3d10.png)

![Screenshot 2022-11-20 at 3 41 31 PM](https://user-images.githubusercontent.com/116296092/202930300-ad04feed-0aa1-4068-8a3b-ae6dfd488ebb.png)

![Screenshot 2022-11-20 at 3 43 03 PM](https://user-images.githubusercontent.com/116296092/202930368-bb6b97bc-2d9e-414b-af6a-3b47616a4ce3.png)


This could be easily modified for any number of counties, in that the list and dictionary they're stored are empty until the script reads the reference file and fills them on each new run. Assuming a similarly structured .csv for future elections, this script would be recycleable indefinitely, or until such time as the voting data is collected via other means before being sent for certification.

## Challenge Summary
    
The challenge finds that of the 3 counties that voted, Denver is far and away the winner by sheer turnout. Dwarfing the other two counties, Denver alone holds 82.8% of all votes cast. The script that finds this is the same as the one that assigns votes to the Candidates 

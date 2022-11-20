# Election-Analysis
First dive into Python scripts


## Project Overview
The primary purpose of this project is to write a script capable of certifying the local congressional election for a State of Colorado Board of Elections. This project, as will be explained, may be easily modified for use in other elctions as well, making it more versatile and reliable than other methods of certification.

## Primary Objectives:
1.    Calculate the total number of votes cast.
        This was achieved by writing a section of the script to independently identify each vote as an integer - divorced from any other details - and add them to a counter that would then be displayed in the terminal and saves to the text file of results: IMAGE HERE

2.    Get a complete list of Candidates who received votes.
        This was achieved by writing a section that was able to identify and save (or assign) the name of all running Candidates to a list, that was then able to be referenced by other subsections later on: IMAGE HERE

3.    Calculate the total number of votes each Candidate received.
        Found in similar fashion to the total vote count, a section of script was created that used near identical framework as previously, but was coupled with a few extra lines to assign the votes to each Candidate correctly as they were loaded into a Dictionary (again, to be used later as reference): IMAGE HERE

4.    Calculate the percentage of votes each candidate won.
        A simple section that took the assigned votes generated on the section above and divided them by the total votes that had been found earlier, based on section 1: IMAGE HERE

5.    Determine the winner of the election based on popular vote.
        Using a few unfilled variables: IMAGE HERE

        The script takes the votes counted and stored for each candidate and compares them with the unfilled variables sequentially. If the next candidate's value is higher than the last, their numbers then take the place of the "winning" variable, and so on until a winner is decided and displayed: IMAGE HERE
 
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
-   
The individual candidate's results:
-   Charles Casper Stockham received 23% of the vote and 85,213 votes.
-   Diana DeGette received 73.8% of the vote and 272,892 votes.
-   Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

-   The winner of the election was:
-   Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Challenge Overview
    
    The challenge was intended to do much the same as the rest of the script, but adds the information block that shows the individual county's voter counts, as well as the largest turnout: IMAGE HERE

    This could be easily modified for any number of counties, in that the list they're stored in is empty until the script reads the refrence file and fills it on each new run. Assuming a similar .csv for future elections, this script would be recycleable indefinitely, or until such time as the data is collected via other means before being sent for certification.
## Challenge Summary
    
    The challenge finds that of the 3 counties that voted, Denver is far and away the winner by sheer turnout. Dwarfing the other two counties, Denver alone holds 82.8% of all votes cast. The script that finds this is the same as the one that assigns votes to the Candidates 
The full ratings data set is 100000 ratings by 943 users on 1682 items (movies). 
You must down sample the ratings.dat file first using the downSample.py. The downSample.py script will just create a smaller subset of the file ratingsData.dat with your specified data set size which can be specified by opening the file. 

ratingData.dat  
------------------------------
	This is a tab separated file representing the ratings with each line consisting of 
	         user id | item id | rating | timestamp. 
        Each user has rated at least 20 movies.  Users and items are
        numbered consecutively from 1. Ratings are either a 1,2,3,4 or 5.
	The time stamps are unix seconds since 1/1/1970 UTC The data is randomly
        ordered. 
               
movies.dat   
------------------------------
-- Information about the items (movies); this is a tab separated
              list of
              movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
              The last 19 fields are the genres, a 1 indicates the movie
              is of that genre, a 0 indicates it is not; movies can be in
              several genres at once.
              The movie ids are the ones used in the ratings.dat data set as "item id".
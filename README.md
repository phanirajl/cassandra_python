# cassandra_python
This repository has lots of useful code for working with Cassandra in python to automate queries from data files and the database once it has been loaded with information. The code assumes you have Cassandra, the Cassandra-driver which allows you to use python and python 3 installed on your computer. All programs are written in MacOS but should be compatible with windows (just make she file paths are listed correctly!)

Step 1: Launch Cassandra in your terminal (cassandra -f) *When you cassandra is running 	you will not be able to enter commands in this terminal
Step 2: Open the sampleSize.py file (located in the data folder) in a text editor and set 	numEntries to the desired numbered of entries you would like in your data set to 	use in you database. Close the file and then execute IN A DIFFERENT terminal 		window then the one one running cassandra above, navigate to the data folder and 	execute sampleSize.py (python sampleSize.py)
Step 3: Open a 3rd terminal window and log into the cassandra query language by type in 	(cqlsh) in the terminal. If Everything is working properly you should see 		something like:

	Connected to Test Cluster at 127.0.0.1.
	[cqlsh 5.0.1 | Cassandra 3.11.3 | CQL spec 3.4.4 | Native protocol v4]
	Use HELP for help.

Step 4: In the terminal window not running cassandra and not logged into the cqlsh 		language, navigate to the main cassandra_python file. Open and inspect 			setUpDatabase.py This will show you the structure of the database we are about to 	construct. In your terminal execute the file (python setUpDatabase.py). Back in 	terminal 3, if you inter the commands
		USE movRatings;
		SELECt * from uidRatedMovies;
	You will see the items which have been loaded into the table. You can do the same 	SELECT statement for the other tables. *note that cassandra is not case sensitive 	and I am only adding that for readability

Step: 5

	
	

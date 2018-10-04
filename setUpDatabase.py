#this script has all of the necessary statments to set up the test database
import os
from cassandra.cluster import Cluster

#Connect to cassandra cluster
cluster = Cluster()
session = cluster.connect()
#session.execute("CREATE KEYSPACE movRatings WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")
session.execute("use movRatings")
session.execute("CREATE TABLE uidratedMovies(uid int Primary Key, ratedMovies List<int>)")
#session.execute("CREATE TABLE ratings(entryNum int Primary Key, uid int, iid int, rating int,tstamp timestamp)")
#session.execute("CREATE TABLE userIDs(uid int PRIMARY KEY)")
#session.execute("CREATE TABLE uidRatings(uid int Primary Key, Listrating Map<int, int>, tstamp Map<int, int>)")


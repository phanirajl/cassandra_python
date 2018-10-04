import os
from cassandra.cluster import Cluster

#Connect to cassandra cluster
cluster = Cluster()
session = cluster.connect('movratings')

#primary key counter for rating entries
pk=0


        
#for each line in the data file, split it into its components and then insert it into the master rating entry table
with open("data/userData.data", "r") as source:
    for line in source:
        entry = line.strip()
        print(entry)
        entry = entry.split('\t')
        uidCur = entry[0]
        iidCur = entry[1]
        ratingCur = entry[2]
        tstampCur = entry[3]
        session.execute("UPDATE uidRatedMovies SET ratedMovies = ratedMovies + %s where uid =%s", [[int(iidCur)],int(uidCur)])
        #session.execute("UPDATE uidRatings SET iids = iids + %s rating = rating + {%s:%s}, tstamp = tstamp + {%s:%s} where uid =%s", [int(iidCur),int(iidCur),int(ratingCur),int(iidCur),int(tstampCur),int(uidCur)])
        #session.execute(insertUserIdsStatement,[uid])
        #session.execute("INSERT INTO ratings(entryNum, uid,iid,rating,tstamp) VALUES (%s,%s,%s,%s,%s)", [pk,int(entry[0]),int(entry[1]),int(entry[2]),int(entry[3])])  
        
"""
#Prepare statements
getUsersStatement = session.prepare("SELECT uid, iid, rating, tstamp FROM ratings ")
insertUserIdsStatement = session.prepare("INSERT INTO userIDs(uid) VALUES (?)")

#Transfer user id's into User id table
users = session.execute(getUsersStatement)
for user in users:
    uidCur = user.uid
    iidCur = user.iid
    ratingCur = user.rating
    tstampCur = userid.tstamp
    #session.execute(insertUserIdsStatement,[uid])
    update uidratings set rating = rating + {iidCur:ratingCur}, tstamp = tstamp +{iidCur:tstampCur} where uid =uidCur;
results = session.execute("SELECT * FROM system.local")



user_lookup_stmt = session.prepare("SELECT * FROM users WHERE user_id=?")

users = []
for user_id in user_ids_to_query:
    user = session.execute(user_lookup_stmt, [user_id])
    users.append(user)


"""

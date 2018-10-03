import os
from cassandra.cluster import Cluster

#Connect to cassandra cluster
cluster = Cluster()
session = cluster.connect('assign1')
#rows = session.execute('SELECT lastname, age, city, email, firstname FROM users')
#for user_row in rows:
 #   print(user_row.lastname+str(user_row.age)+user_row.email)
pk=0
with open("netIDs.data", "r") as source:
    for line in source:
        entry = line.strip()
        entry = entry.split('\t')
        print(repr(entry))
        session.execute("INSERT INTO netIDrate(entry, uid,iid,rating,tstamp) VALUES (%s,%s,%s,%s,%s)", [pk,int(entry[0]),int(entry[1]),int(entry[2]),int(entry[3])])  # right
        pk = pk+1

user_lookup_stmt = session.prepare("SELECT * FROM users WHERE user_id=?")

users = []
for user_id in user_ids_to_query:
    user = session.execute(user_lookup_stmt, [user_id])
    users.append(user)
#for i in data:
    #entry = data.readline()
    #entry = entry.strip()
    #entry = entry.split('\t')
    
    
    
"""
results = session.execute("SELECT * FROM system.local")
for row in results:
    process(row)



UPDATE cycling.cyclist_teams SET teams = teams + {2009 : 'DSB Bank - Nederland bloeit'} WHERE id = 5b6962dd-3f90-4c93-8f61-eabfa4a803e2;
update uidratings set ratings = ratings + {2345:2}, tstamp = tstamp +{2345:2345678} where uid =1;
with open("ratings.dat", "r") as source:
    lines = [line for line in source]
	
	
import random
random_choice = random.sample(lines, 60000)


with open("netIDs.data", "w") as sink:
    sink.write("".join(random_choice))
"""

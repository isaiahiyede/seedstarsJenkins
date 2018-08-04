from jenkinsapi.jenkins import Jenkins
import sqlite3
from datetime import datetime



""" CREATE SQLITE DATABASE """
try:
	conn = sqlite3.connect('test.db')
except:
	# table already exist
	pass


""" CREATE TABLES """
conn.execute('''CREATE TABLE TEST4
         (ID SERIAL PRIMARY KEY,
         STATUS  TEXT  NOT NULL,
         DATE_CHECKED  TEXT  NOT NULL);
         ''')

""" GET SERVER INSTANCE """
username = "YOUR JENKINS INSTANCE USERNAME"
password = "YOUR JENKINS INSTANCE PASSWORD"

def get_server_instance():
    server = Jenkins('http://localhost:8080', username='username', password='password')
    return server

	
alljobs = get_server_instance().get_jobs()
date_checked = datetime.utcnow()

for job_name, job_instance in alljobs:
	running = job_instance.is_queued_or_running()
	if not running:
	    latestBuild = job_instance.get_last_build().get_status()
	else:
		latestBuild = job_instance.get_last_build().get_status()

	try:
		conn.execute("INSERT INTO TEST4 VALUES (?,?,?)", (job_instance.name).get_last_buildnumber(), latestBuild, date_checked)
		print("Successful")
		conn.commit()
	except:
		print("something went wrong")

conn.close()




    



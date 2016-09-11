import requests
import json


def createdatabase(username,password,dbname):
	link = "https://"+username+".cloudant.com/"+dbname
	r = requests.put(link,auth=(username,password))
	return r

def delete_database(username,password,dbname):
	link = "https://"+username+".cloudant.com/"+dbname
	r = requests.delete(link,auth=(username,password))
	return r

def createdoc(username,password,dbname,doc_name, data):
	link = "https://"+username+".cloudant.com/"+dbname+"/"+doc_name
	try:	
		r = requests.put(link,auth=(username,password),headers={"content-type":"application/json"},data=json.dumps(data))
		return r
	except:
		return "error"

def getdoc(username,password,dbname,doc_name):
	link = "https://"+username+".cloudant.com/"+dbname+"/"+doc_name
	r = requests.get(link,auth=(username,password))
	return r


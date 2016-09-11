from nose.tools import *
import functions

dbname = "database1"
docname = "doc1"

#Test for creating database
def test_createdatabase():
	response1 = functions.createdatabase("songires","testdatabase",dbname)
	response2 = functions.createdatabase("songires","testdatabase",dbname)
	assert_equal(201, response1.status_code)	#database created successfully
	assert_equal(412, response2.status_code)	#database update conflict

	
#Test for creating documents in cloudant	
def test_createdoc():
	txt = {
		"a" : "ssup"
	}

	txt1 = {
		"a"
	}

	response1 = functions.createdoc("songires","testdatabase",dbname,docname,txt)
	response2 = functions.createdoc("songires","testdatabase",dbname,docname,txt)
	response3 = functions.createdoc("songires","testdatabase",dbname,"test",txt1)

	assert_equal(201, response1.status_code)	#doctument created successfully
	assert_equal(409, response2.status_code)	#document update conflict
	assert_equal("error",response3)				#data format not valid


#document retrieval test
def test_getdocument():
	response = functions.getdoc("songires","testdatabase",dbname,docname)
	response1 = functions.getdoc("songires","testdatabase","blah","blah")
	assert_equal(200, response.status_code)				#document retrieved successfully
	assert_equal(404, response1.status_code)			#document does not exist


#database deletion test
def test_delete_database():
	response1 = functions.delete_database("songires","testdatabase",dbname)
	response2 = functions.delete_database("songires","testdatabase",dbname)
	assert_equal(200, response1.status_code)		#database deleted
	assert_equal(404, response2.status_code)		#database does not exist

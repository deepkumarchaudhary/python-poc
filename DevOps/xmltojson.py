# Program to convert an xml 
# file to json file 

# import json module and xmltodict 
# module provided by python 
import json 
import xmltodict 

# open the input xml file and read 
# data in form of python dictionary 
# using xmltodict module 
with open("D:\Data\git-deep\python-poc\DevOps\emp.xml") as xml_file: 
	
	data_dict = xmltodict.parse(xml_file.read()) 
	xml_file.close() 
	
	# generate the object using json.dumps() 
	# corresponding to json data 
	
	json_data = json.dumps(data_dict)
    #print(json.dumps(json_data)) 
    #print (json_data)
        #print(json.dumps(json_data))
	
	# Write the json data to output 
	# json file 
	with open("data1.json", "w") as json_file: 
		json_file.write(json_data)
    print(json.dumps(json_data))
	json_file.close() 

#person_json = json.dumps(person_dict)
#print(person_json)
#print(person_dict['name'])
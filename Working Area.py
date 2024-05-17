#YAML
# import yaml

#write
# l_connections = [
#     {"user":"abc",
#      "db_connection":"123"},
#     {"user":"xyz",
#      "db_connection":"456"}
# ]
#
# with open(r'connections.yaml', 'w') as file:
#     document = yaml.dump(l_connections, file)


#reading
# with open(r'connections.yaml') as file:  #r' used here in order not to ignore shielding symbols
#     connections = yaml.load(file, Loader=yaml.FullLoader)
#     print(connections)
#     print(type(connections))

#################################################
#JSON
# import json
#
# #Data to be written
# dictionary = {
#     "name": "Jhon",
#     "role": "Sage",
#     "id": 13,
#     "phonenum": "123"
# }
#
# #Serializing JSON
# json_object = json.dumps(dictionary, indent=4)
#
# #Writing sample JSON
#
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)
#
#
# #Reading from JSON
# with open("sample.json", "r") as openfile:
#     json_object = json.load(openfile)
#
# print(json_object)
# print(type(json_object))

#################################################
#CSV
import pandas

l_connections = [
    {"user":"abc",
     "db_connection":"123"},
    {"user":"xyz",
     "db_connection":"456"}
]

df1 = pandas.DataFrame(l_connections)
print(df1)
print(type(df1))

df1.to_csv("from_pandas.csv", index=False)      #It is better to hide indexes not to creep csv file
                                                            #To change separator you can use sep=';'
df2 = pandas.read_csv("from_pandas.csv")
print(df2)
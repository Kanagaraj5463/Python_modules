import requests
   
# Making a GET request
r = requests.get('https://api.github.com/users/naveenkrnl')
  
# check status code for response received
# success code - 200
print(r)
q = r.text

# print content of request
#print(q['login']) 
print(id(q))

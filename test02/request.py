# _*_enconding:utf-8_*_


import requests,json

data ={'key':"111",
       'key_src':"12345",
       'data':{'nu-1':'01',
       'nu-2':'02',
       'nu-3':'03'
       }
       }

data = json.dumps(data)
s = requests.session()
a = s.post("http://192.168.9.187:88/",data=data)
print (a.text)

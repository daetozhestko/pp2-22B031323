import json
s=open('C:/Users/nurus/Desktop/tsis/tsis4/json/sample_data.json','r')
okay=s.read()
obj=json.loads(okay)
i=0
for i in range(len(obj["imdata"])):
    print(obj["imdata"][i]['l1PhysIf']["attributes"]["dn"])
    i+=1

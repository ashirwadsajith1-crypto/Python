student_data={
"id1":{"Name": "Sara","Age":"13"},
"id2":{"Name": "David","Age":"13"},
"id3":{"Name": "Sara","Age":"13"},
"id4":{"Name": "Rocky","Age":"13"},
"id5":{"Name": "Sara","Age":"13"}
}
result={}
seen_keys=[]
for i,j in student_data.items():
    uniquekey=(j["Name"],j["Age"])
    if uniquekey not in seen_keys:
        seen_keys.append(uniquekey)
        result[i]=j
for i,j in result.items():
    print(i,"-",j)


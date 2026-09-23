dictonary_scores={"Alice": 90, "Jack":92,"Sam":95,"John":80,"James":100}
length=len(dictonary_scores)
total=0
for i in (dictonary_scores.values()):
    total=total+i
avgvalue=total/length
print(f"The average value is {avgvalue}")
low=min(dictonary_scores.values())
high=max(dictonary_scores.values())
print(f"The highest score is {high} and lowest value is {low}")
name=input("Enter the person's name: ")
search=dictonary_scores.get(name,"Oops Student not found😢")
print(search)
    

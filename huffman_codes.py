

with open('shakespeare.txt') as file:
    text = ""
    for i in file:
        text+=i
        
counts = {i : text.count(i) for i in "abcdefghijklmnopqrstuvwxyz"}
total = 0 
for i in counts.keys():
    print(f"percentage of {i}: {counts[i] / sum(counts.values())*100}") 
    total+=counts[i]/sum(counts.values())*100 
print(total)
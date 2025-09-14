import re

with open("C:\\Users\\kumar\\Downloads\\KAHANI PROJECT PROJECT KI.txt" , 'r' , encoding='utf-8') as file:
    data = file.read()

    data=re.split(r'[.,!?;()<>:|\'\-]|--|\s+', data)
    data=[word.strip() for word in data if word.strip()]
# print(data[:20])
# print(len(data))

sort=sorted(set(data))
# print(sort[:20])

token={word:i for i,word in enumerate(sort)}
print(token)

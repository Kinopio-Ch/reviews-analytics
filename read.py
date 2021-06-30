data = []
count = 0               #計數器
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 #count = count + 1
        if count % 10000 == 0:     #count跟1000求餘數
            print(len(data))   #印出現在讀取到哪一行   

print(len(data))  #印出data清單加入review.txt後的清單長度

print(data[0])   #印出第一筆資料
print('---------------')
print(data[1])




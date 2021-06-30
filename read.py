data = []
count = 0               #計數器
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 #count = count + 1
        if count % 10000 == 0:     #count跟1000求餘數
            print(len(data))   #印出現在讀取到哪一行   

print('檔案讀取完了，總共有', len(data), '筆資料')  #印出data清單加入review.txt後的清單長度

#求留言平均長度
sum_len = 0  
for d in data:
    sum_len += len(d)    #長度加總
print('每筆留言平均長度:', sum_len / 1000000)



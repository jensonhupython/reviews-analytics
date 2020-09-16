# Read reviews.txt
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        #print(len(data))   #print會花很多時間
        count += 1
        if count % 1000 == 0:  # "%" 求餘數
            print(len(data))
print('檔案讀取完畢, 總共有', len(data), '筆資料')

#計算每則留言的平均長度
sum_len = 0
for d in data:
    sum_len += len(d)
print('留言的平均長度為:', sum_len/len(data))    
# Read the first data 
#print(data[0])
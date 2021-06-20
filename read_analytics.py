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

# 篩選資料
new_data = []
for new_d in data:
    if len(new_d) < 100:
        new_data.append(new_d)

#print('一共有', len(new_data), '筆留言長度小於100')
#print(new_data[0])

# Filter 'good' in message
good_data = []
for good_d in data:
    if 'good' in good_d:
        good_data.append(good_d)

print('一共有', len(good_data), '筆留言提到 good')
print('Check:')
print(good_data[0])

# 清單快寫法
good_data = [good_d for good_d in data if 'good' in good_d]

# Test
bad_data = []
bad_data = ['bad' in d for bad_d in data]
print(bad_data)


























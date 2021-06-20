# Read reviews.txt
# ch6_82
# 新增功能:
# 1.查詢某字串出現的次數
# 2.讓使用者輸入字串並且算出出現的次數
# ch6_83 import
# time
import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        #print(len(data))   #print會花很多時間
        count += 1
        bar.update(count)
        # if count % 1000 == 0:  # "%" 求餘數
        #     print(len(data))

print('檔案讀取完畢, 總共有', len(data), '筆資料')

#print(data[0])

start_time = time.time()
wc = {} # Create a dictionary: word count
        # dictionary{key:value}

for d in data:
    words = d.split()
    #print(words)
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1  #新增新的key進去 wc dictionary

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

#print(len(wc))
end_time = time.time()
print('花了', end_time-start_time, 'seconds')

while True:
    user_word = input('輸入查找的字串:')
    if user_word == 'q':
        break

    if user_word in wc:
        print(user_word,'出現過的次數', wc[user_word])
    else:
        print('這個字沒有出現過!!')

print('感謝查詢~~')

# 處理連續空白建的處理 split() 留空就是用 空格 當分割符號












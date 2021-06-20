# 利用 dictionary 做一個功能
# 功能: 可以計數某個字出現在整個留言中, 可以讓使用者輸入
import time
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

#print('檔案讀取完畢, 總共有', len(data), '筆資料')
print(data[0])

start_time = time.time()
word_count = {} 
for each_msg in data:
    words = each_msg.split(' ')
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1  #新增新的key進字典
    print(words)
    break

for key in word_count:
    #print(key, word_count[key])
    if word_count[key] > 10000000:
        print(key, word_count[key])
#print(word_count)
end_time = time.time()
print('花了', end_time - start_time, 'second')
print(len(word_count))
print(word_count['Allen'])

print('歡迎使用查找功能, 離開請輸入 q')
while True:
    user_word = input('請問你想查什麼字: ')
    if user_word == 'q':
        break;
    else:
        if user_word in word_count:
            print(user_word, '出現過的次數為: ', word_count[user_word])
        else: 
            print(user_word, '沒有出現過!!')

print('感謝使用!!')        
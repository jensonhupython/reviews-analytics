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


# Read the first data 
print(data[0])
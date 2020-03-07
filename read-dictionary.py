data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1	#count = count + 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了', '總共有', len(data), '筆資料')

print(data[0])
print(data[:3])


# 文字計數
wc = {}    # word_count
for d in data:
	words = d.split()    #預設是空白, 若用split(' ')這樣會切出空白
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1    #新增新的Key進wc字典


for word in wc:   #把wc字典裡的Key一個一個叫出來
	if wc[word] > 1000000:
		print(word, wc[word])


print(len(wc))    #字典有幾個Key
print(wc['Steven'])

while True:
	word = input('請你想查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(wc[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝您使用本查詢功能!')


# # 求每筆留言平均長度
# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)
# print('留言的平均長度為', sum_len/len(data))


# # 篩選清單內長度小於100字的留言
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言長度小於100')
# print(new[0])
# print(new[1])


# # 篩選出留言內有提到good
# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')
# print(good[0])
# print(good[1])


# # list comprehension快寫法
# good = [d for d in data if 'good' in d]     #篩選後將d加入good清單
# print(good)

# good = [d + '123' for d in data if 'good' in d]   #篩選後將d+'123'加入good清單
# print(good)

# bad = ['bad' in d for d in data if 'good' in d]   #篩選後將TURE/FALSE加入bad清單
# print(bad)

# #原始寫法
# bad = []
# for d in data :
# 	bad.append('bad' in d) #篩選後將TURE/FALSE加入bad清單
# print(bad)

# # 此為append留言內容, 並非append(Ture/False)
# bad = []
# for d in data:
# 	if 'bad' in d:
# 		bad.append(d)
# print(bad)
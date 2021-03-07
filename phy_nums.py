word_list = []
# open the file words.txt
file = open("nums.txt", "r")
# read words from words.txt and append to word_list
for word in file:
    word = word.strip('\n')
    nums = eval(word)
    word_list.append(nums)

for i in word_list:
    i += 10.0
print(word_list)

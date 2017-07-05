'''
Challenge 2: To calculate the unique elements in a list and the number of instances of each unique element.
'''

mess = open('2.txt', 'r')
mess_content = mess.read()

#to calculate the unique elements
unique = []
for i in mess_content:
    if i not in unique:
        unique.append(i)

#base dicttionary to implement counter 
count_dict = {}
j = 0
for i in unique:
        count_dict.update({i:j})
        j+= 1

#initalising the values of all the elements' counts
count_list = []
for i in range(26):
    count_list.append(0)

#counter
for k in mess_content:
    count_list[count_dict[k]] +=1

#final result printer
for l in unique:
    print('{' + l + ',' + str(count_list[count_dict[l]]) + '} ', end = "")
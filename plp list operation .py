my_list = []

#appending element in the list
my_list.append(10)
my_list.append(20)
my_list.append(30)

my_list[2] = 15

list_two = [50, 60, 70]

my_list.extend(list_two)

#removing the last item on the list
try:
    my_list.remove()  # This will cause an error
except TypeError as e:
    print(f"Error: {e}")

print(my_list)

#prnting the list in ascending order
my_list.sort()
#optional descending order
# my_list.sort(reverse=True)

#prnting the list of my_list
print(len(my_list))

#printing the index of value 30 in the liat
print(my_list[30])
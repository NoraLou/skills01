# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

##Write a function that takes a list of numbers and returns a new list with only the odd numbers.

def all_odd(number_list):
    odd_list =[]
    for i in range(len(number_list)):
        if i %2 != 0:
            odd_list.append(i)
    return odd_list

print all_odd(number_list)


# # Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    all_even =[]
    for i in range(len(number_list)):
        if i % 2 == 0:
            all_even.append(i)
    return all_even
    
print all_even(number_list)


Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):

    long_words = []

    for i in range(len(word_list)): # when are we using zero indexing...
        if len(word_list[i]) >= 4: # when are we just looking for length.....
            long_words.append(word_list[i])
    return long_words

print(long_words(word_list))

Write a function that finds the smallest element in a list of integers and returns it.

def smallest(number_list):
    for i in range(len(number_list)): #even though it is numbers it is still a LIST that needs to be converted to iterable indexes
        if number_list[i] < number_list[i]+1:
           small_one = number_list[i]


    return small_one

print(smallest(number_list))

# Write a function that finds the largest element in a list of integers and returns it.

def largest(number_list):
    biggest = 0
    for number in number_list:
        if number > biggest:
            biggest = number
    return biggest

print(largest(number_list))



# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    halvesies_list = []
    for i in range(len(number_list)):
        number_list[i] = float(number_list[i])/2
        halvesies_list.append(number_list[i])

    return halvesies_list

print(halvesies(number_list))

Write a function that takes a list of words and returns a list of all the lengths of those words.

def word_lengths(word_list):
    word_lengths_list = []
    for i in range(len(word_list)):
        word_list[i] = len(word_list[i])
        word_lengths_list.append(word_list[i])
    return word_lengths_list 

print(word_lengths(word_list))


# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sum_lis = 0
    for i in range(len(number_list)):
        sum_lis = sum_lis + number_list[i]
    return sum_lis

print(sum_numbers(number_list))

Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    multi = 1
    for i in range(len(number_list)):
        multi = multi * number_list[i]
    return multi

print mult_numbers(number_list)



# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.

def join_strings(word_list):
    word_str = ""
    for word in word_list:
        word_str = word_str + word
    return word_str

print(join_strings(word_list))



# # Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    sum = 0
    for i in range(len(number_list)):
        sum = sum + number_list[i]
    sum_avg = sum/(len(number_list))
    return sum_avg

print(average(number_list)) 





















































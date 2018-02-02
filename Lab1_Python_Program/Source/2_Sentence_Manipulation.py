import sys

print("Please enter a sentence to find middle word, longest word and reverse of each word :")
sentence = sys.stdin.readline().strip('\n')
split_sentence = sentence.split(" ")

'''
To find middle word in sentence
'''
if(len(split_sentence)%2 == 0):
    #if there are even number of words in sentence, then display middle two words
    middle_word_index = int(len(split_sentence) / 2)
    print("Middle word are :: [",split_sentence[middle_word_index-1],split_sentence[middle_word_index],"]")
else:
    # if there are odd number of words in sentence, then display middle one words
    middle_word_index = int((len(split_sentence) / 2) - 0.5)
    print("OMiddle word is :: [", split_sentence[middle_word_index], "]")

'''
To Find longest character
'''
Maxlength = 0

for x in range(0,len(split_sentence)):
    if(len(split_sentence[x])>Maxlength):
        Maxlength=len(split_sentence[x])
        longest_word=split_sentence[x]

print("Longest word is :: ",longest_word)

'''
To reverse words in sentence
'''
print("Reverse of words in sentence :: ")

for x in range(0,len(split_sentence)):
    words = split_sentence[x]
    reversed_word=words[::-1]
    split_sentence[x]=reversed_word
    print(" ",split_sentence[x],end="")
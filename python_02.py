from collections import Counter

def highest_frequency(input_string):
    # Tokenizing the string into words
    words = input_string.split()

    # Counting the frequency of each word using Counter
    word_counts = Counter(words)

    # Finding the word with the highest frequency
    most_common_word = max(word_counts, key=word_counts.get)

   
    return len(most_common_word)

# Example :
input_string = "write write write all the number from from from 1 to 100"
result = highest_frequency(input_string)
print(result)  
# Output: 5

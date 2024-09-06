words = list(input("Enter some words: ").split())
print(words)  # Testing if words work

# Initialize dictionary to store words by their starting letter
letter_dict = {}

# Process each word
for word in words:
    first_letter = word[0]  # Get the first letter
    if first_letter in letter_dict:
        letter_dict[first_letter].append(word)  # Add word to existing list
    else:
        letter_dict[first_letter] = [word]  # Create a new list for this letter

# Check and print words that start with the same letter
for key, word_list in letter_dict.items():
    if len(word_list) > 1:
        print(f"Words starting with '{key}': {word_list}")

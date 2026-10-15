
# Q1. Count vowels in a file

file = open("sample.txt", "r")
content = file.read()
file.close()

count = 0

for ch in content:
    if ch.lower() in "aeiou":
        count += 1

print("Q1: Total number of vowels:", count)


# Q2. Count lines and display 2nd and 4th line

file = open("sample.txt", "r")
lines = file.readlines()
file.close()

print("\nQ2: Total number of lines:", len(lines))

if len(lines) >= 4:
    print("Second line:", lines[1].strip())
    print("Fourth line:", lines[3].strip())
else:
    print("File must contain at least 4 lines.")


# Q3. Find the longest word in a sentence

sentence = input("\nQ3: Enter a sentence: ")

words = sentence.split()

if len(words) > 0:
    longest = max(words, key=len)
    print("List of words:", words)
    print("Longest word:", longest)
else:
    print("No words entered.")


# Q4. Count total words and print unique words

file = open("sample.txt", "r")
content = file.read()
file.close()

words = content.split()

print("\nQ4: Total number of words:", len(words))

unique_words = set(words)

print("Unique words:", unique_words)

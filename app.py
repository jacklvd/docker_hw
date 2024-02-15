import os
from collections import Counter
import socket

# a. List name of all the text file at location: /data
text_files = [f for f in os.listdir("/home/data") if f.endswith(".txt")]
print("Text files:", text_files)

# b. & c. Read the text files and count total words
total_words = 0
words_count = {}
for file in text_files:
    with open(f"/home/data/{file}", "r") as f:
        words = f.read().split()
        total_words += len(words)
        words_count[file] = len(words)

# d. List the top 3 words with maximum counts in IF.txt
with open("/home/data/IF.txt", "r") as f:
    words = f.read().split()
    most_common_words = Counter(words).most_common(3)

# e. Find the IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# f. Write all the output to a text file
with open("/home/output/result.txt", "w") as f:
    f.write(f"Text files: {text_files}\n")
    f.write(f"Total words in each file: {words_count}\n")
    f.write(f"Grand total of words: {total_words}\n")
    f.write(f"Top 3 words in IF.txt: {most_common_words}\n")
    f.write(f"IP address: {ip_address}\n")

# g. Print the information from result.txt file
with open("/home/output/result.txt", "r") as f:
    print(f.read())

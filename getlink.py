import urllib.request
# url = ("https://raw.githubusercontent.com/rasbt/"
#            "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
#            "the-verdict.txt")
# file_path = "the-verdict.txt"
# urllib.request.urlretrieve(url, file_path)
    
with open("the-verdict.txt", "r", encoding="utf-8") as f:
       raw_text = f.read()
print("Total Number of Characters: ", len(raw_text))
# print(raw_text[:99])

# tokenizing the txt
import re
text = 'Hello World! This is a sample text for tokenization.'
preprocessed = re.split(r'([,.:;?!_"()\']|--|\s)',raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))

#converting tokens into token IDs
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

# print the key-value pairs
vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
       print(item)
       if i >= 50:
              break

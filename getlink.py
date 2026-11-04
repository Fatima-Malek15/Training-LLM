import urllib.request
# url = ("https://raw.githubusercontent.com/rasbt/"
#            "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
#            "the-verdict.txt")
# file_path = "the-verdict.txt"
# urllib.request.urlretrieve(url, file_path)
    
with open("the-verdict.txt", "r", encoding="utf-8") as f:
       raw_text = f.read()
print("Total Number of Characters: ", len(raw_text))
print(raw_text[:99])

# tokenizing the txt
import re
text = "Hello World! This, is a test for tokenization."
result = re.split(r'([,.:;?!_"()\']|\s)',raw_text)
result = [item for item in result if item.strip()]
print(result[:30])

#converting tokens into token IDs


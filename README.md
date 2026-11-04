LLMs

LLMs are trained using vast amount of text data. NLP earlier made for specific araes now wide range of 
LLMs for all NLP uses for transformer architecture.

Transformer architecture allows for the LLMs to use selective attention.

custom-builter LLMs outperform general-purpose LLMs such as chat boolbergchat
data privacy concerns and confidentiality are reasons why companies may want to 
build thier own LLMs. This training is a simpe illustrative experiment, since this was my first timr
working with LLMs. LLMs can help achieve complete autonomy for devs, fine-tuning and pretraining.

Step one of training LLMs

feeding it raw data, except removing formatting, filter\applied
pretraining stage for LLMs, gpt-3 model example, then comes fine-tuning the llms.

 There are two classifications: instruction fine-tuning and classification fine-tuning.
  - instruction fine-tuning contains instruction and answer pairs
  - classiication involvles texts and associated class labels eg emails.

The transformer architecture is used to train LLMs, it was first introduced in
2017 and was initally used to translate languages.
It contains of an encoder and a decoder. The encoder processes input into vectors
while the decoder generates output text. 

Tokenzing LLMs

The print command prints the total number 
of characters followed by the first 100 characters 
of this file for illustration purposes. Our goal is to tokenize this 
20,479-character short story into individual words and special charctares.

For this, we go on a small excursion and use Python's 
regular expression library, RE, for illustration purposes.  
Using some simple example text, 
we can use the re.split command.

removing whitespaces or punctuation depends on requirenment or context of the the training.
we then need to convert the token into toekn IDs or integers, this is an 
intermediate step before converting to vectors
map unique word to integer

we convert these tokens from a Python 
string to an integer representation to produce the 
token IDs. This conversion is an intermediate 
step before converting the token IDs into embedding 
vectors. To map the previously generated tokens into 
token IDs, we have to build a vocabulary first.

This vocabulary defines how we map each unique word and 
special character to a unique integer. the purpose
illustrates the process of building a vocabulary from a training 
dataset by tokenizing the text into 
individual tokens and mapping them to unique integers.

The training set consists of only one sentence for illustration purposes. 
Tokenization breaks down the input text into individual tokens. 
The vocabulary contains all unique tokens in the training set and 
is usually sorted alphabetically.

Each unique token is mapped to a unique integer called token ID.
Now that we have tokenized Edith Wharton's short story and assigned it 
to a Python variable called preprocessed, let's create a list 
of all unique tokens and sort them alphabetically
to determine the vocabulary size. 

This code snippet calculates and prints the size of the vocabulary by 
determining the number of unique words in a preprocessed text. 
After determining that the vocabulary size is 1130 via this code, we create the vocabulary
and print its first 51 entries for illustration purposes. 

This code snippet creates a dictionary mapping words to unique integers and prints the first 51 key value pairs. 
The output is a tuple sequence mapping punctuation and words to unique integer indices for tokenization purposes. 
The dictionary contains individual tokens associated with unique integer labels. 
Our next goal is to apply this vocabulary to convert new text into token IDs.

Tokenization breaks down the training set into individual tokens. 
New tokenized sample text is mapped to token IDs using an existing vocabulary.




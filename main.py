from ngram import NGram

text = None;
with open('./data/sherlock.txt', 'r') as file:
    text = file.read()

def getNgram(ngrams, str):
    ngram = ngrams.get(str)
    if(not ngram):
       ngram = NGram(str)
       ngrams[str] = ngram;
    return ngram

def getNRgams(text, n):
    ngrams = {}
    for i in range(len(text) - (n-1)):
        ngram = getNgram(ngrams, text[i: i+(n-1)])
        ngram.add(text[i + (n-1)])
    return ngrams

def generate(ngrams, n, characters):
    text = "the quick fox jumps over the lazy dog"[0:n-1]
    for i in range(characters):
        if(1 % 10 == 0):
            print(text)
        substr = text[len(text)-(n-1):len(text)]
        text += ngrams[substr].getRand()

    return text

n = 6
print(generate(getNRgams(text, n),n, 500))

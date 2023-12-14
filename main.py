import random
from ngram import NGram
import eng_to_ipa as ipa

text = None;
with open('./data/sherlock.txt', 'r') as file:
    text = file.read()

    # text = text[1 : 200000]
    # text = ipa.convert(text);

def getNgram(ngrams, str):
    ngram = ngrams.get(str)
    if(not ngram):
       ngram = NGram(str)
       ngrams[str] = ngram;
    return ngram

def getNRgams(text, n, **kwargs):
    ngrams = {}
    for i in range(len(text) - (n-1)):
        substr = text[i: i+(n-1)]
        next = text[i + (n-1)]
        if(kwargs.get("stop_seq")):
            if(kwargs.get("stop_seq") in substr or kwargs.get("stop_seq") in next):
                continue;

        ngram = getNgram(ngrams, substr)
        ngram.add(next)
    return ngrams

def generate(ngrams, n, characters):
    built = text[0:n-1]
    i = 0
    while i < characters:
        if(1 % 10 == 0):
            print(built)
        
        while(True):
            try:
                substr = built[len(built)-(n-1):len(built)]
                rand = ngrams[substr].getRand();
                break;
            except:
                remove = random.randint(1, n * 2)
                i -= remove
                built = built[0:len(built) - (remove)]
        
        built += rand
        i += 1

    return built

n = 9
ngrams = getNRgams(text, n, stop_seq = "e")
print(generate(ngrams,n, 2000))

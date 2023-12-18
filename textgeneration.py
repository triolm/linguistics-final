
import random
from ngram import NGram


def getNgram(ngrams, str, create = False):
    ngram = ngrams.get(str)
    if(ngram):
        ngram = ngram.get("ngram")
    if(not ngram):
       ngram = NGram(str)
       ngrams[str] = {"ngram": ngram, "count": 1};
    elif(create):
        ngrams[str]["count"] += 1;
    return ngram

def getNRgams(text, n, **kwargs):
    ngrams = {}
    for i in range(len(text) - (n-1)):
        substr = text[i: i+(n-1)]
        next = text[i + (n-1)]
        if(kwargs.get("stop_seq")):
            if(kwargs.get("stop_seq") in substr.lower() or kwargs.get("stop_seq") in next.lower()):
                continue;

        ngram = getNgram(ngrams, substr, True)
        ngram.add(next)
    return ngrams

def generate(text, ngrams, n, characters):
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
            except Exception as e:
                if(i > n):
                    remove = random.randint(1, n * 2)
                    i -= remove
                    built = built[0:len(built) - (remove)]
        
        built += rand
        i += 1

    return built
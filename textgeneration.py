
import random
from ngram import NGram


def get_ngram(ngrams, str, create = False):
    ngram = ngrams.get(str)
    if(ngram):
        ngram = ngram.get("ngram")
    if(not ngram):
       ngram = NGram(str)
       ngrams[str] = {"ngram": ngram, "count": 1};
    elif(create):
        ngrams[str]["count"] += 1;
    return ngram

def get_ngrams(text, n, **kwargs):
    ngrams = {}
    for i in range(len(text) - (n-1)):
        substr = text[i: i+(n-1)]
        next = text[i + (n-1)]
        if(kwargs.get("stop_seq") and kwargs.get("stop_seq") in substr.lower()):
            continue;
        
        ngram = get_ngram(ngrams, substr, True)
            
        if (kwargs.get("stop_seq") and kwargs.get("stop_seq") in next.lower()):
            continue;

        ngram.add(next)
    return ngrams

def generate(text, ngrams, n, characters):
    built = text[0:n-1]
    i = 0
    while i < characters:
        while(True):
            try:
                substr = built[len(built)-(n-1):len(built)]
                rand = ngrams[substr].get("ngram").get_rand();
                break;
            except Exception as e:
                if(i > n):
                    remove = random.randint(1, n * 2)
                    i -= remove
                    built = built[0:len(built) - (remove)]
        built += rand
        i += 1
    return built
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

def getNRgams(text, n):
    ngrams = {}
    for i in range(len(text) - (n-1)):
        substr = text[i: i+(n-1)]
        next = text[i + (n-1)]
        ngram = getNgram(ngrams, substr)
        ngram.add(next)
    return ngrams

def generate(ngrams, n, characters):
    built = text[0:n-1]
    for i in range(characters):
        if(1 % 10 == 0):
            print(built)
        substr = built[len(built)-(n-1):len(built)]
        # rand = "e"
        # while( "e" in rand):
        rand = ngrams[substr].getRand();
        
        built += rand

    return built

n = 3
print(generate(getNRgams(text, n),n, 2000))

import time
import eng_to_ipa as ipa
from plots import *
from textgeneration import *

sourceText = "riddleywalker"
n = 4
stop_seq = "a"

def open_text_file(textName, **kwargs):
    text = None;

    with open('./data/' + sourceText + '.txt', 'r') as file:
        text = file.read()
        if(kwargs.ipa):
            text = text[1 : 200000]
            text = ipa.convert(text, stress_marks=False);

    return text;

def plot_ngrams_from(sourceText, n, nPlot, **kwargs):
    text = open_text_file(sourceText, kwargs.ipa)
    ngramStart = time.time()
    ngrams = get_ngrams(text, n, stop_seq = kwargs.stop_seq)
    print("generated ngrams in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

    return  plot_ngrams(ngrams, nPlot, omit_whitespace = kwargs.omit_whitespace,remove_highest = kwargs.remove_highest)

def plot_ngram_children_from(sourceText, parent, nPlot, **kwargs):
    text = open_text_file(sourceText, kwargs.ipa)
    ngramStart = time.time()
    ngrams = get_ngrams(text, len(parent) + 1, stop_seq = kwargs.stop_seq)
    print("generated ngrams in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

    return  plot_ngrams(get_ngram(ngrams, parent), nPlot, omit_whitespace = kwargs.omit_whitespace,remove_highest = kwargs.remove_highest)


def generate_text_from(sourceText, n, characters, **kwargs):
    text = open_text_file(sourceText, kwargs.ipa)
    
    ngramStart = time.time()
    ngrams = get_ngrams(text, n, stop_seq = kwargs.stop_seq)
    print("generated ngrams in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

    generateStart = time.time()

    out = generate(text, ngrams, n, characters if characters else 200)
    print("generated output in " + str(round((time.time() - generateStart) * 1000)) + "ms.")
    print("Finished in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

    return text


# f = open("./output/" + sourceText + ("-removed-" + stop_seq + "-" if stop_seq else "-") + str(time.time()) + ".txt", "x")
# f.write(out)
# f.close
    

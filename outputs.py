import time
import eng_to_ipa as ipa
from plots import *
from textgeneration import *
import os

def get_text_files():
    for root, dirs, files in os.walk("./data", topdown=False):
        return files

def open_text_file(textName, **kwargs):
    text = None;
    if  kwargs.get("iscustom"):
        if(len(kwargs.get("custom_text")) < 10):
            raise Exception("Custom text too short")
        text = kwargs.get("custom_text")
        #removes issues with text being very short
        if(" " in text):
            text = text + " " + text
    else:
        with open('./data/' + textName, 'r', encoding="utf8") as file:
            text = file.read()
    
    if(kwargs.get("lowercase")):
        text = text.lower();

    if(kwargs.get("ipa")):
        text = text[1 : 200000]
        text = ipa.convert(text, stress_marks=False);
    return text;

def to_ipa(text):
   converted = ""
   while(len(text)):
       converted += ipa.covert(text[0: 200000 if len(text) > 200000 else len(text)])
       text = text[text[200000 if len(text) > 200000 else len(text)]: len(text)]

def plot_ngrams_from(sourceText, n, nPlot, **kwargs):
    text = open_text_file(sourceText, ipa = kwargs.get("ipa"), custom_text = kwargs.get("custom_text"), lowercase = kwargs.get("lowercase"), iscustom = kwargs.get("iscustom"))
    ngramStart = time.time()
    ngrams = get_ngrams(text, n, stop_seq = kwargs.get("stop_seq"))
    # print("generated ngrams in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

    return plot_ngrams(ngrams, nPlot, omit_whitespace = kwargs.get("omit_whitespace"),remove_highest = kwargs.get("remove_highest"))

def plot_ngram_children_from(sourceText, parent, nPlot, **kwargs):
    text = open_text_file(sourceText, ipa = kwargs.get("ipa"), custom_text = kwargs.get("custom_text"), lowercase = kwargs.get("lowercase"), iscustom = kwargs.get("iscustom"))
    ngramStart = time.time()
    ngrams = get_ngrams(text, len(parent) + 1, stop_seq = kwargs.get("stop_seq"))
    # print("generated ngrams in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

    return plot_ngram_children(get_ngram(ngrams, parent), nPlot, omit_whitespace = kwargs.get("omit_whitespace"),remove_highest = kwargs.get("remove_highest"))


def generate_text_from(sourceText, n, characters, **kwargs):
    text = open_text_file(sourceText, ipa = kwargs.get("ipa"),custom_text = kwargs.get("custom_text"), lowercase = kwargs.get("lowercase"), iscustom = kwargs.get("iscustom"))
    
    ngramStart = time.time()
    ngrams = get_ngrams(text, n, stop_seq = kwargs.get("stop_seq"))
    # print("generated ngrams in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

    generateStart = time.time()

    out = generate(text, ngrams, n, characters if characters else 200)
    
    # print("generated output in " + str(round((time.time() - generateStart) * 1000)) + "ms.")
    # print("Finished in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

    return out


# f = open("./output/" + sourceText + ("-removed-" + stop_seq + "-" if stop_seq else "-") + str(time.time()) + ".txt", "x")
# f.write(out)
# f.close
    

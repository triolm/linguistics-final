import time
import eng_to_ipa as ipa
from plots import *
from textgeneration import *

text = None;
sourceText = "shakespeare"
n = 2
stop_seq = "a"


with open('./data/' + sourceText + '.txt', 'r') as file:
    text = file.read()
    # text = text[1 : 200000]
    # text = ipa.convert(text, stress_marks=False);

ngramStart = time.time()

ngrams = get_ngrams(text, n)
print("generated ngrams in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

plot_ngram_children(get_ngram(ngrams, "t"), 40, omitWhitespace = True)

# generateStart = time.time()
# out = generate(text, ngrams, n, 2000)
# print("generated output in " + str(round((time.time() - generateStart) * 1000)) + "ms.")
# print("Finished in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")


# f = open("./output/" + sourceText + ("-removed-" + stop_seq + "-" if stop_seq else "-") + str(time.time()) + ".txt", "x")
# f.write(out)
# f.close
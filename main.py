import time
import eng_to_ipa as ipa
from textgeneration import *
import matplotlib.pyplot as plt
import numpy as np

text = None;
sourceText = "sherlock"
n = 5
stop_seq = "a"


with open('./data/' + sourceText + '.txt', 'r') as file:
    text = file.read()
    text = text[1 : 200000]
    text = ipa.convert(text, stress_marks=False);

ngramStart = time.time()

ngrams = getNRgams(text, n, stop_seq = stop_seq)
print("generated ngrams in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")

keys = np.array(list(ngrams.keys()))
vals = np.array([i["count"] for i in ngrams.values()])

mask = vals > 200

print(len(mask))
print(len(keys))

plt.bar(keys[mask],vals[mask])
plt.xticks(rotation=90)
plt.show()

# generateStart = time.time()
# out = generate(text, ngrams, n, 2000)
# print("generated output in " + str(round((time.time() - generateStart) * 1000)) + "ms.")
# print("Finished in " + str(round((time.time() - ngramStart) * 1000)) + "ms.")


# f = open("./output/" + sourceText + ("-removed-" + stop_seq + "-" if stop_seq else "-") + str(time.time()) + ".txt", "x")
# f.write(out)
# f.close
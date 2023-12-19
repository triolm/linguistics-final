
import re
from matplotlib import pyplot as plt
import pandas as pd

def plot_ngrams(ngrams, nShow, **kwargs):
    keys = pd.array([key.replace("\n", " ") for key in ngrams.keys()])
    vals = pd.array([i["count"] for i in ngrams.values()])
    # mask = vals > 200
    return plot_dict(keys, vals, nShow, **kwargs);
 


def plot_ngram_children(ngram, nShow, **kwargs):
    keys = pd.array([key.replace("\n", " ") for key in ngram.children.keys()]) 
    vals = pd.array([i["weight"] for i in ngram.children.values()])
    return plot_dict(keys, vals, nShow, **kwargs);

    

def plot_dict(keys, vals, nShow, **kwargs):
    remove_highstes = kwargs.get("remove_highstes") if kwargs.get("remove_highstes") else 0
    
    df = pd.DataFrame(
        dict(
            keys=keys,
            vals= vals
        )
    )
    if(kwargs.get("omit_whitespace")):
        mask = [not re.match("^(.*\s+.*)+$", key) for key in df.loc[:,"keys"]]
        df = df[mask]
    df = df.sort_values('vals', ascending=False);
    df = df[remove_highstes: remove_highstes + nShow]

    plt.bar("keys", "vals", data=df)
    plt.xticks(rotation=60)
    # plt.show()
    return plt
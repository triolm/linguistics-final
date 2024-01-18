# Overview 
## Ngram Analysis
This application can generate plots to visualize the frequency of ngrams (a sequence of characters of length _n_, in this case) in input texts. The plots can visualize the textual or IPA representations of these texts.
The application can additionally visualize the frequency of characters following an inputted ngram.
## Text Generation
Using ngram data, text can be generated using the model that Claude Shannon details in his 1948 paper "A Mathematical Theory of Communication." This method uses a Markov chain that has been generated to represent the frequencies of ngrams in a text. 
A Markov chain allows us to calculate the probability of an event based on the event that occurred before it. In order to predict what the next character could be in a string, we can take the _n-1_ characters that preceed it and see which characters most often followed them in the source text. Then, we can randomly choose from these characters, weighting them based on which ones occured most often in this situation. Using this method, a sequence of characters can be generated that statistically reflect the source text.


In this application, the user can change the length of the ngrams to observe the difference it makes on the output text. I have also added features which allow the user to generate an output based on the IPA represenatation (using the Carnegie-Mellon University Pronouncing Dictionary) of a source text or to generate an output that does not include a cerain sequence of characters.


# How to Run
- Clone this repo (if it's not already downloaded) and navigate into its directory
```
git clone https://github.com/triolm/linguistics-final.git
cd linguistics-final
```
- Install required packages (preferably to a venv) with 
```
pip install -r requirements.txt
```
- Create the ./data directory (if it doesn't already exist) and add text files to analyze
- Run app (on macos) with 
```
python3 -m shiny run
```
It is additionally possible to run this application using RStudio or the Shiny for Python VS Code extension.

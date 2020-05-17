import re
from janome.tokenizer import Tokenizer as Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import sTokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer

with open("rowData.txt", "r", encoding="utf-8") as f:
    data = f.read()

data = re.sub("《[^》]+》", "", data)
data = re.sub("［[^］]+］", "", data)
data = re.sub("[｜ 　「」]", "", data)

data = data.split("。")
data = [x + "。" for x in data]

t = Tokenizer()

tokenized = []
tmp1 = []
tmp2 = []

for line in data:
    for token in t.tokenize(line):
        tmp1.append(token.surface)
        tmp2 = " ".join(tmp1)
    tokenized.append(tmp2)
    tmp1 = []

tokenized = " ".join(tokenized)

parser = PlaintextParser.from_string("".join(tokenized), sTokenizer("japanese"))

# Lex-Rank
LexRankSummarizer = LexRankSummarizer()
LexRankSummarizer.stop_words = [" "]
summary = LexRankSummarizer(document=parser.document, sentences_count=7)
print("".join(re.sub(" ", "", str(sentence)) for sentence in list(summary)))

# LSA
LsaSummarizer = LsaSummarizer()
summary = LsaSummarizer(document=parser.document, sentences_count=7)
print("".join(re.sub(" ", "", str(sentence)) for sentence in list(summary)))

# Text-Rank
TextRankSummarizer = TextRankSummarizer()
summary = TextRankSummarizer(document=parser.document, sentences_count=7)
print("".join(re.sub(" ", "", str(sentence)) for sentence in list(summary)))
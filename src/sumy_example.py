# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 2
INPUTSTRING = "Text summarization is a difficult challenge that is faced by  NLP researchers. Currently I am experimenting with a few text-summarization algorithms in my projects. One of them is LexRank. It is a graph based algorithm that uses a similarity function(cosine similarity in the original paper) to compute similarities between different sentences. It uses a pre-defined threshold to build the graph of the documents, creating an edge between 2 sentences(nodes) every time the similarity is above the threshold. They also used a Pagerank-like scheme to rank the sentences(nodes)."

if __name__ == "__main__":
    #parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    parser = PlaintextParser.from_string(INPUTSTRING, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)

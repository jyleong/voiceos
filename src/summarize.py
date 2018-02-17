from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import math

testArr = [
    'A total of 95 teams have qualified at least one athlete so far, with 92 of them expected to compete.',
    'Six nations are scheduled to make their Winter Olympics debut: Ecuador, Eritrea, Kosovo, Malaysia, Nigeria and Singapore.',
    'Athletes from the Cayman Islands, Dominica and Peru qualified to compete, however all three National Olympic Committees returned the quota spots back to the International Ski Federation (FIS).',
    "Under an agreement with North Korea, its qualified athletes are allowed to cross the Korean Demilitarized Zone into South Korea and compete in the games."
    "The two nations are scheduled to march together under the Korean Unification Flag during the opening ceremony. A Unified Korea women's ice hockey team is also competing under a separate IOC country code designation (COR); in all other sports, there is a separate North Korea team and a separate South Korea team."
    "See North Korea at the 2018 Winter Olympics for further details.",
    "On 5 December 2017 the IOC announced that the Russian Olympic Committee was suspended due to the Russian doping controversy. "
    """Individual athletes who qualified and can demonstrate they have complied with the IOC's doping regulations instead compete as "Olympic Athletes from Russia" (OAR) under a neutral flag and with the Olympic anthem played in any ceremony."""]


def summarizeArr(arr):
    txt = " ".join(arr)
    sents_count = txt.count('.')

    if sents_count == 0 and len(txt.split()) > 0:  # if there is more than one word and no periods, it is a sentence
        return txt
    else:
        summary = summarize(txt, sents_count)
        return summary


def summarize(txt, count):
    LANGUAGE = "english"
    SENTENCES_COUNT = math.ceil(math.sqrt(count))
    INPUTSTRING = txt

    parser = PlaintextParser.from_string(INPUTSTRING, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    slist = []
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        slist.append(str(sentence))

    output = " ".join(slist)

    return output


if __name__ == "__main__":
    print(summarizeArr(["Hello my name is bob"]))

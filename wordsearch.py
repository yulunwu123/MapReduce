from mrjob.job import MRJob
import re

first_word = re.compile(r"\bmagical\b", re.IGNORECASE)
second_word = re.compile(r"\bsoaring\b", re.IGNORECASE)
third_word = re.compile(r"\blopsided\b", re.IGNORECASE)


class MRWordFrequency(MRJob):
    def mapper(self, _, line):
        # yield each matched word in the line
        for word in first_word.findall(line):
            yield word.lower(), 1
        for word in second_word.findall(line):
            yield word.lower(), 1
        for word in third_word.findall(line):
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    MRWordFrequency.run()


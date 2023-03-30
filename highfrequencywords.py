from mrjob.job import MRJob
from mrjob.step import MRStep

import re

WORD_RE = re.compile(r"[\w']+")


class MRTop10Frequency(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper1,
                   reducer=self.reducer1),
            MRStep(mapper=self.mapper2,
                   reducer=self.reducer2)
        ]

    def mapper1(self, _, line):
        # yield each word in the line
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def reducer1(self, _, freq):
        yield _, sum(freq)

    def mapper2(self, _, freq):
        yield None, (freq, _,)

    def reducer2(self, _, freq_word):
        sorted_pair = sorted(freq_word, reverse=True)
        for pair in sorted_pair[0:10]:
            yield pair


if __name__ == '__main__':
    MRTop10Frequency.run()


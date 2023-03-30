"""
mrjob v0.7.4 documentation: Writing your first job
https://mrjob.readthedocs.io/en/latest/guides/quickstart.html
"""
from mrjob.job import MRJob


class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRWordFrequencyCount.run()
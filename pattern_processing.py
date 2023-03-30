from mrjob.job import MRJob


class MRIrisData(MRJob):

    def mapper(self, _, line):
        line = line.strip()
        line_split = line.split(",")
        sepal_length = line_split[0]
        sepal_width = line_split[1]
        petal_length = line_split[2]
        petal_width = line_split[3]
        classification = line_split[-1]
        yield "min sepal length", float(sepal_length)
        yield "max petal width", float(petal_width)
        if classification == "Iris-setosa":
            yield "ave sep width Iris Setosa", float(sepal_width)
        else:
            yield "diff", [float(sepal_length), float(petal_length)]

    def reducer(self, _, values):
        if _ == 'min sepal length':
            yield _, min(values)
        elif _ == "max petal width":
            yield _, max(values)
        elif _ == "ave sep width Iris Setosa":
            count = 0
            sum_sep_width = 0.0;
            for i in values:
                count += 1
                sum_sep_width += float(i)
            ave = sum_sep_width / count
            yield _, ave
        elif _ == "diff":
            count, sum_sep, sum_pet, ave_sep, ave_pet = 0, 0.0, 0.0, 0.0, 0.0
            for each in values:
                count += 1
                sep, pet = each
                sum_sep += float(sep)
                sum_pet += float(pet)
            ave_sep = sum_sep / count
            ave_pet = sum_pet / count
            diff = ave_sep - ave_pet
            yield "diff", diff


if __name__ == '__main__':
    MRIrisData.run()

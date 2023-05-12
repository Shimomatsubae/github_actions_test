import sum_array
import numpy


def main():
    array = sum_array.sum_array()
    vec1 = numpy.array([1, 2, 3])
    vec2 = numpy.array([4, 5, 6])
    array.sum_arrays(vec1=vec1, vec2=vec2)


if __name__ == "__main__":
    main()

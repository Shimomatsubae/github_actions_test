from sum_array import sum_array
import numpy


def test_sum_array():
    vec1 = numpy.array([4, 5, 6])
    vec2 = numpy.array([7, 8, 9])
    res = sum_array.sum_arrays(vec1=vec1, vec2=vec2)

    assert res == [[4, 5, 6], [7, 8, 9]]

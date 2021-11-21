from matching import matching_brackets as mb


def test_brackets():

    assert mb("[[something]]")
    assert mb("[[t]his i[s]]")
    assert mb("[[[[[[[[[[[]]]]]]]]]]]")
    assert mb("")
    assert not mb("]")
    assert not mb("[[[[[[[[[[]]]]]]]]]]]")
    assert not mb("]]][[[")


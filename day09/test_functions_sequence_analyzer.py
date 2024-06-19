import functions_sequence_analyzer as fn

def test_duplications():
    assert fn.duplications("ACCCCGTGCGATGACCCC") == "ACCCC"
    assert fn.duplications("") == ""

def test_frequency():
    assert fn.frequency("ATCG") == {'A': 25, 'T': 25, 'G': 25, 'C': 25}
    assert fn.frequency("") == {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    assert fn.frequency("AAA") == {'A': 100, 'T': 0, 'G': 0, 'C': 0}
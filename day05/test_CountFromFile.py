import FunctionsCountFromText

def test_count_characters():
    assert FunctionsCountFromText.count_characters("fekmv !2#4 -! ? 4  rr .") == 23
    assert FunctionsCountFromText.count_characters("") == 0

def test_count_words():
    assert FunctionsCountFromText.count_words("first second third 4th") == 4
    assert FunctionsCountFromText.count_words("ubuu-ibib-ibibi-bibibi-ibibi") == 1
    assert FunctionsCountFromText.count_words("") == 0

def test_count_lines():
    assert FunctionsCountFromText.count_lines("") == 0
    assert FunctionsCountFromText.count_lines("njn\nmkrmk\n") == 3


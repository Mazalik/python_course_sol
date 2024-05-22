import functions_count_from_text

def test_count_characters():
    assert functions_count_from_text.count_characters("fekmv !2#4 -! ? 4  rr .") == 23
    assert functions_count_from_text.count_characters("") == 0

def test_count_words():
    assert functions_count_from_text.count_words("first second third 4th") == 4
    assert functions_count_from_text.count_words("ubuu-ibib-ibibi-bibibi-ibibi") == 1
    assert functions_count_from_text.count_words("") == 0

def test_count_lines():
    assert functions_count_from_text.count_lines("") == 0
    assert functions_count_from_text.count_lines("njn\nmkrmk\n") == 3


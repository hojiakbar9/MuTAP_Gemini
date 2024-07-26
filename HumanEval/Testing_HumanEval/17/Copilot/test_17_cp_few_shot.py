from script_17_cp_few_shot import parse_music

def test_parse_music():
    assert parse_music("o o o o") == [4, 4, 4, 4]
    assert parse_music("o| o| o| o|") == [2, 2, 2, 2]
    assert parse_music(".| .| .| .|") == [1, 1, 1, 1]
    assert parse_music("o o| o o|") == [4, 2, 4, 2]
    assert parse_music("o| o o| o") == [2, 4, 2, 4]
    assert parse_music("o o| o| o") == [4, 2, 2, 4]
    assert parse_music("o| o| o o") == [2, 2, 4, 4]
    assert parse_music("o o o| o|") == [4, 4, 2, 2]
    assert parse_music("o| o| o| o") == [2, 2, 2, 4]
    assert parse_music("o| o o o|") == [2, 4, 4, 2]
    assert parse_music("o| o o| o") == [2, 4, 2, 4]
    assert parse_music("o o| o o") == [4, 2, 4, 4]
    assert parse_music("o o o o|") == [4, 4, 4, 2]
    assert parse_music("o o o| o") == [4, 4, 2, 4]
    assert parse_music("o| o o o") == [2, 4, 4, 4]
    assert parse_music("o o| o| o|") == [4, 2, 2, 2]
    assert parse_music("o| o| o| o|") == [2, 2, 2, 2]
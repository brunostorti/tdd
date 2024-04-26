from Media import Media

def test_media():
    result = Media.media(6, 8)
    assert result == 7

def test_media2():
    result = Media.media(5, 7)
    assert result == 6
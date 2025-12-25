# A simple function to test (this mimics your cleaning logic)
def clean_url(url):
    return url.strip()

# The test itself
def test_url_stripping():
    sample_url = "  https://google.com/image.png  \n"
    expected_output = "https://google.com/image.png"
    
    assert clean_url(sample_url) == expected_output
from plugin_template.plugin import SimpleDetector

plugin_args = {}


def test_basic():
    simple = SimpleDetector(plugin_args)
    assert simple.name() == "simple-detector"
    assert simple.needs_encryption("/simple.txt")
    assert not simple.needs_encryption("/complicated.pdf")

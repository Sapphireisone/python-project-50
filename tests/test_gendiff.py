from gendiff.modules.gendiff import gendiff


result_1 = {
    '- follow': False,
    '- host': 'hexlet.io',
    '- proxy': '123.234.53.22',
    '- timeout': 50,
}

result_2 = {
    '- follow': False,
    '  host': 'hexlet.io',
    '- proxy': '123.234.53.22',
    '- timeout': 50,
    '+ timeout': 20,
    '+ verbose': True,
}

result_3 = {
    '+ host': 'hexlet.io',
    '+ timeout': 20,
    '+ verbose': True,
}

result_4 = {
    '  follow': False,
    '  host': 'hexlet.io',
    '  proxy': '123.234.53.22',
    '  timeout': 50,
}


def test_gendiff():
    # Test function with JSON
    assert gendiff('tests/fixtures/test_file1.json', 'tests/fixtures/\
test_file3.json') == result_1
    assert gendiff('tests/fixtures/test_file1.json', 'tests/fixtures/\
test_file2.json') == result_2
    assert gendiff('tests/fixtures/test_file3.json', 'tests/fixtures/\
test_file2.json') == result_3
    assert gendiff('tests/fixtures/test_file3.json', 'tests/fixtures/\
test_file3.json') == {}
    assert gendiff('tests/fixtures/test_file1.json', 'tests/fixtures/\
test_file1.json') == result_4

    # Test function with yml
    assert gendiff('tests/fixtures/test_file1.yml', 'tests/fixtures/\
test_file3.yml') == result_1
    assert gendiff('tests/fixtures/test_file1.yml', 'tests/fixtures/\
test_file2.yml') == result_2
    assert gendiff('tests/fixtures/test_file3.yml', 'tests/fixtures/\
test_file2.yml') == result_3
    assert gendiff('tests/fixtures/test_file3.yml', 'tests/fixtures/\
test_file3.yml') == {}
    assert gendiff('tests/fixtures/test_file1.yml', 'tests/fixtures/\
test_file1.yml') == result_4

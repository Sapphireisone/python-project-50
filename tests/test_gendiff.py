from gendiff.modules.gendiff import generate_diff


result_1 = '{\n - follow: False\n - host: hexlet.io\n - proxy: 123.234.53.22\n\
 - timeout: 50\n}'

result_2 = '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n\
 - timeout: 50\n + timeout: 20\n + verbose: True\n}'

result_3 = '{\n + host: hexlet.io\n + timeout: 20\n + verbose: True\n}'

result_4 = '{\n   follow: False\n   host: hexlet.io\n   proxy: 123.234.53.22\n\
   timeout: 50\n}'


def test_gendiff():
    assert generate_diff('tests/fixtures/test_file1.json', {}) == result_1
    assert generate_diff('tests/fixtures/test_file1.json', 'tests/fixtures/\
test_file2.json') == result_2
    assert generate_diff({}, 'tests/fixtures/test_file2.json') == result_3
    assert generate_diff({}, {}) == {}
    assert generate_diff('tests/fixtures/test_file1.json', 'tests/fixtures/\
test_file1.json')

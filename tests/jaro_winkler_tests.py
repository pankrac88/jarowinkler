import pytest

from jaro import jaro_distance
from jaro import jaro_winkler_distance


class TestJaroWinklerDistance:

    # TEST CASES FROM https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
    def test_jaro(self):
        assert pytest.approx(jaro_distance('MARTHA', 'MARHTA'), 0.005) == 0.944 

    def test_jaro_winkler(self):
        assert pytest.approx(jaro_winkler_distance('MARTHA', 'MARHTA'), 0.005) == 0.961

    def test_jaro_dixon(self):
        assert pytest.approx(jaro_distance('DIXON', 'DICKSONX'), 0.005) == 0.767 

    def test_jaro_winkler_dixon(self):
        assert pytest.approx(jaro_winkler_distance('DIXON', 'DICKSONX'), 0.005) == 0.814

    def test_jaro_duane(self):
        assert pytest.approx(jaro_distance('DUANE', 'DWAYNE'), 0.005) == 0.822

    def test_jaro_winkler_duane(self):
        assert pytest.approx(jaro_winkler_distance('DUANE', 'DWAYNE'), 0.005) == 0.84

    # TEST CASES FROM http://alias-i.com/lingpipe/docs/api/com/aliasi/spell/JaroWinklerDistance.html
    def test_jaro_jones(self):
        assert pytest.approx(jaro_distance('JONES', 'JOHNSON'), 0.005) == 0.79

    def test_jaro_winkler_jones(self):
        assert pytest.approx(jaro_winkler_distance('JONES', 'JOHNSON'), 0.005) == 0.832

    def test_jaro_artificial(self):
        assert pytest.approx(jaro_distance('ABCVWXYZ', 'CABVWXYZ'), 0.005) == 0.958
        
    def test_jaro_winkler_artificial(self):
        assert pytest.approx(jaro_winkler_distance('ABCVWXYZ', 'CABVWXYZ'), 0.005) == 0.958

    # http://commons.apache.org/proper/commons-lang/apidocs/src-html/org/apache/commons/lang3/StringUtils.html#line.7141        
        

import pytest
from click.testing import CliRunner
from client import query_movie

@pytest.fixture
def runner():
    return CliRunner()

def test_query_movie(runner):
    result = runner.invoke(query_movie, ['Mine 9'])
    assert result.exit_code == 0
    assert 'show_id' in result.output
    assert 'title: Mine 9' in result.output


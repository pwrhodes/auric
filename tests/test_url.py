"""Test the URL class."""
from collections import namedtuple

import pytest

from auric import URL

TEST_HOSTNAME = "auric.test"

UrlInput = namedtuple("UrlInput", ["input_value", "expected_result"])


def test_url():
    """Test basic initialisation of url and presence of attribute."""
    my_url = URL(hostname=TEST_HOSTNAME)
    assert hasattr(my_url, "as_string")


def test_required_args__url():
    """Test basic initialisation of url without required argument."""
    with pytest.raises(TypeError):
        URL()  # pylint: disable=no-value-for-parameter


@pytest.mark.parametrize(
    "protocol",
    [
        UrlInput(input_value="https", expected_result=True),
        UrlInput(input_value="http", expected_result=True),
        UrlInput(input_value="test", expected_result=False),
    ],
)
def test_protocols__url(protocol):
    """Test initialisation of url various protocols."""
    if protocol.expected_result:
        URL(hostname=TEST_HOSTNAME, protocol=protocol.input_value)
    if not protocol.expected_result:
        with pytest.raises(ValueError):
            URL(hostname=TEST_HOSTNAME, protocol=protocol.input_value)


def test_str__url():
    """Test as_string result type."""
    my_url = URL(hostname=TEST_HOSTNAME)
    result = str(my_url)
    assert isinstance(result, str)


def test_as_string__url():
    """Test as_string result type."""
    my_url = URL(hostname=TEST_HOSTNAME)
    result = my_url.as_string()
    assert isinstance(result, str)


def test_string_consistency__url():
    """Test as_string result type."""
    my_url = URL(hostname=TEST_HOSTNAME)
    as_string_result = my_url.as_string()
    str_result = str(my_url)
    assert as_string_result == str_result


def test_as_string_content__url():
    """Test contents of url as_string with no optional arguments."""
    my_url = URL(hostname=TEST_HOSTNAME)
    result = my_url.as_string()
    assert result == TEST_HOSTNAME


def test_as_string_content_protocol__url():
    """Test contents of url as_string with protocol argument."""
    protocol = "https"
    my_url = URL(hostname=TEST_HOSTNAME, protocol=protocol)
    result = my_url.as_string()
    assert protocol in result


def test_as_string_content_port__url():
    """Test contents of url as_string with protocol argument."""
    port = 443
    my_url = URL(hostname=TEST_HOSTNAME, port=port)
    result = my_url.as_string()
    assert str(port) in result


def test_as_string_content_path__url():
    """Test contents of url as_string with protocol argument."""
    path = "test"
    my_url = URL(hostname=TEST_HOSTNAME, path=path)
    result = my_url.as_string()
    assert path in result


def test_as_string_content_query__url():
    """Test contents of url as_string with protocol argument."""
    query = "test"
    my_url = URL(hostname=TEST_HOSTNAME, query=query)
    result = my_url.as_string()
    assert query in result


# TODO: Test the order of URL attributes in string

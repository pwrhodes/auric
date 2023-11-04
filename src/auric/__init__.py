"""auric module."""
from auric.valid_values import PROTOCOLS


# pylint: disable=too-many-arguments,too-many-instance-attributes
class URL:  # dead: disable
    """Contains a URL and all it's components."""

    @property
    def protocol(self) -> str:
        """Returns the protocol."""
        if self._protocol:
            return self._protocol
        return ""

    @protocol.setter
    def protocol(self, set_protocol) -> None:
        """Contains the protocol."""
        if set_protocol:
            if set_protocol not in PROTOCOLS:
                raise ValueError("Invalid protocol provoded")
        self._protocol = set_protocol

    @property
    def hostname(self) -> str:
        """Returns the hostname."""
        return self._hostname

    @hostname.setter
    def hostname(self, set_hostname) -> None:
        """Sets the hostname."""
        self._hostname = set_hostname

    @property
    def port(self) -> str:
        """Returns the port."""
        if self._port:
            return self._port
        return ""

    @port.setter
    def port(self, set_port) -> None:
        """Sets the port."""
        self._port = set_port

    @property
    def path(self) -> str:
        """Contains the path."""
        if self._path:
            return self._path
        return ""

    @path.setter
    def path(self, set_path) -> None:
        """Sets the path."""
        self._path = set_path

    @property
    def query(self) -> str:
        """Contains the query."""
        if self._query:
            return self._query
        return ""

    @query.setter
    def query(self, set_query) -> None:
        """Sets the query."""
        self._query = set_query

    def __init__(self, hostname, protocol=None, port=None, path=None, query=None):
        """Initialise the instance."""
        self.hostname = hostname
        self.protocol = protocol
        self.port = port
        self.path = path
        self.query = query

    def as_string(self) -> str:  # dead: disable
        """Render the URL as a string."""
        url = self.hostname
        if self.protocol:
            url = url + "://" + self.protocol
        if self.port:
            url = url + ":" + str(self.port)
        if self.path:
            url = url + "/" + self.path
        if self.query:
            url = url + "?" + self.query
        return url

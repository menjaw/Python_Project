import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None):
    """Download a remote file specified by a URL to a
    local directory.

    :param url: str
      URL pointing to a remote file.

    :param to: str
      Local path, absolute or relative, with a filename
      to the file storing the contents of the remote file.
    """

    # TODO: Implement me!
    if to:
        localfile = to
    else:
        filename = os.path.basename(urlparse(url).path)
        localfile = os.path.join(".", filename)

    print("Downloading file to {}".format(localfile))

    if not os.path.isfile(localfile):
        req.urlretrieve(url, localfile)

    return localfile
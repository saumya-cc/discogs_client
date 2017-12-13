from __future__ import absolute_import, division, print_function, unicode_literals

__version_info__ = 2, 2, 1
__version__ = '2.2.1'

from discogs_client_cloudcar.client import Client
from discogs_client_cloudcar.models import Artist, Release, Master, Label, User, \
    Listing, Track, Price, Video

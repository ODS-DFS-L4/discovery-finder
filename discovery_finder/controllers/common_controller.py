import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from discovery_finder.models.version_availability_read import VersionAvailabilityRead  # noqa: E501
from discovery_finder import util


def read_version_availability_v1_api_version_availability_get():  # noqa: E501
    """Read Version Availability

    Get the status of the discovery service and software version. # noqa: E501


    :rtype: Union[VersionAvailabilityRead, Tuple[VersionAvailabilityRead, int], Tuple[VersionAvailabilityRead, int, Dict[str, str]]
    """
    return 'do some magic!'

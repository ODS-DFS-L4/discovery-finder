import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from discovery_finder.models.discovery_finder import DiscoveryServiceDB  # noqa: E501
from discovery_finder.models.discovery_service_list_read import DiscoveryServiceListRead  # noqa: E501
from discovery_finder.models.http_validation_error import HTTPValidationError  # noqa: E501
from discovery_finder.models.single_discovery_service_detail import SingleDiscoveryServiceDetail  # noqa: E501
from discovery_finder import util


def create_discovery_service_v1_api_discovery_finder_discovery_services_post(body):  # noqa: E501
    """Create a new discovery service URL

    Create a new discovery service url with details like region and application type. # noqa: E501

    :param single_discovery_service_detail: 
    :type single_discovery_service_detail: dict | bytes

    :rtype: Union[SingleDiscoveryServiceDetail, Tuple[SingleDiscoveryServiceDetail, int], Tuple[SingleDiscoveryServiceDetail, int, Dict[str, str]]
    """
    discovery_service = body
    # if connexion.request.is_json:
        # discovery_service = DiscoveryService.from_dict(connexion.request.get_json())  # noqa: E501
    db = DiscoveryServiceDB()
    db.create(body['domain'], body['url'])
    return {
        'domain': body['domain'],
        'url': body['url']}


def delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete(url_id):  # noqa: E501
    """Delete Discovery Service

    Deletes a discovery service URL from the database. This asynchronous function removes a discovery service URL from the database session provided.  Args:     db_session (DBSessionDep): The database session dependency.     url_id (int): The ID of the discovery service URL to be deleted.  Returns:     dict: A dictionary containing the status of the deletion operation. # noqa: E501

    :param url_id: 
    :type url_id: str
    :type url_id: str

    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_discovery_services_v1_api_discovery_finder_discovery_services_get(url_id):  # noqa: E501
    """Get Discovery Services

    Fetches discovery service URLs from the database. This asynchronous function retrieves a list of discovery service URLs from the database session provided.

    Returns:     list: A list of discovery service URLs and their details. # noqa: E501

    :param url_id: 
    :type url_id: str

    :rtype: Union[DiscoveryServiceListRead, Tuple[DiscoveryServiceListRead, int], Tuple[DiscoveryServiceListRead, int, Dict[str, str]]
    """
    db = DiscoveryServiceDB()
    url_list = db.get(url_id)
    return {'available_services': [{
        'url': url,
        'domain': domain
        } for url, domain in url_list]}

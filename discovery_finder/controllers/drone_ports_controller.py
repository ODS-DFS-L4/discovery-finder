import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from discovery_finder.models.create_or_update_drone_port_reference_response import CreateOrUpdateDronePortReferenceResponse  # noqa: E501
from discovery_finder.models.delete_drone_port_reference_response import DeleteDronePortReferenceResponse  # noqa: E501
from discovery_finder.models.http_validation_error import HTTPValidationError  # noqa: E501
from discovery_finder.models.put_drone_port_reference_parameters import PutDronePortReferenceParameters  # noqa: E501
from discovery_finder.models.query_drone_port_reference_parameters import QueryDronePortReferenceParameters  # noqa: E501
from discovery_finder.models.query_drone_port_reference_response import QueryDronePortReferenceResponse  # noqa: E501
from discovery_finder import util


def delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete(port_id):  # noqa: E501
    """Delete Drone Port Reference

    Deletes a drone port reference by its port ID. # noqa: E501

    :param port_id: 
    :type port_id: str
    :type port_id: str

    :rtype: Union[DeleteDronePortReferenceResponse, Tuple[DeleteDronePortReferenceResponse, int], Tuple[DeleteDronePortReferenceResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_drone_port_details_v1_api_managed_corridors_ports_port_id_get(port_id):  # noqa: E501
    """Get drone port reference details

    Retrieve details of a specific drone port by its ID. # noqa: E501

    :param port_id: The ID of the drone port to retrieve.
    :type port_id: str
    :type port_id: str

    :rtype: Union[CreateOrUpdateDronePortReferenceResponse, Tuple[CreateOrUpdateDronePortReferenceResponse, int], Tuple[CreateOrUpdateDronePortReferenceResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def search_drone_ports_v1_api_managed_corridors_ports_query_post(body, supports_drone_type=None, usage_type=None, port_type=None, manufacturer=None):  # noqa: E501
    """Query Drone ports

    Query all the drone ports in an area of interest. # noqa: E501

    :param query_drone_port_reference_parameters: 
    :type query_drone_port_reference_parameters: dict | bytes
    :param supports_drone_type: 
    :type supports_drone_type: str
    :param usage_type: 
    :type usage_type: int
    :param port_type: 
    :type port_type: int
    :param manufacturer: 
    :type manufacturer: str

    :rtype: Union[List[QueryDronePortReferenceResponse], Tuple[List[QueryDronePortReferenceResponse], int], Tuple[List[QueryDronePortReferenceResponse], int, Dict[str, str]]
    """
    query_drone_port_reference_parameters = body
    if connexion.request.is_json:
        query_drone_port_reference_parameters = QueryDronePortReferenceParameters.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put(port_id, body):  # noqa: E501
    """Upsert Drone Port Reference

    Upsert (update or insert) a drone port reference. This function handles the creation or updating of a drone port reference based on the provided payload and port ID. If the drone port is created, the response status code is set to 201. # noqa: E501

    :param port_id: 
    :type port_id: str
    :type port_id: str
    :param put_drone_port_reference_parameters: 
    :type put_drone_port_reference_parameters: dict | bytes

    :rtype: Union[CreateOrUpdateDronePortReferenceResponse, Tuple[CreateOrUpdateDronePortReferenceResponse, int], Tuple[CreateOrUpdateDronePortReferenceResponse, int, Dict[str, str]]
    """
    put_drone_port_reference_parameters = body
    if connexion.request.is_json:
        put_drone_port_reference_parameters = PutDronePortReferenceParameters.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

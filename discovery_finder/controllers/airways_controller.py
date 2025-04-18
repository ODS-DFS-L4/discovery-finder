import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from discovery_finder.models.delete_airway_definition_response import DeleteAirwayDefinitionResponse  # noqa: E501
from discovery_finder.models.http_validation_error import HTTPValidationError  # noqa: E501
from discovery_finder.models.put_airway_definition_parameters import PutAirwayDefinitionParameters  # noqa: E501
from discovery_finder.models.query_airway_definition_parameters import QueryAirwayDefinitionParameters  # noqa: E501
from discovery_finder.models.query_single_airway_definition_response import QuerySingleAirwayDefinitionResponse  # noqa: E501
from discovery_finder.models.single_airway_definition_response import SingleAirwayDefinitionResponse  # noqa: E501
from discovery_finder.models.upsert_airway_definition_response_public import UpsertAirwayDefinitionResponsePublic  # noqa: E501
from discovery_finder import util


def create_airway_v1_api_aerial_corridors_airways_airway_id_put(airway_id, body):  # noqa: E501
    """Create or update an airway by ID

    A new airway is created or an existing one is updated by providing the airway ID and the new airway definition, which includes the airway name, junctions, and sections. The operation is idempotent. # noqa: E501

    :param airway_id: 
    :type airway_id: str
    :type airway_id: str
    :param put_airway_definition_parameters: 
    :type put_airway_definition_parameters: dict | bytes

    :rtype: Union[UpsertAirwayDefinitionResponsePublic, Tuple[UpsertAirwayDefinitionResponsePublic, int], Tuple[UpsertAirwayDefinitionResponsePublic, int, Dict[str, str]]
    """
    put_airway_definition_parameters = body
    if connexion.request.is_json:
        put_airway_definition_parameters = PutAirwayDefinitionParameters.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_airway_v1_api_aerial_corridors_airways_airway_id_delete(airway_id):  # noqa: E501
    """Delete an airway by ID

    Delete an airway from the ICDS by providing the airway ID. # noqa: E501

    :param airway_id: 
    :type airway_id: str
    :type airway_id: str

    :rtype: Union[DeleteAirwayDefinitionResponse, Tuple[DeleteAirwayDefinitionResponse, int], Tuple[DeleteAirwayDefinitionResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get(airway_id):  # noqa: E501
    """Get details of a single airway by ID

    Retrieve details of a specific airway by its ID. # noqa: E501

    :param airway_id: The ID of the airway to retrieve.
    :type airway_id: str
    :type airway_id: str

    :rtype: Union[SingleAirwayDefinitionResponse, Tuple[SingleAirwayDefinitionResponse, int], Tuple[SingleAirwayDefinitionResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def search_for_airways_v1_api_aerial_corridors_airways_query_post(body):  # noqa: E501
    """Query airways 

    This endpoint allows querying section of airways based on the area of interest. Although it uses request.POST, no changes are made to the database. The POST method is used instead of GET because GET does not support passing body parameters for querying. # noqa: E501

    :param query_airway_definition_parameters: 
    :type query_airway_definition_parameters: dict | bytes

    :rtype: Union[List[QuerySingleAirwayDefinitionResponse], Tuple[List[QuerySingleAirwayDefinitionResponse], int], Tuple[List[QuerySingleAirwayDefinitionResponse], int, Dict[str, str]]
    """
    query_airway_definition_parameters = body
    if connexion.request.is_json:
        query_airway_definition_parameters = QueryAirwayDefinitionParameters.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

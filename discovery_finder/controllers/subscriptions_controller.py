import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from discovery_finder.models.create_or_update_subscription_response import CreateOrUpdateSubscriptionResponse  # noqa: E501
from discovery_finder.models.delete_subscription_response import DeleteSubscriptionResponse  # noqa: E501
from discovery_finder.models.http_validation_error import HTTPValidationError  # noqa: E501
from discovery_finder.models.put_subscription_parameters import PutSubscriptionParameters  # noqa: E501
from discovery_finder.models.query_subscription_parameters import QuerySubscriptionParameters  # noqa: E501
from discovery_finder import util


def delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete(subscription_id):  # noqa: E501
    """Delete Subscription

    Delete a subscription by its ID. # noqa: E501

    :param subscription_id: 
    :type subscription_id: str
    :type subscription_id: str

    :rtype: Union[DeleteSubscriptionResponse, Tuple[DeleteSubscriptionResponse, int], Tuple[DeleteSubscriptionResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get(subscription_id):  # noqa: E501
    """Get Subscription details

    Retrieve details of a specific subscription by its ID. # noqa: E501

    :param subscription_id: The ID of the subscription to retrieve.
    :type subscription_id: str
    :type subscription_id: str

    :rtype: Union[CreateOrUpdateSubscriptionResponse, Tuple[CreateOrUpdateSubscriptionResponse, int], Tuple[CreateOrUpdateSubscriptionResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def search_subscriptions_v1_api_managed_corridors_subscriptions_query_post(body):  # noqa: E501
    """Query Subscriptions

    Query subscriptions in an area of interest. # noqa: E501

    :param query_subscription_parameters: 
    :type query_subscription_parameters: dict | bytes

    :rtype: Union[List[CreateOrUpdateSubscriptionResponse], Tuple[List[CreateOrUpdateSubscriptionResponse], int], Tuple[List[CreateOrUpdateSubscriptionResponse], int, Dict[str, str]]
    """
    query_subscription_parameters = body
    if connexion.request.is_json:
        query_subscription_parameters = QuerySubscriptionParameters.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put(subscription_id, body):  # noqa: E501
    """Upsert Subscription

    Upsert a subscription. This endpoint creates a new subscription or updates an existing one based on the provided subscription ID. # noqa: E501

    :param subscription_id: 
    :type subscription_id: str
    :type subscription_id: str
    :param put_subscription_parameters: 
    :type put_subscription_parameters: dict | bytes

    :rtype: Union[CreateOrUpdateSubscriptionResponse, Tuple[CreateOrUpdateSubscriptionResponse, int], Tuple[CreateOrUpdateSubscriptionResponse, int, Dict[str, str]]
    """
    put_subscription_parameters = body
    if connexion.request.is_json:
        put_subscription_parameters = PutSubscriptionParameters.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

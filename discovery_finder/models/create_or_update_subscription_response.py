from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from discovery_finder.models.base_model import Model
from discovery_finder.models.subscription_base import SubscriptionBase
from discovery_finder import util

from discovery_finder.models.subscription_base import SubscriptionBase  # noqa: E501

class CreateOrUpdateSubscriptionResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, subscription_details=None):  # noqa: E501
        """CreateOrUpdateSubscriptionResponse - a model defined in OpenAPI

        :param id: The id of this CreateOrUpdateSubscriptionResponse.  # noqa: E501
        :type id: str
        :param subscription_details: The subscription_details of this CreateOrUpdateSubscriptionResponse.  # noqa: E501
        :type subscription_details: SubscriptionBase
        """
        self.openapi_types = {
            'id': str,
            'subscription_details': SubscriptionBase
        }

        self.attribute_map = {
            'id': 'id',
            'subscription_details': 'subscription_details'
        }

        self._id = id
        self._subscription_details = subscription_details

    @classmethod
    def from_dict(cls, dikt) -> 'CreateOrUpdateSubscriptionResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateOrUpdateSubscriptionResponse of this CreateOrUpdateSubscriptionResponse.  # noqa: E501
        :rtype: CreateOrUpdateSubscriptionResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this CreateOrUpdateSubscriptionResponse.


        :return: The id of this CreateOrUpdateSubscriptionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CreateOrUpdateSubscriptionResponse.


        :param id: The id of this CreateOrUpdateSubscriptionResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def subscription_details(self) -> SubscriptionBase:
        """Gets the subscription_details of this CreateOrUpdateSubscriptionResponse.


        :return: The subscription_details of this CreateOrUpdateSubscriptionResponse.
        :rtype: SubscriptionBase
        """
        return self._subscription_details

    @subscription_details.setter
    def subscription_details(self, subscription_details: SubscriptionBase):
        """Sets the subscription_details of this CreateOrUpdateSubscriptionResponse.


        :param subscription_details: The subscription_details of this CreateOrUpdateSubscriptionResponse.
        :type subscription_details: SubscriptionBase
        """
        if subscription_details is None:
            raise ValueError("Invalid value for `subscription_details`, must not be `None`")  # noqa: E501

        self._subscription_details = subscription_details

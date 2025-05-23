from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from discovery_finder.models.base_model import Model
from discovery_finder.models.airway_output import AirwayOutput
from discovery_finder import util

from discovery_finder.models.airway_output import AirwayOutput  # noqa: E501

class UpsertAirwayDefinitionResponsePublic(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, airway=None):  # noqa: E501
        """UpsertAirwayDefinitionResponsePublic - a model defined in OpenAPI

        :param airway: The airway of this UpsertAirwayDefinitionResponsePublic.  # noqa: E501
        :type airway: AirwayOutput
        """
        self.openapi_types = {
            'airway': AirwayOutput
        }

        self.attribute_map = {
            'airway': 'airway'
        }

        self._airway = airway

    @classmethod
    def from_dict(cls, dikt) -> 'UpsertAirwayDefinitionResponsePublic':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpsertAirwayDefinitionResponsePublic of this UpsertAirwayDefinitionResponsePublic.  # noqa: E501
        :rtype: UpsertAirwayDefinitionResponsePublic
        """
        return util.deserialize_model(dikt, cls)

    @property
    def airway(self) -> AirwayOutput:
        """Gets the airway of this UpsertAirwayDefinitionResponsePublic.


        :return: The airway of this UpsertAirwayDefinitionResponsePublic.
        :rtype: AirwayOutput
        """
        return self._airway

    @airway.setter
    def airway(self, airway: AirwayOutput):
        """Sets the airway of this UpsertAirwayDefinitionResponsePublic.


        :param airway: The airway of this UpsertAirwayDefinitionResponsePublic.
        :type airway: AirwayOutput
        """
        if airway is None:
            raise ValueError("Invalid value for `airway`, must not be `None`")  # noqa: E501

        self._airway = airway

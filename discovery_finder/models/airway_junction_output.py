from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from discovery_finder.models.base_model import Model
from discovery_finder.models.airway_junction_detail_output import AirwayJunctionDetailOutput
from discovery_finder import util

from discovery_finder.models.airway_junction_detail_output import AirwayJunctionDetailOutput  # noqa: E501

class AirwayJunctionOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, type=None, airways=None):  # noqa: E501
        """AirwayJunctionOutput - a model defined in OpenAPI

        :param id: The id of this AirwayJunctionOutput.  # noqa: E501
        :type id: str
        :param name: The name of this AirwayJunctionOutput.  # noqa: E501
        :type name: str
        :param type: The type of this AirwayJunctionOutput.  # noqa: E501
        :type type: str
        :param airways: The airways of this AirwayJunctionOutput.  # noqa: E501
        :type airways: List[AirwayJunctionDetailOutput]
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'type': str,
            'airways': List[AirwayJunctionDetailOutput]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'airways': 'airways'
        }

        self._id = id
        self._name = name
        self._type = type
        self._airways = airways

    @classmethod
    def from_dict(cls, dikt) -> 'AirwayJunctionOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AirwayJunction-Output of this AirwayJunctionOutput.  # noqa: E501
        :rtype: AirwayJunctionOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this AirwayJunctionOutput.


        :return: The id of this AirwayJunctionOutput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this AirwayJunctionOutput.


        :param id: The id of this AirwayJunctionOutput.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this AirwayJunctionOutput.


        :return: The name of this AirwayJunctionOutput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AirwayJunctionOutput.


        :param name: The name of this AirwayJunctionOutput.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self) -> str:
        """Gets the type of this AirwayJunctionOutput.


        :return: The type of this AirwayJunctionOutput.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this AirwayJunctionOutput.


        :param type: The type of this AirwayJunctionOutput.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def airways(self) -> List[AirwayJunctionDetailOutput]:
        """Gets the airways of this AirwayJunctionOutput.


        :return: The airways of this AirwayJunctionOutput.
        :rtype: List[AirwayJunctionDetailOutput]
        """
        return self._airways

    @airways.setter
    def airways(self, airways: List[AirwayJunctionDetailOutput]):
        """Sets the airways of this AirwayJunctionOutput.


        :param airways: The airways of this AirwayJunctionOutput.
        :type airways: List[AirwayJunctionDetailOutput]
        """
        if airways is None:
            raise ValueError("Invalid value for `airways`, must not be `None`")  # noqa: E501

        self._airways = airways

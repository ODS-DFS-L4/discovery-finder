from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from discovery_finder.models.base_model import Model
from discovery_finder.models.b_box_definition import BBoxDefinition
from discovery_finder import util

from discovery_finder.models.b_box_definition import BBoxDefinition  # noqa: E501

class AreaOfInterest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, outline_polygon=None):  # noqa: E501
        """AreaOfInterest - a model defined in OpenAPI

        :param outline_polygon: The outline_polygon of this AreaOfInterest.  # noqa: E501
        :type outline_polygon: BBoxDefinition
        """
        self.openapi_types = {
            'outline_polygon': BBoxDefinition
        }

        self.attribute_map = {
            'outline_polygon': 'outline_polygon'
        }

        self._outline_polygon = outline_polygon

    @classmethod
    def from_dict(cls, dikt) -> 'AreaOfInterest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AreaOfInterest of this AreaOfInterest.  # noqa: E501
        :rtype: AreaOfInterest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def outline_polygon(self) -> BBoxDefinition:
        """Gets the outline_polygon of this AreaOfInterest.


        :return: The outline_polygon of this AreaOfInterest.
        :rtype: BBoxDefinition
        """
        return self._outline_polygon

    @outline_polygon.setter
    def outline_polygon(self, outline_polygon: BBoxDefinition):
        """Sets the outline_polygon of this AreaOfInterest.


        :param outline_polygon: The outline_polygon of this AreaOfInterest.
        :type outline_polygon: BBoxDefinition
        """
        if outline_polygon is None:
            raise ValueError("Invalid value for `outline_polygon`, must not be `None`")  # noqa: E501

        self._outline_polygon = outline_polygon

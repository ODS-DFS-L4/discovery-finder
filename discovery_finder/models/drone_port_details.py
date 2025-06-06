from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from discovery_finder.models.base_model import Model
from discovery_finder.models.drone_port_type import DronePortType
from discovery_finder.models.drone_port_usage_type import DronePortUsageType
from discovery_finder import util

from discovery_finder.models.drone_port_type import DronePortType  # noqa: E501
from discovery_finder.models.drone_port_usage_type import DronePortUsageType  # noqa: E501

class DronePortDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, manufacturer=None, port_type=None, latitude=None, longitude=None, altitude=None, supports_drone_type=None, usage_type=None, url=None):  # noqa: E501
        """DronePortDetails - a model defined in OpenAPI

        :param manufacturer: The manufacturer of this DronePortDetails.  # noqa: E501
        :type manufacturer: str
        :param port_type: The port_type of this DronePortDetails.  # noqa: E501
        :type port_type: DronePortType
        :param latitude: The latitude of this DronePortDetails.  # noqa: E501
        :type latitude: float
        :param longitude: The longitude of this DronePortDetails.  # noqa: E501
        :type longitude: float
        :param altitude: The altitude of this DronePortDetails.  # noqa: E501
        :type altitude: float
        :param supports_drone_type: The supports_drone_type of this DronePortDetails.  # noqa: E501
        :type supports_drone_type: str
        :param usage_type: The usage_type of this DronePortDetails.  # noqa: E501
        :type usage_type: DronePortUsageType
        :param url: The url of this DronePortDetails.  # noqa: E501
        :type url: str
        """
        self.openapi_types = {
            'manufacturer': str,
            'port_type': DronePortType,
            'latitude': float,
            'longitude': float,
            'altitude': float,
            'supports_drone_type': str,
            'usage_type': DronePortUsageType,
            'url': str
        }

        self.attribute_map = {
            'manufacturer': 'manufacturer',
            'port_type': 'port_type',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'altitude': 'altitude',
            'supports_drone_type': 'supports_drone_type',
            'usage_type': 'usage_type',
            'url': 'url'
        }

        self._manufacturer = manufacturer
        self._port_type = port_type
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude
        self._supports_drone_type = supports_drone_type
        self._usage_type = usage_type
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'DronePortDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DronePortDetails of this DronePortDetails.  # noqa: E501
        :rtype: DronePortDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def manufacturer(self) -> str:
        """Gets the manufacturer of this DronePortDetails.


        :return: The manufacturer of this DronePortDetails.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        """Sets the manufacturer of this DronePortDetails.


        :param manufacturer: The manufacturer of this DronePortDetails.
        :type manufacturer: str
        """
        if manufacturer is not None and len(manufacturer) > 24:
            raise ValueError("Invalid value for `manufacturer`, length must be less than or equal to `24`")  # noqa: E501
        if manufacturer is not None and len(manufacturer) < 1:
            raise ValueError("Invalid value for `manufacturer`, length must be greater than or equal to `1`")  # noqa: E501

        self._manufacturer = manufacturer

    @property
    def port_type(self) -> DronePortType:
        """Gets the port_type of this DronePortDetails.


        :return: The port_type of this DronePortDetails.
        :rtype: DronePortType
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type: DronePortType):
        """Sets the port_type of this DronePortDetails.


        :param port_type: The port_type of this DronePortDetails.
        :type port_type: DronePortType
        """
        if port_type is None:
            raise ValueError("Invalid value for `port_type`, must not be `None`")  # noqa: E501

        self._port_type = port_type

    @property
    def latitude(self) -> float:
        """Gets the latitude of this DronePortDetails.

        ドローンポート中心緯度  # noqa: E501

        :return: The latitude of this DronePortDetails.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this DronePortDetails.

        ドローンポート中心緯度  # noqa: E501

        :param latitude: The latitude of this DronePortDetails.
        :type latitude: float
        """
        if latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501
        if latitude is not None and latitude > 90:  # noqa: E501
            raise ValueError("Invalid value for `latitude`, must be a value less than or equal to `90`")  # noqa: E501
        if latitude is not None and latitude < -90:  # noqa: E501
            raise ValueError("Invalid value for `latitude`, must be a value greater than or equal to `-90`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Gets the longitude of this DronePortDetails.

        ドローンポート中心経度  # noqa: E501

        :return: The longitude of this DronePortDetails.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this DronePortDetails.

        ドローンポート中心経度  # noqa: E501

        :param longitude: The longitude of this DronePortDetails.
        :type longitude: float
        """
        if longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501
        if longitude is not None and longitude > 180:  # noqa: E501
            raise ValueError("Invalid value for `longitude`, must be a value less than or equal to `180`")  # noqa: E501
        if longitude is not None and longitude < -180:  # noqa: E501
            raise ValueError("Invalid value for `longitude`, must be a value greater than or equal to `-180`")  # noqa: E501

        self._longitude = longitude

    @property
    def altitude(self) -> float:
        """Gets the altitude of this DronePortDetails.

        ドローンポート着陸面の高さ(対地高度)  # noqa: E501

        :return: The altitude of this DronePortDetails.
        :rtype: float
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude: float):
        """Sets the altitude of this DronePortDetails.

        ドローンポート着陸面の高さ(対地高度)  # noqa: E501

        :param altitude: The altitude of this DronePortDetails.
        :type altitude: float
        """
        if altitude is None:
            raise ValueError("Invalid value for `altitude`, must not be `None`")  # noqa: E501
        if altitude is not None and altitude > 100:  # noqa: E501
            raise ValueError("Invalid value for `altitude`, must be a value less than or equal to `100`")  # noqa: E501
        if altitude is not None and altitude < 0:  # noqa: E501
            raise ValueError("Invalid value for `altitude`, must be a value greater than or equal to `0`")  # noqa: E501

        self._altitude = altitude

    @property
    def supports_drone_type(self) -> str:
        """Gets the supports_drone_type of this DronePortDetails.

        対応機体。着陸可能な機体の種類等を設定  # noqa: E501

        :return: The supports_drone_type of this DronePortDetails.
        :rtype: str
        """
        return self._supports_drone_type

    @supports_drone_type.setter
    def supports_drone_type(self, supports_drone_type: str):
        """Sets the supports_drone_type of this DronePortDetails.

        対応機体。着陸可能な機体の種類等を設定  # noqa: E501

        :param supports_drone_type: The supports_drone_type of this DronePortDetails.
        :type supports_drone_type: str
        """
        if supports_drone_type is None:
            raise ValueError("Invalid value for `supports_drone_type`, must not be `None`")  # noqa: E501
        if supports_drone_type is not None and len(supports_drone_type) > 24:
            raise ValueError("Invalid value for `supports_drone_type`, length must be less than or equal to `24`")  # noqa: E501

        self._supports_drone_type = supports_drone_type

    @property
    def usage_type(self) -> DronePortUsageType:
        """Gets the usage_type of this DronePortDetails.


        :return: The usage_type of this DronePortDetails.
        :rtype: DronePortUsageType
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type: DronePortUsageType):
        """Sets the usage_type of this DronePortDetails.


        :param usage_type: The usage_type of this DronePortDetails.
        :type usage_type: DronePortUsageType
        """
        if usage_type is None:
            raise ValueError("Invalid value for `usage_type`, must not be `None`")  # noqa: E501

        self._usage_type = usage_type

    @property
    def url(self) -> str:
        """Gets the url of this DronePortDetails.

        ドローンポートのURL  # noqa: E501

        :return: The url of this DronePortDetails.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this DronePortDetails.

        ドローンポートのURL  # noqa: E501

        :param url: The url of this DronePortDetails.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb2.domain.notification_endpoint_base import NotificationEndpointBase


class SlackNotificationEndpoint(NotificationEndpointBase):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'token': 'str',
        'id': 'str',
        'org_id': 'str',
        'user_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'description': 'str',
        'name': 'str',
        'status': 'str',
        'labels': 'list[Label]',
        'type': 'NotificationEndpointType'
    }

    attribute_map = {
        'url': 'url',
        'token': 'token',
        'id': 'id',
        'org_id': 'orgID',
        'user_id': 'userID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'description': 'description',
        'name': 'name',
        'status': 'status',
        'labels': 'labels',
        'type': 'type'
    }

    def __init__(self, url=None, token=None, id=None, org_id=None, user_id=None, created_at=None, updated_at=None, description=None, name=None, status='active', labels=None, type=None):  # noqa: E501
        """SlackNotificationEndpoint - a model defined in OpenAPI"""  # noqa: E501
        NotificationEndpointBase.__init__(self, id=id, org_id=org_id, user_id=user_id, created_at=created_at, updated_at=updated_at, description=description, name=name, status=status, labels=labels, type=type)

        self._url = None
        self._token = None
        self.discriminator = None

        self.url = url
        self.token = token

    @property
    def url(self):
        """Gets the url of this SlackNotificationEndpoint.  # noqa: E501


        :return: The url of this SlackNotificationEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SlackNotificationEndpoint.


        :param url: The url of this SlackNotificationEndpoint.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def token(self):
        """Gets the token of this SlackNotificationEndpoint.  # noqa: E501


        :return: The token of this SlackNotificationEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SlackNotificationEndpoint.


        :param token: The token of this SlackNotificationEndpoint.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SlackNotificationEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
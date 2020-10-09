# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    OpenAPI spec version: 2.3.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Amount(BaseModel):
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
    openapi_types = {"currency": "CurrencyCode", "value": "float"}

    attribute_map = {"currency": "currency", "value": "value"}

    def __init__(self, currency=None, value=None):  # noqa: E501
        """Amount - a model defined in OpenAPI"""  # noqa: E501

        self._currency = None
        self._value = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if value is not None:
            self.value = value

    @property
    def currency(self):
        """Gets the currency of this Amount.  # noqa: E501


        :return: The currency of this Amount.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Amount.


        :param currency: The currency of this Amount.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency = currency

    @property
    def value(self):
        """Gets the value of this Amount.  # noqa: E501


        :return: The value of this Amount.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Amount.


        :param value: The value of this Amount.  # noqa: E501
        :type: float
        """

        self._value = value

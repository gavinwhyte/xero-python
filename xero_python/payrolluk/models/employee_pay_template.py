# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.3.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeePayTemplate(BaseModel):
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
        "employee_id": "str",
        "earning_templates": "list[EarningsTemplate]",
    }

    attribute_map = {
        "employee_id": "employeeID",
        "earning_templates": "earningTemplates",
    }

    def __init__(self, employee_id=None, earning_templates=None):  # noqa: E501
        """EmployeePayTemplate - a model defined in OpenAPI"""  # noqa: E501

        self._employee_id = None
        self._earning_templates = None
        self.discriminator = None

        if employee_id is not None:
            self.employee_id = employee_id
        if earning_templates is not None:
            self.earning_templates = earning_templates

    @property
    def employee_id(self):
        """Gets the employee_id of this EmployeePayTemplate.  # noqa: E501

        Unique identifier for the employee  # noqa: E501

        :return: The employee_id of this EmployeePayTemplate.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this EmployeePayTemplate.

        Unique identifier for the employee  # noqa: E501

        :param employee_id: The employee_id of this EmployeePayTemplate.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def earning_templates(self):
        """Gets the earning_templates of this EmployeePayTemplate.  # noqa: E501


        :return: The earning_templates of this EmployeePayTemplate.  # noqa: E501
        :rtype: list[EarningsTemplate]
        """
        return self._earning_templates

    @earning_templates.setter
    def earning_templates(self, earning_templates):
        """Sets the earning_templates of this EmployeePayTemplate.


        :param earning_templates: The earning_templates of this EmployeePayTemplate.  # noqa: E501
        :type: list[EarningsTemplate]
        """

        self._earning_templates = earning_templates

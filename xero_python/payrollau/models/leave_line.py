# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.3.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LeaveLine(BaseModel):
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
        "leave_type_id": "str",
        "calculation_type": "LeaveLineCalculationType",
        "entitlement_final_pay_payout_type": "EntitlementFinalPayPayoutType",
        "employment_termination_payment_type": "EmploymentTerminationPaymentType",
        "include_superannuation_guarantee_contribution": "bool",
        "number_of_units": "float",
        "annual_number_of_units": "float",
        "full_time_number_of_units_per_period": "float",
    }

    attribute_map = {
        "leave_type_id": "LeaveTypeID",
        "calculation_type": "CalculationType",
        "entitlement_final_pay_payout_type": "EntitlementFinalPayPayoutType",
        "employment_termination_payment_type": "EmploymentTerminationPaymentType",
        "include_superannuation_guarantee_contribution": "IncludeSuperannuationGuaranteeContribution",
        "number_of_units": "NumberOfUnits",
        "annual_number_of_units": "AnnualNumberOfUnits",
        "full_time_number_of_units_per_period": "FullTimeNumberOfUnitsPerPeriod",
    }

    def __init__(
        self,
        leave_type_id=None,
        calculation_type=None,
        entitlement_final_pay_payout_type=None,
        employment_termination_payment_type=None,
        include_superannuation_guarantee_contribution=None,
        number_of_units=None,
        annual_number_of_units=None,
        full_time_number_of_units_per_period=None,
    ):  # noqa: E501
        """LeaveLine - a model defined in OpenAPI"""  # noqa: E501

        self._leave_type_id = None
        self._calculation_type = None
        self._entitlement_final_pay_payout_type = None
        self._employment_termination_payment_type = None
        self._include_superannuation_guarantee_contribution = None
        self._number_of_units = None
        self._annual_number_of_units = None
        self._full_time_number_of_units_per_period = None
        self.discriminator = None

        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if entitlement_final_pay_payout_type is not None:
            self.entitlement_final_pay_payout_type = entitlement_final_pay_payout_type
        if employment_termination_payment_type is not None:
            self.employment_termination_payment_type = (
                employment_termination_payment_type
            )
        if include_superannuation_guarantee_contribution is not None:
            self.include_superannuation_guarantee_contribution = (
                include_superannuation_guarantee_contribution
            )
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if annual_number_of_units is not None:
            self.annual_number_of_units = annual_number_of_units
        if full_time_number_of_units_per_period is not None:
            self.full_time_number_of_units_per_period = (
                full_time_number_of_units_per_period
            )

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this LeaveLine.  # noqa: E501

        Xero leave type identifier  # noqa: E501

        :return: The leave_type_id of this LeaveLine.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this LeaveLine.

        Xero leave type identifier  # noqa: E501

        :param leave_type_id: The leave_type_id of this LeaveLine.  # noqa: E501
        :type: str
        """

        self._leave_type_id = leave_type_id

    @property
    def calculation_type(self):
        """Gets the calculation_type of this LeaveLine.  # noqa: E501


        :return: The calculation_type of this LeaveLine.  # noqa: E501
        :rtype: LeaveLineCalculationType
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this LeaveLine.


        :param calculation_type: The calculation_type of this LeaveLine.  # noqa: E501
        :type: LeaveLineCalculationType
        """

        self._calculation_type = calculation_type

    @property
    def entitlement_final_pay_payout_type(self):
        """Gets the entitlement_final_pay_payout_type of this LeaveLine.  # noqa: E501


        :return: The entitlement_final_pay_payout_type of this LeaveLine.  # noqa: E501
        :rtype: EntitlementFinalPayPayoutType
        """
        return self._entitlement_final_pay_payout_type

    @entitlement_final_pay_payout_type.setter
    def entitlement_final_pay_payout_type(self, entitlement_final_pay_payout_type):
        """Sets the entitlement_final_pay_payout_type of this LeaveLine.


        :param entitlement_final_pay_payout_type: The entitlement_final_pay_payout_type of this LeaveLine.  # noqa: E501
        :type: EntitlementFinalPayPayoutType
        """

        self._entitlement_final_pay_payout_type = entitlement_final_pay_payout_type

    @property
    def employment_termination_payment_type(self):
        """Gets the employment_termination_payment_type of this LeaveLine.  # noqa: E501


        :return: The employment_termination_payment_type of this LeaveLine.  # noqa: E501
        :rtype: EmploymentTerminationPaymentType
        """
        return self._employment_termination_payment_type

    @employment_termination_payment_type.setter
    def employment_termination_payment_type(self, employment_termination_payment_type):
        """Sets the employment_termination_payment_type of this LeaveLine.


        :param employment_termination_payment_type: The employment_termination_payment_type of this LeaveLine.  # noqa: E501
        :type: EmploymentTerminationPaymentType
        """

        self._employment_termination_payment_type = employment_termination_payment_type

    @property
    def include_superannuation_guarantee_contribution(self):
        """Gets the include_superannuation_guarantee_contribution of this LeaveLine.  # noqa: E501

        amount of leave line  # noqa: E501

        :return: The include_superannuation_guarantee_contribution of this LeaveLine.  # noqa: E501
        :rtype: bool
        """
        return self._include_superannuation_guarantee_contribution

    @include_superannuation_guarantee_contribution.setter
    def include_superannuation_guarantee_contribution(
        self, include_superannuation_guarantee_contribution
    ):
        """Sets the include_superannuation_guarantee_contribution of this LeaveLine.

        amount of leave line  # noqa: E501

        :param include_superannuation_guarantee_contribution: The include_superannuation_guarantee_contribution of this LeaveLine.  # noqa: E501
        :type: bool
        """

        self._include_superannuation_guarantee_contribution = (
            include_superannuation_guarantee_contribution
        )

    @property
    def number_of_units(self):
        """Gets the number_of_units of this LeaveLine.  # noqa: E501

        Number of units for leave line.  # noqa: E501

        :return: The number_of_units of this LeaveLine.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this LeaveLine.

        Number of units for leave line.  # noqa: E501

        :param number_of_units: The number_of_units of this LeaveLine.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units

    @property
    def annual_number_of_units(self):
        """Gets the annual_number_of_units of this LeaveLine.  # noqa: E501

        Hours of leave accrued each year  # noqa: E501

        :return: The annual_number_of_units of this LeaveLine.  # noqa: E501
        :rtype: float
        """
        return self._annual_number_of_units

    @annual_number_of_units.setter
    def annual_number_of_units(self, annual_number_of_units):
        """Sets the annual_number_of_units of this LeaveLine.

        Hours of leave accrued each year  # noqa: E501

        :param annual_number_of_units: The annual_number_of_units of this LeaveLine.  # noqa: E501
        :type: float
        """

        self._annual_number_of_units = annual_number_of_units

    @property
    def full_time_number_of_units_per_period(self):
        """Gets the full_time_number_of_units_per_period of this LeaveLine.  # noqa: E501

        Normal ordinary earnings number of units for leave line.  # noqa: E501

        :return: The full_time_number_of_units_per_period of this LeaveLine.  # noqa: E501
        :rtype: float
        """
        return self._full_time_number_of_units_per_period

    @full_time_number_of_units_per_period.setter
    def full_time_number_of_units_per_period(
        self, full_time_number_of_units_per_period
    ):
        """Sets the full_time_number_of_units_per_period of this LeaveLine.

        Normal ordinary earnings number of units for leave line.  # noqa: E501

        :param full_time_number_of_units_per_period: The full_time_number_of_units_per_period of this LeaveLine.  # noqa: E501
        :type: float
        """

        self._full_time_number_of_units_per_period = (
            full_time_number_of_units_per_period
        )

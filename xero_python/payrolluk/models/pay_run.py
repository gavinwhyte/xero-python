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


class PayRun(BaseModel):
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
        "pay_run_id": "str",
        "payroll_calendar_id": "str",
        "period_start_date": "date",
        "period_end_date": "date",
        "payment_date": "date",
        "total_cost": "float",
        "total_pay": "float",
        "pay_run_status": "str",
        "pay_run_type": "str",
        "calendar_type": "str",
        "posted_date_time": "date",
        "pay_slips": "list[Payslip]",
    }

    attribute_map = {
        "pay_run_id": "payRunID",
        "payroll_calendar_id": "payrollCalendarID",
        "period_start_date": "periodStartDate",
        "period_end_date": "periodEndDate",
        "payment_date": "paymentDate",
        "total_cost": "totalCost",
        "total_pay": "totalPay",
        "pay_run_status": "payRunStatus",
        "pay_run_type": "payRunType",
        "calendar_type": "calendarType",
        "posted_date_time": "postedDateTime",
        "pay_slips": "paySlips",
    }

    def __init__(
        self,
        pay_run_id=None,
        payroll_calendar_id=None,
        period_start_date=None,
        period_end_date=None,
        payment_date=None,
        total_cost=None,
        total_pay=None,
        pay_run_status=None,
        pay_run_type=None,
        calendar_type=None,
        posted_date_time=None,
        pay_slips=None,
    ):  # noqa: E501
        """PayRun - a model defined in OpenAPI"""  # noqa: E501

        self._pay_run_id = None
        self._payroll_calendar_id = None
        self._period_start_date = None
        self._period_end_date = None
        self._payment_date = None
        self._total_cost = None
        self._total_pay = None
        self._pay_run_status = None
        self._pay_run_type = None
        self._calendar_type = None
        self._posted_date_time = None
        self._pay_slips = None
        self.discriminator = None

        if pay_run_id is not None:
            self.pay_run_id = pay_run_id
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if period_start_date is not None:
            self.period_start_date = period_start_date
        if period_end_date is not None:
            self.period_end_date = period_end_date
        if payment_date is not None:
            self.payment_date = payment_date
        if total_cost is not None:
            self.total_cost = total_cost
        if total_pay is not None:
            self.total_pay = total_pay
        if pay_run_status is not None:
            self.pay_run_status = pay_run_status
        if pay_run_type is not None:
            self.pay_run_type = pay_run_type
        if calendar_type is not None:
            self.calendar_type = calendar_type
        if posted_date_time is not None:
            self.posted_date_time = posted_date_time
        if pay_slips is not None:
            self.pay_slips = pay_slips

    @property
    def pay_run_id(self):
        """Gets the pay_run_id of this PayRun.  # noqa: E501

        Xero unique identifier for the pay run  # noqa: E501

        :return: The pay_run_id of this PayRun.  # noqa: E501
        :rtype: str
        """
        return self._pay_run_id

    @pay_run_id.setter
    def pay_run_id(self, pay_run_id):
        """Sets the pay_run_id of this PayRun.

        Xero unique identifier for the pay run  # noqa: E501

        :param pay_run_id: The pay_run_id of this PayRun.  # noqa: E501
        :type: str
        """

        self._pay_run_id = pay_run_id

    @property
    def payroll_calendar_id(self):
        """Gets the payroll_calendar_id of this PayRun.  # noqa: E501

        Xero unique identifier for the payroll calendar  # noqa: E501

        :return: The payroll_calendar_id of this PayRun.  # noqa: E501
        :rtype: str
        """
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        """Sets the payroll_calendar_id of this PayRun.

        Xero unique identifier for the payroll calendar  # noqa: E501

        :param payroll_calendar_id: The payroll_calendar_id of this PayRun.  # noqa: E501
        :type: str
        """

        self._payroll_calendar_id = payroll_calendar_id

    @property
    def period_start_date(self):
        """Gets the period_start_date of this PayRun.  # noqa: E501

        Period start date of the payroll calendar  # noqa: E501

        :return: The period_start_date of this PayRun.  # noqa: E501
        :rtype: date
        """
        return self._period_start_date

    @period_start_date.setter
    def period_start_date(self, period_start_date):
        """Sets the period_start_date of this PayRun.

        Period start date of the payroll calendar  # noqa: E501

        :param period_start_date: The period_start_date of this PayRun.  # noqa: E501
        :type: date
        """

        self._period_start_date = period_start_date

    @property
    def period_end_date(self):
        """Gets the period_end_date of this PayRun.  # noqa: E501

        Period end date of the payroll calendar  # noqa: E501

        :return: The period_end_date of this PayRun.  # noqa: E501
        :rtype: date
        """
        return self._period_end_date

    @period_end_date.setter
    def period_end_date(self, period_end_date):
        """Sets the period_end_date of this PayRun.

        Period end date of the payroll calendar  # noqa: E501

        :param period_end_date: The period_end_date of this PayRun.  # noqa: E501
        :type: date
        """

        self._period_end_date = period_end_date

    @property
    def payment_date(self):
        """Gets the payment_date of this PayRun.  # noqa: E501

        Payment date of the pay run  # noqa: E501

        :return: The payment_date of this PayRun.  # noqa: E501
        :rtype: date
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this PayRun.

        Payment date of the pay run  # noqa: E501

        :param payment_date: The payment_date of this PayRun.  # noqa: E501
        :type: date
        """

        self._payment_date = payment_date

    @property
    def total_cost(self):
        """Gets the total_cost of this PayRun.  # noqa: E501

        Total cost of the pay run  # noqa: E501

        :return: The total_cost of this PayRun.  # noqa: E501
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this PayRun.

        Total cost of the pay run  # noqa: E501

        :param total_cost: The total_cost of this PayRun.  # noqa: E501
        :type: float
        """

        self._total_cost = total_cost

    @property
    def total_pay(self):
        """Gets the total_pay of this PayRun.  # noqa: E501

        Total pay of the pay run  # noqa: E501

        :return: The total_pay of this PayRun.  # noqa: E501
        :rtype: float
        """
        return self._total_pay

    @total_pay.setter
    def total_pay(self, total_pay):
        """Sets the total_pay of this PayRun.

        Total pay of the pay run  # noqa: E501

        :param total_pay: The total_pay of this PayRun.  # noqa: E501
        :type: float
        """

        self._total_pay = total_pay

    @property
    def pay_run_status(self):
        """Gets the pay_run_status of this PayRun.  # noqa: E501

        Pay run status  # noqa: E501

        :return: The pay_run_status of this PayRun.  # noqa: E501
        :rtype: str
        """
        return self._pay_run_status

    @pay_run_status.setter
    def pay_run_status(self, pay_run_status):
        """Sets the pay_run_status of this PayRun.

        Pay run status  # noqa: E501

        :param pay_run_status: The pay_run_status of this PayRun.  # noqa: E501
        :type: str
        """
        allowed_values = ["Draft", "Posted", "None"]  # noqa: E501
        if pay_run_status not in allowed_values:
            raise ValueError(
                "Invalid value for `pay_run_status` ({0}), must be one of {1}".format(  # noqa: E501
                    pay_run_status, allowed_values
                )
            )

        self._pay_run_status = pay_run_status

    @property
    def pay_run_type(self):
        """Gets the pay_run_type of this PayRun.  # noqa: E501

        Pay run type  # noqa: E501

        :return: The pay_run_type of this PayRun.  # noqa: E501
        :rtype: str
        """
        return self._pay_run_type

    @pay_run_type.setter
    def pay_run_type(self, pay_run_type):
        """Sets the pay_run_type of this PayRun.

        Pay run type  # noqa: E501

        :param pay_run_type: The pay_run_type of this PayRun.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Scheduled",
            "Unscheduled",
            "EarlierYearUpdate",
            "None",
        ]  # noqa: E501
        if pay_run_type not in allowed_values:
            raise ValueError(
                "Invalid value for `pay_run_type` ({0}), must be one of {1}".format(  # noqa: E501
                    pay_run_type, allowed_values
                )
            )

        self._pay_run_type = pay_run_type

    @property
    def calendar_type(self):
        """Gets the calendar_type of this PayRun.  # noqa: E501

        Calendar type of the pay run  # noqa: E501

        :return: The calendar_type of this PayRun.  # noqa: E501
        :rtype: str
        """
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        """Sets the calendar_type of this PayRun.

        Calendar type of the pay run  # noqa: E501

        :param calendar_type: The calendar_type of this PayRun.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Weekly",
            "Fortnightly",
            "FourWeekly",
            "Monthly",
            "Annual",
            "Quarterly",
            "None",
        ]  # noqa: E501
        if calendar_type not in allowed_values:
            raise ValueError(
                "Invalid value for `calendar_type` ({0}), must be one of {1}".format(  # noqa: E501
                    calendar_type, allowed_values
                )
            )

        self._calendar_type = calendar_type

    @property
    def posted_date_time(self):
        """Gets the posted_date_time of this PayRun.  # noqa: E501

        Posted date time of the pay run  # noqa: E501

        :return: The posted_date_time of this PayRun.  # noqa: E501
        :rtype: date
        """
        return self._posted_date_time

    @posted_date_time.setter
    def posted_date_time(self, posted_date_time):
        """Sets the posted_date_time of this PayRun.

        Posted date time of the pay run  # noqa: E501

        :param posted_date_time: The posted_date_time of this PayRun.  # noqa: E501
        :type: date
        """

        self._posted_date_time = posted_date_time

    @property
    def pay_slips(self):
        """Gets the pay_slips of this PayRun.  # noqa: E501


        :return: The pay_slips of this PayRun.  # noqa: E501
        :rtype: list[Payslip]
        """
        return self._pay_slips

    @pay_slips.setter
    def pay_slips(self, pay_slips):
        """Sets the pay_slips of this PayRun.


        :param pay_slips: The pay_slips of this PayRun.  # noqa: E501
        :type: list[Payslip]
        """

        self._pay_slips = pay_slips

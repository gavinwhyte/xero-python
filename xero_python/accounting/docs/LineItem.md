# LineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_id** | **str** | LineItem unique ID | [optional] 
**description** | **str** | Description needs to be at least 1 char long. A line item with just a description (i.e no unit amount or quantity) can be created by specifying just a &lt;Description&gt; element that contains at least 1 character | [optional] 
**quantity** | **float** | LineItem Quantity | [optional] 
**unit_amount** | **float** | LineItem Unit Amount | [optional] 
**item_code** | **str** | See Items | [optional] 
**account_code** | **str** | See Accounts | [optional] 
**account_id** | **str** | The associated account ID related to this line item | [optional] 
**tax_type** | **str** | The tax type from TaxRates | [optional] 
**tax_amount** | **float** | The tax amount is auto calculated as a percentage of the line amount (see below) based on the tax rate. This value can be overriden if the calculated &lt;TaxAmount&gt; is not correct. | [optional] 
**line_amount** | **float** | If you wish to omit either of the &lt;Quantity&gt; or &lt;UnitAmount&gt; you can provide a LineAmount and Xero will calculate the missing amount for you. The line amount reflects the discounted price if a DiscountRate has been used . i.e LineAmount &#x3D; Quantity * Unit Amount * ((100 – DiscountRate)/100) | [optional] 
**tracking** | [**list[LineItemTracking]**](LineItemTracking.md) | Optional Tracking Category – see Tracking.  Any LineItem can have a  maximum of 2 &lt;TrackingCategory&gt; elements. | [optional] 
**discount_rate** | **float** | Percentage discount being applied to a line item (only supported on  ACCREC invoices – ACC PAY invoices and credit notes in Xero do not support discounts | [optional] 
**discount_amount** | **float** | Discount amount being applied to a line item. Only supported on ACCREC invoices - ACCPAY invoices and credit notes in Xero do not support discounts. | [optional] 
**repeating_invoice_id** | **str** | The Xero identifier for a Repeating Invoice | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



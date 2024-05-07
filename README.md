# **Vendor Management System**

This repository contains a Vendor Management System built using Django and Django REST Framework. The system allows for the management of vendor profiles, tracking of purchase orders, and calculation of vendor performance metrics.

# **Features**

Vendor Profile Management: Create, read, update, and delete vendor profiles.
Purchase Order Tracking: Create, read, update, and delete purchase orders.
Historical Performance Evaluation: Calculate historical on-time delivery rate, quality rating, response time, and fulfillment rate for each vendor.

# **Models**

The system uses the following models:

## **Vendor:** 
Represents a vendor with fields for name, contact details, address, vendor code, on-time delivery rate, quality rating average, average response time, and fulfillment rate.


## **PurchaseOrder:**
Represents a purchase order with fields for PO number, vendor, order date, delivery date, items, quantity, status, quality rating, issue date, and acknowledgment date.


## **HistoricalPerformance:** 
Represents historical performance data for a vendor with fields for on-time delivery rate, quality rating, response time, and fulfillment rate.

# **API Endpoints**
The system provides the following API endpoints:

POST */api/vendors/*: Create a new vendor.
GET */api/vendors/*: List all vendors.
GET */api/vendors/{vendor_id}/*: Retrieve a specific vendor's details.
PUT */api/vendors/{vendor_id}/*: Update a vendor's details.
DELETE */api/vendors/{vendor_id}/*: Delete a vendor.
POST */api/purchase_orders/*: Create a new purchase order.
GET */api/purchase_orders/*: List all purchase orders.
GET */api/purchase_orders/{po_id}/*: Retrieve a specific purchase order's details.
PUT */api/purchase_orders/{po_id}/*: Update a purchase order.
DELETE */api/purchase_orders/{po_id}/*: Delete a purchase order.
GET */api/vendors/{vendor_id}/performance/*: Retrieve a vendor's historical performance metrics.

# **Running the Test Suite**
To run the test suite, follow these steps:

### **Install the required packages** by running `pip install -r requirements.txt`
### **Run the tests using the following command:** `python manage.py test`
The test suite includes tests for the Vendor, PurchaseOrder, and HistoricalPerformance models, as well as tests for the API endpoints.


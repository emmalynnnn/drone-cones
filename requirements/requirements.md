# Requirements Document

## Problem Description

Drone Cones aims to provide a service that can allow a customer to order ice cream products at their specified location and have them delivered via drone delivery.  This will require systems to facilitate customer, drone-owner, and admin interactions.

## Solution Description

To achieve these goals, our software will provide the following:

1. An ordering system to allow customers to view menu items, add menu items into an order, pay for the order, and track the status of the order as it is being delivered.

2. An account system to store necessary data for customers, drone-owners, and admins to allow notifications to be sent to account holders.

3. Administrative tools to allow management of menu inventory, perform customer support operations, perform financial operations and generate reports, and see drone status and leasing reports.

4. Drone-owner tools to register and unregister drones for lease, see earnings, receive payments, and view pending orders.  

## Customer User Stories

* As a customer, I want to order ice cream at my current location so I can obtain ice cream via drone delivery.
  
* As a customer, I expect to be able to contact customer support in order to resolve issues with my order.
  
* As a customer, I want to be able to track my current order to know when it will arrive.
  
* As a customer, I want to register for a customer account in order to receive sales promotions and other benefits.
  
* As a customer, I want to login to my customer account in order to check information pertaining to me, such as order history or current rewards points.
  
* As a customer, I expect to receive notifications from Drone Cones in order to know when orders arrive or if any sales promotions are occurring.

## Customer Use Cases

![UML Diagram](customer_use_cases_UML.png)

## Admin User Stories

* The admin wants to track the drones so that they can give an accurate ETA to customers.
  
* The admin wants to see and set stock levels so they can ensure ice cream is always on hand.
  
* The admin wants to see stats on how many orders they get so that they can know if the business is gonna go out of business.
  
* The admin wants to know the number of drone-owners so they can know if they need to get more.
  
* The admin opens the website and signs in with their admin credentials. They see a dashboard of the current status of orders and inventory so that they can quickly respond to problems and shortages.

## Admin Use Cases

![UML Diagram](Manager_Use_Cases_UML.png)

## Drone-Owner User Stories

* As a drone-owner, I want to be able to register a drone/register new drones.
  
* As a drone-owner (who likes to use my drone), I want to be able to pull my drone out of the project without needing excessive notice so I can have my drone back.
  
* As a drone-owner I want to see stats on my drone’s deliveries and location.
  
* As a business-oriented drone-owner, I want to be able to clearly see how much money I would make before committing to the project so I can make an informed decision.

* As a drone owner I want to see how much money I’ve made.

## Drone-Owner Use Cases

![UML Diagram](Operator_Use_Cases_UML.png)

# The Supply Chain System

## Overview

This system is designed for a unique store that offers festive seasonal items all year round. From Easter eggs in December to Halloween candy in April, this store has it all. The system focuses on processing bulk orders received through the store's website. It utilizes the abstract factory design pattern to manage the varied inventory of toys, stuffed animals, and candy corresponding to different holidays like Easter, Christmas, and Halloween.

## Features

### Inventory
The store maintains a unique assortment of items for each festive season, categorized into Toys, Stuffed Animals, and Candy, each with specific attributes and varieties. 

For the Easter season, the store offers the following items:
- Robot Bunny (Toy)
- Creme Eggs (Candy)
- Easter Bunny (Stuffed Animal)

For the Christmas season, the store offers the following items:
- Santa's Workshop (Toy)
- Candy Canes (Candy)
- Reindeer (Stuffed Animal)

For the Halloween season, the store offers the following items:
- RC Spider (Toy)
- Pumpkin Caramel Toffee (Candy)
- Dancing Skeleton (Stuffed Animal)

### Process Web Orders
The system processes orders from Excel files using the pandas package. An OrderProcessor class reads the file, creating Order objects with details like order number, product ID, quantity, item type, item name, etc.

### The Storefront
The Store class handles order reception, inventory management, and item creation through factory classes when stock is low. It also generates a Daily Transaction Report upon exiting the program.

### Daily Transaction Report
The Daily Transaction Report is a text file that specifies the list of orders processed that day.

## Usage

Upon running the program, the store owner is greeted with a terminal menu with the following options:

1. Process Web Orders: Process orders from an Excel file downloaded daily from the online storefront.
2. Check Inventory: View current stock with status indicators (In Stock, Low, Very Low, Out of Stock).
3. Exit: Exits the program and generates a daily transaction report.

## Limitations

The Excel file must be formatted in a specific way for the program to process it correctly. It should have the following columns:

| order_number | holiday   | item | name                                 | quantity | product_id | description                                               | has_batteries | min_age | dimensions | num_rooms | speed | jump_height | has_glow | spider_type | num_sound | colour | has_lactose | has_nuts | variety | pack_size | stuffing | size | fabric |
|--------------|-----------|------|--------------------------------------|----------|------------|-----------------------------------------------------------|---------------|---------|------------|-----------|-------|-------------|----------|-------------|-----------|--------|-------------|----------|---------|-----------|----------|------|--------|
| 1            | Christmas | Toy  | Santas Workshop - Essentials Edition | 10       | C1230T     | The most sought after christmas present! Get yours today! | N             | 5       | 50,90      | 4         |       |             |          |             |           |        |             |          |         |           |          |      |        |
| ...          | ...       | ...  | ...                                  | ...      | ...        | ...                                                       | ...           | ...     | ...        | ...       | ...   | ...         | ...      | ...         | ...       | ...    | ...         | ...      | ...     | ...       | ...      | ...  | ...    |

The column names must be exactly as shown above. The order of the columns does not matter. The program will not process the file if it is not formatted correctly.
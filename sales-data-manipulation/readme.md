# Data Manipulation with Pandas

## Overview

This project demonstrates how to manipulate a large sales dataset using pandas. The dataset contains product sales data, and the goal is to:

1. Group the data by region and calculate total sales for each region.
2. Create a new column, `average_price_per_unit`, which calculates the average price per unit sold for each `product_id`.
3. Filter the dataset to include only the rows where the total sales for that product exceed ₹10,000.

---

## Features

- **Group Data by Region**: Aggregates total sales for each region.
- **Calculate Average Price Per Unit**: Computes the average price per unit sold for each `product_id`.
- **Filter Data**: Filters products whose total sales exceed ₹10,000.

---

## Prerequisites

1. **Python**: Ensure Python 3.8 or higher is installed.
2. **Dependencies**: Install the required Python libraries using the following command:
   ```bash
   pip install pandas
   ```

### Sample CSV Data

Here is a sample of the dataset:

```
csv

product_id,date,price,quantity,region
101,2024-09-01,500,20,North
102,2024-09-01,600,15,South
103,2024-09-02,300,40,West
104,2024-09-02,800,5,North
105,2024-09-03,700,10,East
```

### Steps

1. Group the Data by Region:
   We will group the data by the region column and calculate the total sales (price \* quantity) for each region.
2. Create a New Column **_average_price_per_unit_**:
   This new column will store the average price per unit sold for each **_product_id_**.
3. Filter the Data:
   We will filter the dataset to include only rows where the total sales for the product exceed ₹10,000.

### Handling Large Datasets

When dealing with millions of rows, you can optimize performance by:

**_Using dtype argument:_** Specify data types for columns to reduce memory usage.

**_Processing in Chunks:_** Load the data in chunks to avoid memory overflow.

**_Avoiding Iteration:_** Avoid looping over DataFrame rows and use vectorized operations instead.

### Handling Missing or Duplicated Data

**_Handling Missing product_id:_**

Use dropna() to remove rows with missing product_id or other important columns.
Use fillna() to replace missing values with default values if needed.

### Handling Duplicated Rows:

Use drop_duplicates() to remove duplicate rows based on certain columns.

### Output

The output of this manipulation will be:

**_Grouped Data by Region:_** The total sales for each region will be available in the region_sales DataFrame.

**_New Column average_price_per_unit:_** A new column will be added to the original dataset with the calculated average price per unit sold.

**_Filtered Data:_** The filtered_data DataFrame will contain only rows where the total sales exceed ₹10,000.

### License

This project is licensed under the MIT License.

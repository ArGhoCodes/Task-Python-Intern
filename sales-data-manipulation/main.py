import pandas as pd

# File name
CSV_FILE = "sales-data-manipulation/sales_data.csv"

def manipulate_sales_data(csv_file):
    # Efficiently load the data in chunks for large datasets
    chunk_size = 100_000  # Process 100,000 rows at a time
    region_sales_aggregated = {}
    filtered_data = []
    product_sales = {}

    for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
        # Drop rows with missing or non-numeric critical values
        chunk.dropna(subset=['product_id', 'price', 'quantity'], inplace=True)
        chunk['price'] = pd.to_numeric(chunk['price'], errors='coerce')
        chunk['quantity'] = pd.to_numeric(chunk['quantity'], errors='coerce')
        chunk.dropna(subset=['price', 'quantity'], inplace=True)

        # Ensure `product_id` is consistent (remove duplicates within the chunk)
        chunk.drop_duplicates(subset=['product_id'], inplace=True)

        # Add total sales column
        chunk['total_sales'] = chunk['price'] * chunk['quantity']

        # Aggregate region-wise total sales for the chunk
        region_sales_chunk = chunk.groupby('region')['total_sales'].sum().to_dict()
        for region, sales in region_sales_chunk.items():
            region_sales_aggregated[region] = region_sales_aggregated.get(region, 0) + sales

        # Add average price per unit for each product
        product_sales_chunk = (
            chunk.groupby('product_id')
            .apply(lambda x: (x['price'] * x['quantity']).sum() / x['quantity'].sum())
            .reset_index(name='average_price_per_unit')
        )
        product_sales.update(product_sales_chunk.set_index('product_id')['average_price_per_unit'].to_dict())

        # Filter rows where total sales > ₹10,000
        filtered_data_chunk = chunk[chunk['total_sales'] > 10000]
        filtered_data.append(filtered_data_chunk)

    # Combine all filtered rows into a single DataFrame
    filtered_data = pd.concat(filtered_data, ignore_index=True)

    # Save outputs
    region_sales_df = pd.DataFrame(list(region_sales_aggregated.items()), columns=['region', 'total_sales'])
    region_sales_df.to_csv("region_sales.csv", index=False)

    filtered_data.to_csv("filtered_sales.csv", index=False)

    # Save product average prices
    product_avg_price_df = pd.DataFrame.from_dict(product_sales, orient='index', columns=['product_id','average_price_per_unit'])
    product_avg_price_df.to_csv("product_avg_price.csv")

    print("Region-wise total sales saved to 'region_sales.csv'.")
    print("Filtered data saved to 'filtered_sales.csv'.")
    print("Average price per product saved to 'product_avg_price.csv'.")

# Call the function
manipulate_sales_data(CSV_FILE)

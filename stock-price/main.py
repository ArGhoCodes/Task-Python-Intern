import asyncio
import websockets
import json
import csv
import os

# webSocket URL
SOCKET_URL = "wss://ws.coincap.io/prices?assets=bitcoin,ethereum,tether,binance-coin,solana,usd-coin"
CSV_FILE = "stock-price/stock_data.csv"

# batch size for write operations
BATCH_SIZE = 10

# limiting the number of rows to process
MAX_ROWS = 1000

# initialized a batch buffer and a counter for performance optimization
batch_buffer = []
row_count = 0


async def write_to_csv(batch):
    file_exists = os.path.exists(CSV_FILE)
    
    with open(CSV_FILE, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        if not file_exists:
            writer.writerow(["symbol", "price", "volume"])  
        
        # Writing the batch records
        writer.writerows(batch)


async def process_data():
    #connecting WebSocket and process incoming data."""
    global batch_buffer, row_count

    while row_count < MAX_ROWS:  # processing each row until MAX_ROWS is reached
        try:
            async with websockets.connect(SOCKET_URL) as websocket:
                print(f"Connected to {SOCKET_URL}...")
                
                while row_count < MAX_ROWS:
                    message = await websocket.recv()
                    data = json.loads(message)
                    
                    # processing received data
                    for symbol, price in data.items():
                        if row_count >= MAX_ROWS:
                            break
                        
                        # appending the data to the batch buffer
                        # there is no volume in the data provided
                        batch_buffer.append([symbol, price, None]) 
                        row_count += 1
                        
                        # writing to csv in batches
                        if len(batch_buffer) >= BATCH_SIZE:
                            await write_to_csv(batch_buffer)
                            batch_buffer.clear()
                    
        except (websockets.ConnectionClosed, asyncio.TimeoutError) as e:
            # handling the connection interruption error
            print(f"Connection interrupted: {e}. Reconnecting...")
            await asyncio.sleep(5) 
    
    # writing any remaining rows in the buffer
    if batch_buffer:
        await write_to_csv(batch_buffer)
        batch_buffer.clear()

    print(f"Processed {row_count} rows. Exiting...")


async def main():
    """running the WebSocket processing loop."""
    await process_data()


if __name__ == "__main__":
    asyncio.run(main())

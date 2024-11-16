## WebSocket Data Streaming and CSV Storage

### Overview

This project demonstrates how to stream live stock market data from a WebSocket endpoint and store the received data in a CSV file. The application handles connection interruptions, ensures data consistency, and optimizes performance for real-time data processing.

### Features:

Live WebSocket Data Streaming: Connects to a WebSocket endpoint to receive live stock market data.
CSV Storage: Saves incoming data to a CSV file in real time.
Reconnection Handling: Automatically reconnects to the WebSocket if the connection is interrupted.
Batch Inserts: Efficiently handles bursts of data by writing in batches to the CSV file.

### Prerequisites

Python: Ensure Python 3.8 or higher is installed.

## Dependencies

Install the required Python libraries using the command:

```
pip install websockets pandas
```

WebSocket Endpoint :

The WebSocket endpoint streams JSON-formatted data containing the following fields:

```
symbol: The stock symbol (e.g., 'AAPL').
price: The current price (e.g., 145.67).
volume: The number of shares traded (e.g., 1500).

```

Sample WebSocket Data :

```
{
"symbol": "AAPL",
"price": 145.67,
"volume": 1500
}
```

### CSV Format

The application stores data in the following CSV format:

```
symbol,price,volume
AAPL,145.67,1500
GOOGL,2725.67,2000
MSFT,289.12,3000
```

### Usage

Run the Script

Save the script in a file, e.g., websocket_to_csv.py.

Execute the script:

```
python websocket_to_csv.py
```

### Code Explanation

WebSocket Connection

The script uses the websockets library to establish a connection to the WebSocket endpoint. It listens for incoming data and processes it in real-time.

Handling Connection Interruptions
The script automatically attempts to reconnect to the WebSocket if the connection is interrupted, using a retry mechanism with a delay.

Batch Data Handling
Incoming data is temporarily stored in a batch buffer. Once the batch size reaches a predefined threshold, the data is written to the CSV file to minimize file I/O operations.

### Key Code Snippet

```
async def process_data():
"""Main function to connect to WebSocket and process incoming data."""
batch_buffer = []
BATCH_SIZE = 10 # Number of records to batch before writing to CSV

    while True:
        try:
            async with websockets.connect(SOCKET_URL) as websocket:
                print(f"Connected to {SOCKET_URL}...")
                while True:
                    message = await websocket.recv()
                    data = json.loads(message)

                    # Process incoming data
                    for symbol, price in data.items():
                        batch_buffer.append([symbol, price, None])  # Volume is None here
                        if len(batch_buffer) >= BATCH_SIZE:
                            await write_to_csv(batch_buffer)
                            batch_buffer.clear()
        except (websockets.ConnectionClosed, asyncio.TimeoutError):
            print("Connection interrupted. Reconnecting...")
            await asyncio.sleep(5)  # Wait before reconnecting
```

### Tricky Aspects Addressed

1. Reconnection Handling
   Automatic retries ensure uninterrupted data collection.
   A delay between reconnections prevents overwhelming the server.
2. Batch Inserts for Performance
   Data is stored in a buffer and written in batches to reduce disk I/O operations.
   This optimizes performance, especially for high-frequency data streams.

### Output Files:

The collected data is stored in a file named stock_data.csv. If the script is run multiple times, new data will be appended to the same file.

### Customization

Batch Size

Modify the batch size for optimization:

BATCH_SIZE = 20

```
#WebSocket URL

Update the SOCKET_URL variable with your WebSocket endpoint:
SOCKET_URL = "wss://your-websocket-url"

```

### License

This project is licensed under the MIT License.

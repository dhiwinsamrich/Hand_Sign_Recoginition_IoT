from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define an API endpoint to handle POST requests
@app.route('/process-data', methods=['POST'])
def process_data():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Print the received data to the console
        print("Received data:")
        print(data)

        # Return a response to confirm receipt of data
        return jsonify({"message": "Data received successfully!", "received_data": data}), 200
    except Exception as e:
        # Handle any errors and print them
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 400

# Run the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

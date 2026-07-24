import http.server
import socketserver
import urllib.parse
import json

PORT = 8000

class ServerlessFunctionHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL to get the path and query parameters
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query_params = urllib.parse.parse_qs(parsed_url.query)

        # Simulate a serverless function triggered by an HTTP GET request
        if path == '/hello':
            # This is our "serverless function" logic.
            # It takes a 'name' parameter and returns a greeting.
            # This function is stateless and only performs its task when invoked,
            # mimicking a Function-as-a-Service (FaaS) execution.
            name = query_params.get('name', ['World'])[0] # Default to 'World' if no name
            response_message = f"Hello, {name}! This is a simulated serverless function response."
            status_code = 200

            self.send_response(status_code)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": response_message}).encode("utf-8"))

        elif path == '/info':
            # Another simulated function, perhaps returning system info.
            # Each function is a distinct, deployable unit.
            response_message = {
                "function_name": "info_service",
                "version": "1.0",
                "runtime": "Python Standard Library",
                "status": "active"
            }
            status_code = 200

            self.send_response(status_code)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_message).encode("utf-8"))

        else:
            # Handle unknown paths
            response_message = "404 Not Found. Try /hello?name=YourName or /info"
            status_code = 404

            self.send_response(status_code)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": response_message}).encode("utf-8"))

    def do_POST(self):
        # Simulate a serverless function triggered by an HTTP POST request.
        # Serverless functions can respond to various event types, including POST requests.
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        if path == '/process_data':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                # Simulate processing the data received in the request body.
                # This demonstrates handling input for a specific serverless task.
                processed_result = f"Data received: {data.get('input', 'No input')}. Processed successfully!"
                response_message = {"status": "success", "result": processed_result}
                status_code = 200
            except json.JSONDecodeError:
                response_message = {"status": "error", "message": "Invalid JSON"}
                status_code = 400

            self.send_response(status_code)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_message).encode("utf-8"))
        else:
            response_message = "404 Not Found. Try POST to /process_data with JSON body."
            status_code = 404
            self.send_response(status_code)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": response_message}).encode("utf-8"))


# Set up the server to listen for requests, acting as the "serverless platform"
# that invokes our functions based on incoming HTTP events.
with socketserver.TCPServer(('', PORT), ServerlessFunctionHandler) as httpd:
    print(f"Serving simulated serverless functions at http://localhost:{PORT}")
    print("Test with: curl http://localhost:8000/hello?name=DevToUser")
    print("Test with: curl -X POST -H \"Content-Type: application/json\" -d '{\"input\": \"sample data\"}' http://localhost:8000/process_data")
    httpd.serve_forever()

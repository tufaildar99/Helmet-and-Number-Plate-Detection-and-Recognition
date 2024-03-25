import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
from bucket import Bucket
import json

from db import Database
db = Database()
bucket = Bucket()
# Define the handler to use for incoming requests

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL and the query parameters
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if parsed_path.path == '/get_violations':
            # Read number plate from query 
            number_plate = query_params['no'][0]
            print(number_plate)

            # Get violations from db
            violations = db.getViolations(number_plate)
            if len(violations) == 0:
                self.send_response(404)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "GET")
                self.end_headers()
                violations = "No violations found"
                self.wfile.write(bytes(str(violations), "utf-8"))
            else:
            # Serve as json response
                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "GET")
                self.send_header("Content-type", "application/json")
                self.end_headers()
                
                result = []
                for violation in violations:
                    result.append({
                        "no": violation[0],
                        "timestamp": str(violation[1]),
                        "proof": bucket.get_public_url(violation[2])
                    })

                # Convert the result to JSON and send it
                self.wfile.write(bytes(json.dumps(result), "utf-8"))
# Set the handler for the server
handler = MyHandler

# Set the port number for the server
port = 8080

# Create the server and bind it to the specified port
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving on port {port}")

# Run the server indefinitely
httpd.serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Adding a debug print to make sure the method is being called
        print("Handling GET request") 
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"message": "This is a GET response"}
        self.wfile.write(json.dumps(response).encode("utf-8"))


    def do_POST(self):
        print("Handling POST request") 
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        message = json.loads(post_data)
        
        print(f"Received message: {message}")

        # Responding back with a message
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"response": f"Hello, {message['name']}!"}
        self.wfile.write(json.dumps(response).encode("utf-8"))

def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server running on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()

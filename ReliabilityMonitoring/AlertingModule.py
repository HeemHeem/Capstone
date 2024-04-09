from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading

# Timer duration in seconds
TIMER_DURATION = 60

# Initialize the last successful communication time
last_successful_communication_time = time.time()

# Flag to stop the server
stop_server = False


# HTTP Request Handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global last_successful_communication_time
        # determine the length of the content in post
        content_length = int(self.headers['Content-Length'])
        # using content length decode the content of the post method
        post_data = self.rfile.read(content_length).decode('utf-8')
        # if the post data equals connected
        if post_data.strip() == "connected":
            print(f"{time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(time.time()))} - Device is connected")
            # Last communication time becomes current time
            last_successful_communication_time = time.time()


# Create HTTP Server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    global stop_server
    # empty string indicates that server will accept connections
    server_address = ('', port)
    # Create a http server with address and handler class
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    while not stop_server:
        httpd.handle_request()
    httpd.shutdown()


# Check Timer
def check_timer():
    global last_successful_communication_time
    current_time = time.time()
    # if the current time minus the last time the device communicated is greater than or equal to the time limit
    if (current_time - last_successful_communication_time) >= TIMER_DURATION:
        last_active = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(last_successful_communication_time))
        print("Device is offline. Last active: ", last_active)
        # Push notifications, email, SMS would happen here
    else:
        print(f"Next check in {TIMER_DURATION} seconds...")


if __name__ == "__main__":
    # Create a new thread for the server so that the server can run independently while the program checks the timer
    server_thread = threading.Thread(target=run)
    try:
        # Execute the server thread
        server_thread.start()
        # Continuous loop that checks the timer and then waits
        while True:
            check_timer()
            time.sleep(TIMER_DURATION)
    # if a keyboard interrupt occurs then the server thread ends gracefully
    except KeyboardInterrupt:
        print("Stopping server...")
        stop_server = True
        server_thread.join()

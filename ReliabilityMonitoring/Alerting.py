from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading
import datetime

# Timer duration in seconds
TIMER_DURATION = 60

# Initialize the last successful communication time
last_successful_communication_time = datetime.datetime.now()


# HTTP Request Handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global last_successful_communication_time
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        if post_data.strip() == "connected":
            print("Device is connected.")
            last_successful_communication_time = datetime.time()


# Create HTTP Server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


# Check Timer
def check_timer():
    global last_successful_communication_time
    current_time = time.time()
    if (current_time - last_successful_communication_time.timestamp()) >= TIMER_DURATION:
        print("Device is offline. Last active: ", last_successful_communication_time.strftime('%Y/%m/%d %H:%M:%S'))
        # Push notifications, email, SMS would happen here
    else:
        print(f"Timer reset. Next check in {TIMER_DURATION} seconds...")


if __name__ == "__main__":
    server_thread = threading.Thread(target=run)
    try:
        server_thread.start()
        while True:
            check_timer()
            time.sleep(TIMER_DURATION)
    except KeyboardInterrupt:
        print("Stopping server...")
        server_thread.join()

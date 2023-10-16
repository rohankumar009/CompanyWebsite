from http.server import BaseHTTPRequestHandler, HTTPServer

def server(url):
    """
    url is a *PARTIAL* URL. If the browser requests `http://localhost:4131/contact?name=joe`
    then the `url` parameter will have the value "/contact?name=joe". (so the schema and 
    authority will not be included, but the full path, any query, and any anchor will be included)

    This function is called each time another program/computer makes a request to this website.
    The URL represents the requested file.

    This function should return a string.
    """

    ######
    # TODO: Hey student! This is the function you need to change! Don't miss it!
    ######

    # Remove all the query/parameters/anchors from the URL: GOT THIS FROM LEC so I hope its right?
    url = url.split('?')[0].split('#')[0]

    url_to_file = { "/": "mainpage.html", "/main": "mainpage.html", "/contact": "contactform.html", "/testimonies": "testimonies.html" }

    
    if url in url_to_file:
        file_name = url_to_file[url]
        try:
            with open(file_name, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "404 Not Found: The requested file does not exist."
    else:
        return "404 Not Found: The requested page does not exist."
    

# You shouldn't need to change content below this. It would be best if you just left it alone.

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Call the student-edited server code.
        message = server(self.path)
        
        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # prepare the response object with minimal viable headers.
        self.protocol_version = "HTTP/1.1"
        # Send response code
        self.send_response(200)
        # Send headers
        # Note -- this would be binary length, not string length
        self.send_header("Content-Length", len(message))
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)
        return

def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ('', PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()
run()
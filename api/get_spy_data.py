from http.server import BaseHTTPRequestHandler
from main import Options
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            spy = Options('SPY')
            data = spy.get_options_data()
            json_data = data.to_json(orient='split')
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(e).encode())

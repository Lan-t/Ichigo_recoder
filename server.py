from http.server import HTTPServer, SimpleHTTPRequestHandler
import time

class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        body = open('resoureces/log.log').read()
        self.send_response(200)
        self.send_header('Content-type', 'text; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body.encode("UTF-8"))

    def do_POST(self):
        if self.path == '/reset':open('resoureces/log.log','w').write('')
        
        body = ''
        try:
            content_len = int(self.headers.get('content-length'))
            req = self.rfile.read(content_len)
            res = 200
            req_str = req.decode('UTF-8')
            body = '\'Posted'

        except TypeError:
            body += '\'No Data'
            res = 400

        try:
            track = [float(i) for i in req_str.split(' ')]
            log(track)
        except ValueError:
            body = '\'Data format: キオン[SP]シツド'
            res = 400

        self.send_response(res)
        body = body.encode("UTF-8")
        self.send_header('Content-type', 'text; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

def log(track):
    t = time.localtime()
    text = '%d/%d/%d %d:%d:%d %.5f %.5f\n'%(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, (track[0]/2**16)*165-40, (track[1]/2**16)*100
    open('resoureces/log.log', 'a').write(text)
    open('resoureces/backup', 'a').write(text)

port = 80
host = ''
httpd = HTTPServer((host, port), MyHandler)
print('serving at port', port)
httpd.serve_forever()



# -*- coding:utf-8 -*-
from os import path
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from webService.src.flask_main import app

curdir = path.dirname(path.realpath(__file__))
sep = '/'

# MIME-TYPE
mimedic = [
                        ('.html', 'text/html'),
                        ('.htm', 'text/html'),
                        ('.js', 'application/javascript'),
                        ('.css', 'text/css'),
                        ('.json', 'application/json'),
                        ('.png', 'image/png'),
                        ('.jpg', 'image/jpeg'),
                        ('.gif', 'image/gif'),
                        ('.txt', 'text/plain'),
                        ('.avi', 'video/x-msvideo'),
        ]


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        sendReply = False
        querypath = urlparse(self.path)
        filepath, query = querypath.path, querypath.query

        if filepath.endswith('/'):
            filepath += 'htmls/index.html'
        elif filepath.startswith('/items'):
            filepath = 'htmls' + filepath

        filename, fileext = path.splitext(filepath)
        for e in mimedic:
            if e[0] == fileext:
                mimetype = e[1]
                sendReply = True

        if sendReply:
            try:
                with open(path.realpath(curdir + sep + filepath), 'rb') as f:
                    content = f.read()
                    self.send_response(200)
                    self.send_header('Content-type', mimetype)
                    self.end_headers()
                    self.wfile.write(content)
            except IOError:
                self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        pass


def main():
    server = ('', 8999)
    httpd = HTTPServer(server, MyHandler)
    httpd.serve_forever()
    app.run(host='0.0.0.0', port='9090')
    pass


if __name__ == '__main__':
    main()

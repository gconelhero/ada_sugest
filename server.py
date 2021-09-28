from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

t_list = []

class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('t_list'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += "<h1>Titles List's</h1>"
            output += '<h3><a href="/t_list/new">Add New Titles List</a></h3>'
            for t in t_list:
                output += f"{t}"
                output += '</br>'
            output += '</body></html>'
            self.wfile.write(output.encode())

        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')

            output = ''
            output += '<html><body>'
            output += '<h1>Add New List</h1>'

            output += '<form method="POST" enctype="multipart/form-data" action"/t_list/new">'
            output += '<input name="titles" type="text" placeholder="Add New Titles">'
            output += '<input type="submit" value="Add">'
            output += '</form>'
            output += '</body></html>'

            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/new'):
            content_type, parameter_dict = cgi.parse_header(
                self.headers.get('content-type')
            )
            parameter_dict['boundary'] = bytes(
                parameter_dict['boundary'], "utf-8"
            )
            content_length = int(self.headers.get('Content-length'))
            parameter_dict['CONTENT-LENGTH'] = content_length
            if content_type == 'multipart/form-data':
                fields = cgi.parse_multipart(
                    self.rfile, parameter_dict
                )
                new_task = fields.get('titles')
                print("TESTE", new_task)
                t_list.extend(list(new_task))
                print(t_list)

        self.send_response(301)
        self.send_header('content-type', 'text/html')
        #self.send_header('Location', '/t_list')
        self.end_headers()


def main():
    port = 80
    server_address = ('0.0.0.0', port)
    server = HTTPServer(server_address, Request)
    print('Server running...')
    server.serve_forever()

if __name__ == '__main__':
    main()


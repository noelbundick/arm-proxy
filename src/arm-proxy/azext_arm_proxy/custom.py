from knack.util import CLIError


def start_arm_proxy(cmd, port=8000):
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    from pyngrok import ngrok

    with HTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler) as httpd:
        public_url = ngrok.connect(port, "http")
        print("proxy connected at {}, press Ctrl+C to exit".format(public_url))
        httpd.serve_forever()

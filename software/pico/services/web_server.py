import constants
from phew import access_point, dns, logging, server
from phew.template import render_template
from phew.server import redirect

DOMAIN = "pico.wireless"


@server.route("/", methods=['GET'])
def index(request):
    if request.method == 'GET':
        logging.debug("Get request")
        # return server.redirect("/test.html")
        return render_template("index.html")


@server.route("/upload-route-sheet", methods=["POST"])
def upload_route_sheet(request):
    print(request)
    return "", 200


@server.catchall()
def catch_all(request):
    print("***************CATCHALL***********************\n" + str(request))
    return redirect("http://" + DOMAIN + "/")


class WebServer(object):
    def __init__(self):
        self.ap = None
        self.ip = None
        self.dns = None

    def start(self):
        logging.info(f"SSID {constants.SSID}")

        self.ap = access_point(constants.SSID)
        self.ip = self.ap.ifconfig()[0]
        logging.info(f"Starting DNS server on {self.ip}")
        dns.run_catchall(self.ip)
        server.run()
        
        logging.info("Webserver started")

    def stop(self):
        server.shutdown()
        logging.info("Webserver shutdown")
        self.ap.active(False)
        logging.info("Access point shutdown")
# from microdot import Microdot, send_file

# def StartServer():
#     app = Microdot()
#     @app.get("/")
#     def index(request):
#         # resp = Response(body=html, status_code=200, headers={"Content-Type": "text/html"})
#         return send_file("index.html")

#     @app.get("/htmx.js")
#     def htmx(request):
#         return send_file("htmx.js")

#     @app.get("/style.css")
#     def css(request):
#         return send_file("style.css")

#     @app.post("/forward")
#     def forward(request):
#         print("forwards")
#         return "forward"

#     @app.post("/stop")
#     def stop(request):
#         print("stop")
#         return "stop"

#     @app.post("/back")
#     def back(request):
#         print("back")
#         return "back"

#     @app.post("/left")
#     def left(request):
#         print("left")
#         return "left"

#     @app.post("/right")
#     def right(request):
#         print("right")
#         return "right"
    
#     app.run(port=80)
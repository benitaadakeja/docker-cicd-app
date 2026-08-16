from flask import Flask 
 
app = Flask(__name__)
@app.route("/") 
def routeReturner(): 
      return "Hello from CI/CD and Docker applications!" 
@app.route("/health") 
def healthChecks(): 
       return { "status" : "healthy" } 
 
if __name__ == "__main__": 
   app.run( host="0.0.0.0", port=5000) 
 
 

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    #print("Hola Mundo<hr>")
    #return HttpResponse('Hello from Python!! 17072020')
    return render(request, "index.html")

@app.route('/my-link/')
def my_link():
     print 'I got clicked!'

     return 'Click.'

if __name__ == '__main__':
     app.run(debug=True)
        

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

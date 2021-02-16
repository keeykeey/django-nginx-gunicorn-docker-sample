#from django.shortcuts import render
from django.http import HttpResponse

template ='''
    <html>
    <head>
      <style type="text/css">
        p {color:red;
           line-height:1.5;
        }
      </style>
    </head>
    <body>
      <p>hello nginx</p>
    </body>
    </html>'''

def hello(request):
        return HttpResponse(template)

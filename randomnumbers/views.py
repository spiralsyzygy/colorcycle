from django.shortcuts import render
from django.http import HttpResponse
import json
import random

def nine_random_numbers(request):
    a = []
    min, max = 100, 255
    for i in xrange(9):
        a.append('{0:0{width}}{1:0{width}}{2:0{width}}'.format(
                random.randrange(min,max), random.randrange(min,max), random.randrange(min,max), width=3))
        
    return HttpResponse(json.dumps(a), content_type="application/json")  
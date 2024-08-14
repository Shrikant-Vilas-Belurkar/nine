from django.shortcuts import render

# Create your views here.
def two(r):
    return render(r, 'two.html')
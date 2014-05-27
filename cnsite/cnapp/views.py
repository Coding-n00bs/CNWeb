from django.shortcuts import render

# Create Views Here
def index(request):
    return render(request, 'cnapp/index.html')

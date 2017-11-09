from django.shortcuts import render

# Create your views here. This goes to the templates folder and searches for blog/post_list.html
def post_list(request):
    return render(request, 'blog/post_list.html')
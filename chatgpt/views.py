from django.http import HttpResponse
from django.shortcuts import render
from .apiServices import chatpgt
from django.http import JsonResponse

def home(request):
    return HttpResponse("Hello, Django!")

def chat(request):
    if request.method =='POST':
        prompt = request.POST.get('prompt')
        print(prompt)
        context = {}
        response = chatpgt.fetch_chatgpt(prompt)
        context['response'] = response
        print(context['response'])
        return JsonResponse(context, safe=False)
    return render(request, 'chatpage.html')
import random
import requests
from django.shortcuts import render, redirect


def fetch_post(request):
    if request.method == 'GET' and 'fetch' in request.GET:
        post_id = random.randint(1, 100)
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
        data = response.json()

        # Save fetched post in the session
        if 'posts' not in request.session:
            request.session['posts'] = []
        request.session['posts'].append(data)
        request.session.modified = True

        return redirect('success')
    return render(request, 'home.html')


def success(request):
    posts = request.session.get('posts', [])
    return render(request, 'success.html', {'posts': posts})
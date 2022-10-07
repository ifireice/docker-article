from django.shortcuts import render
import random

def index(request):
    images = ["https://images.freeimages.com/images/large-previews/c22/cat-1395746.jpg",
              "https://images.freeimages.com/images/large-previews/b5c/cat-yawning-1403730.jpg",
              "https://images.freeimages.com/images/large-previews/f80/leopard-1-1249438.jpg",
              "https://images.freeimages.com/images/large-previews/415/lucky-cat-1421225.jpg",
              "https://images.freeimages.com/images/large-previews/c37/calico-cat-1561584.jpg"
              ]
    template = 'cats/index.html'
    url = random.choice(images)
    context = {
        'url': url,
    }
    return render(request, template,context)
from django.shortcuts import render

def index(request):
      return render(request, 'artist/index.html',)
def contact(request):
    return render(request, 'artist/contact.html', )
def gallery(request):
    return render(request, 'artist/gallery.html')
def services(request):
    return render(request, 'artist/services.html',)
def single(request):
    return render(request, 'artist/single.html',)
def typo(request):
    return render(request, 'artist/typo.html',
                  )
def about(request):
    return render(request, 'artist/about.html',
                )
def ttt(request):
    return render(request, 'artist/index1.html',)

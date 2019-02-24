from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def result(req):
    text = req.GET['fulltext']
    words = text.split(' ')
    word_dic = {}
    for w in words:
        if  w in word_dic:
            word_dic[w] += 1
        else:
            word_dic[w] = 1
    
    return render(req, 'result.html', {
        'full': text,
        'length': len(words),
        'dic' : word_dic.items()
    })
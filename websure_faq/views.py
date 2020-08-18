from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Question

# Create your views here.

def index(request):
    question = Question.objects.all()
    quotation = Question.objects.filter(header='Quotation')
    newbusiness=Question.objects.filter(header='New Business')
    paginator=Paginator(question,1)
    page_number=request.GET.get('page',1)
    page_obj=paginator.get_page(page_number)
    if page_obj.has_next():
        next_url=f'?page={page_obj.next_page_number()}'
    else:
        next_url=''
    if page_obj.has_previous():
        prev_url=f'?page={page_obj.previous_page_number()}'
    else:
        prev_url=''
    return render(request,'index.html',{
        'Question':question,
         'Quotation':quotation,
         'newbusiness': newbusiness,
         'context':page_obj,
         'next_page_url':next_url,
         'previous_page_url':prev_url
        })
    
def search(request):
    try:
        q=request.GET.get('q')
    except:
        q=None
    if q:
        question = Question.objects.filter(question_text__icontains=q)
        context={'query': q,'question':question}
        template ='results.html'
    else:
        context={}
        template = 'index.html'

    return render(request,template,context)


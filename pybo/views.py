from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from pybo.models import Question, Answer
from pybo.forms import QuestionForm

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = { 'question_list': question_list }
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = { 'question' : question }
    return render(request, 'pybo/question_detail.html', context)

def reply(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:pybo_detail', question_id=question.id)

def write(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:pybo_index')
        else:
            context = {'form': form}
            return render(request, 'pybo/question_write.html', context)
    else:
        form = QuestionForm()
        context = {'form': form}
        return render(request, 'pybo/question_write.html', context)
        
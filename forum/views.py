from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateQuestion, PostComment
from .models import Question, Comment

# Create your views here.
def forum(request):
    term = ''
    questions = Question.objects.order_by('date')[::-1]
    num = len(questions)

    if 'search' in request.GET:
        term = request.GET['search']
        questions = Question.objects.filter(question__icontains=term)[::-1]
    
    args = {'questions': questions, 'num': num, 'term': term}
    return render(request, 'forum/help.html', args)

def your_ques(request):
    term = ''
    questions = Question.objects.filter(creator_id__exact=request.user.pk)
    num = len(questions)

    if 'search' in request.GET:
                term = request.GET['search']
                questions = questions.filter(question__icontains=term)
    
    args = {'questions': questions, 'num': num, 'term': term}
    return render(request, 'forum/your_ques.html', args)

def create_question(request):
    qType = 'create'

    if request.method == 'POST':
        form = CreateQuestion(request.POST)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.question = form.cleaned_data['question']
            ques.content = form.cleaned_data['content']
            ques.creator = request.user
            form.save()
            return redirect('forum')
    else:
        form = CreateQuestion()

        args = {'form': form, 'qType': qType}
        return render(request, 'forum/create_question.html', args)

def edit_question(request, pk):
    qType = 'edit'
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        form = CreateQuestion(request.POST, instance=question)
        if form.is_valid():
            ques = form.save(commit=False)
            ques.creator = request.user
            form.save()
            return redirect('your_ques')

    else:
        form = CreateQuestion(instance=question)
        return render(request, 'forum/create_question.html', {'form': form, 'qType': qType})

def view_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    comments = Comment.objects.filter(post_id__exact=pk)
    com = len(comments)

    if request.method == 'POST':
        form = PostComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.creator = request.user
            comment.post_id = pk
            comment.user_id = request.user.pk
            form.save()
            # return redirect('')

    else:
        form = PostComment()

    args = {'question': question, 'comments': comments, 'com': com, 'form': form}
    return render(request, 'forum/view_question.html', args)

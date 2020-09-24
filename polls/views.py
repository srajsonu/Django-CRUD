from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question


def index(request):
    latest_quest_list = Question.objects.order_by('-pub_date')[:5]

    template = loader.get_template('polls/index.html')

    context = {'latest_question_list': latest_quest_list}

    # output = ', '.join([q.question_text for q in latest_quest_list])

    # return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)


def owner(request):
    return HttpResponse("Hello, world. 198dd5fb is the polls index.")


# def detail(request, question_id):
#
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist')
#
#     return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

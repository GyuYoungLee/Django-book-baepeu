from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from polls.models import Question, Choice


def index_page(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


class IndexPageView(ListView):
    # model = Question
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:2]

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


def detail_page(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {"question": question}
    return render(request, 'polls/detail.html', context)


class DetailPageView(DetailView):
    # path 파라미터로 pk를 받음
    model = Question
    template_name = 'polls/detail.html'


def result_page(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {"question": question}
    return render(request, 'polls/result.html', context)


class ResultPageView(DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except Choice.DoesNotExist:
        context = {
            'question': question,
            'error_message': 'you didnt select a choice'
        }
        return render(request, 'polls/detail.html', context)

    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=[question.id]))

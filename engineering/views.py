from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EngineeringOutcome, EngineeringExam
# Create your views here.
@login_required
def deshboard(request):

    qs = EngineeringOutcome.objects.filter(user=request.user).order_by('-exam')
    d = []
    for x in qs:
        d.append(x.exam)

    q = EngineeringExam.objects.filter(name__in=d)

    context = {
        'result': qs,
        'exam': q
    }

    return render(request, 'engineering/deshboard.html', context)


def detail(request, exam_id):

    all_result = EngineeringOutcome.objects.filter(user=request.user).\
                    order_by('-exam')
    exams = []
    for x in all_result:
        exams.append(x.exam)

    exa = EngineeringExam.objects.filter(name__in=exams)

    if exam_id:
        all_result = []
        all_result = EngineeringOutcome.objects.filter(
                                    user=request.user,
                                    exam=exam_id).order_by('-exam')
    context = {
        'result': all_result,
        'exam': exa
    }

    return render(request, 'engineering/deshboard.html', context)

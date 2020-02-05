from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EngineeringOutcome, EngineeringExam
from .models import EngineeringSemester, EngineeringSubject, EngineeringExamApplication, EngineeringExamApplicationSubject, EngineeringExamApplicationSubjectUser
from .forms import ExamForm, SubjectFormset
from django.shortcuts import redirect

# Create your views here.
@login_required
def deshboard(request):

    qs = EngineeringOutcome.objects.filter(user=request.user).order_by('-exam')
    d = []
    for x in qs:
        d.append(x.exam)

    q = EngineeringExam.objects.filter(name__in=d)

    if request.method == 'GET':
        examfom = ExamForm(request.GET or None)
        formset = SubjectFormset(request.GET or None)
    elif request.method == 'POST':
        examfom = ExamForm(request.POST)
        formset = SubjectFormset(request.POST)
        if examfom.is_valid() and formset.is_valid():
            # first save this book, as its reference will be used in `Author`

            examfom = examfom.save(commit=False)
            examfom.user = request.user  # The logged-in user
            examfom.save()

            for form in formset:

                form = form.save(commit=False)
                form.form = examfom  # The logged-in user
                form.save()
                obj, created = EngineeringExamApplicationSubject.objects.get_or_create(form=examfom, stream=form.stream, semester=form.semester, subject=form.subject)
                obj.save()
                # print(form.cleaned_data['stream'])
                # print(form.cleaned_data['semester'])
                # print(form.cleaned_data['subject'])
            return redirect('engineering:deshboard')

    context = {
        'result': qs,
        'exam': q,
        'form': examfom,
        'formset': formset,
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

    if request.method == 'GET':
        examfom = ExamForm(request.GET or None)
        formset = SubjectFormset(request.GET or None)
    elif request.method == 'POST':
        examfom = ExamForm(request.POST)
        formset = SubjectFormset(request.POST)
        if examfom.is_valid() and formset.is_valid():
            # first save this book, as its reference will be used in `Author`

            examfom = examfom.save(commit=False)
            examfom.user = request.user  # The logged-in user
            examfom.save()

            for form in formset:

                form = form.save(commit=False)
                form.form = examfom  # The logged-in user
                form.save()
                obj, created = EngineeringExamApplicationSubject.objects.get_or_create(form=examfom, stream=form.stream, semester=form.semester, subject=form.subject)
                obj.save()
                # print(form.cleaned_data['stream'])
                # print(form.cleaned_data['semester'])
                # print(form.cleaned_data['subject'])
            return redirect('engineering:deshboard')

    context = {
        'result': all_result,
        'exam': exa,
        'form': examfom,
        'formset': formset,
    }

    return render(request, 'engineering/deshboard.html', context)


# def post_new(request):
#     form = ExamForm()
#     return render(request, 'engineering/fom.html', {'form': form})

def load_semester(request):
    stream_id = request.GET.get('stream')
    semester = EngineeringSemester.objects.filter(stream_id=stream_id)
    print(semester)
    return render(request, 'hr/semester_list_options.html', {'semester': semester})


def load_subject(request):
    stream_id = request.GET.get('stream')
    semester_id = request.GET.get('semester')
    print(semester_id)
    print(stream_id)
    subject = EngineeringSubject.objects.filter(stream_id=stream_id, semester_id=semester_id)
    print(subject)
    return render(request, 'hr/subject_list_options.html', {'subject': subject})


def post_new(request):
    template_name = 'engineering/fom.html'
    if request.method == 'GET':
        examfom = ExamForm(request.GET or None)
        formset = SubjectFormset(request.GET or None)
    elif request.method == 'POST':
        examfom = ExamForm(request.POST)
        formset = SubjectFormset(request.POST)
        if examfom.is_valid() and formset.is_valid():
            # first save this book, as its reference will be used in `Author`

            examfom = examfom.save(commit=False)
            examfom.user = request.user  # The logged-in user
            examfom.save()

            for form in formset:

                form = form.save(commit=False)
                form.form = examfom  # The logged-in user
                form.save()
                obj, created = EngineeringExamApplicationSubject.objects.get_or_create(form=examfom, stream=form.stream, semester=form.semester, subject=form.subject)
                obj.save()
                # print(form.cleaned_data['stream'])
                # print(form.cleaned_data['semester'])
                # print(form.cleaned_data['subject'])
            return redirect('engineering:deshboard')
    return render(request, template_name, {
        'form': examfom,
        'formset': formset,
    })




# def create_book_with_authors(request):
#     template_name = 'engineering/fom.html'
#     username = "not logged in"
   
#     if request.method == "POST":
#         #Get the posted form
#         MyLoginForm = LoginForm(request.POST)
      
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username']
#     else:
#         MyLoginForm = Loginform()
		
#     return render(request, template_name, {"username" : username})

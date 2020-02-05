from django import forms

from .models import EngineeringExamApplication, \
                    EngineeringExamApplicationSubject, \
                    EngineeringSubject, \
                    EngineeringExam, \
                    EngineeringExamApplicationSubjectUser

from django.forms import modelformset_factory
from django.forms import formset_factory, inlineformset_factory


class ExamForm(forms.ModelForm):
    class Meta:
        model = EngineeringExamApplication
        fields = ('exam', 'exam_type',)


class SubjectForm(forms.ModelForm):
    class Meta:
        model = EngineeringExamApplicationSubjectUser
        fields = ('stream', 'semester', 'subject',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['semester'] = forms.ChoiceField()
        self.fields['subject'] = forms.ChoiceField()


SubjectFormset = inlineformset_factory(
                        EngineeringExamApplication,
                        EngineeringExamApplicationSubjectUser,
                        form=SubjectForm,
                        extra=5,
                )


# SubjectFormSet = formset_factory(SubjectForm, extra=2)


# -----------------------------------------------------------------------
# model form with specific field
# class ExamForm(forms.ModelForm):
#     class Meta:
#         model = EngineeringExamApplication
#         fields = ('exam', 'exam_type',)


# model form with metod and customize model field
# and update data
# class ExamForm(forms.ModelForm):
#     class Meta:
#         model = EngineeringExamApplication
#         fields = ('exam', 'exam_type',)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         EXAM_CHOICES = (
#             ('R', 'Reguler'),
#             ('K', 'KT'),
#         )
#         self.fields['exam_type'] = forms.ChoiceField(
#                                                     label=('exam'),
#                                                     choices=EXAM_CHOICES
#                                                 )
#         data = EngineeringExam.objects.all()
#         self.fields['exam'] = forms.ChoiceField(
#             label=('exxam'),
#             choices=[('------', '------')] + [(d.id, d.name) for d in data],
#             widget=forms.Select(attrs={'class': 'span12'})
#         )


# normal form with init method and data bind
# class ExamForm(forms.Form):
#     exam_type = forms.ChoiceField()
#     exam = forms.ChoiceField()

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         EXAM_CHOICES = (
#             ('R', 'Reguler'),
#             ('K', 'KT'),
#         )

#         self.fields['exam_type'] = forms.ChoiceField(
#                                                     label=('exam'),
#                                                     choices=EXAM_CHOICES
#                                                 )

#         data = EngineeringExam.objects.all()
#         self.fields['exam'] = forms.ChoiceField(
#             label=('exxam'),
#             choices=[(d.id, d.name) for d in data],
#             widget=forms.Select(attrs={'class': 'span12'})
#         )

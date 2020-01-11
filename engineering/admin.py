from django.contrib import admin
from .models import *
# from django_admin_listfilter_dropdown.filters import DropdownFilter, \
#         RelatedDropdownFilter, ChoiceDropdownFilter


# Register your models here.
class EngineeringSemesterAdmin(admin.ModelAdmin):
    list_display = ('id', 'semester',)
    list_display_links = ('semester',)
    search_fields = ('semester',)
    list_per_page = 50


class EngineeringStreamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_form',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('short_form',)
    list_per_page = 50
    prepopulated_fields = {"stream_slug": ("name",)}


class EngineeringExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'exam_start_date', 'exam_end_date',)
    list_display_links = ('name', 'code',)
    search_fields = ('name',)
    list_per_page = 50
    prepopulated_fields = {"exam_slug": ("name",)}


class EngineeringSubjectClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'stream', 'semester')
    list_display_links = ('id',)
    search_fields = ('semester__semester', 'stream__name')
    list_per_page = 50
    list_filter = ('semester', 'stream')


class EngineeringOutcomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'exam', 'subject', 'stream_sem',
                    'i_assessment', 'internal_assessment_grade', 't_work',
                    'term_work_grade', 'o_exam', 'oral_grade', 'o_p_exam',
                    'oral_and_practical_grade', 'e_s_exam',
                    'end_sem_exam_grade',)
    list_display_links = ('user',)
    search_fields = ('user__username',)
    list_per_page = 50
    raw_id_fields = ('user', 'subject',)
    # list_filter = (('stream_sem', RelatedDropdownFilter),
    #                ('subject', RelatedDropdownFilter),  'exam')

    admin.site.empty_value_display = '-'

    # def get_queryset(self, request):
    #     qs = super(EngineeringOutcomeAdmin, self).get_queryset(request)
    #     if request.user.userprofile.is_lecturer:
    #         qs = qs.filter(subject=14)
    #     return qs

    # def changelist_view(self, request, extra_context=None):
    #     if request.user.userprofile.is_lecturer:
    #         self.list_display = (
    #                             'user', 'exam', 'subject', 'stream_sem',
    #                             'internal_assessment_grade',
    #                             'term_work_grade', 'oral_grade',
    #                             'oral_and_practical_grade',
    #                             'end_sem_exam_grade',)
    #     return super(EngineeringOutcomeAdmin, self).changelist_view(
    #                                                     request,
    #                                                     extra_context)

    # def get_form(self, request, obj=None, **kwargs):
    #     if request.user.userprofile.is_lecturer:
    #         self.fields = ('user', 'exam', 'subject',
    #                        'stream_sem',)  # same thing
    #         self.readonly_fields = ('user', 'exam', 'subject', 'stream_sem',)
    #     return super(EngineeringOutcomeAdmin, self).get_form(
    #                                                         request,
    #                                                         obj,
    #                                                         **kwargs)

    # def get_list_filter(self, request):
    #     if request.user.userprofile.is_lecturer:
    #         self.list_filter = (('subject', RelatedDropdownFilter),  'exam')

    #     return self.list_filter


admin.site.register(EngineeringSemester, EngineeringSemesterAdmin)
admin.site.register(EngineeringStream, EngineeringStreamAdmin)
admin.site.register(EngineeringExam, EngineeringExamAdmin)
admin.site.register(EngineeringSubjectClassification,
                    EngineeringSubjectClassificationAdmin)
admin.site.register(EngineeringOutcome, EngineeringOutcomeAdmin)

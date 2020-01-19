from django.db import models
from django.utils.text import slugify
from django.utils.html import format_html
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import CusetomUser

from smart_selects.db_fields import ChainedForeignKey


class EngineeringBook(models.Model):
    name = models.CharField(max_length=100)
    book_slug = models.SlugField(max_length=150, unique=True)
    primary_author_first_name = models.CharField(
                                                "Author First",
                                                max_length=100,
                                                blank=True)
    primary_author_last_name = models.CharField(
                                                "Author Last",
                                                max_length=100,
                                                blank=True)
    pub_date = models.DateField("Book Pub Date", blank=True, null=True)

    def __str__(self):
        return self.name


class EngineeringStream(models.Model):
    name = models.CharField(max_length=50, unique=True)
    stream_slug = models.SlugField(max_length=150, unique=True)
    short_form = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name


class EngineeringSemester(models.Model):
    stream = models.ForeignKey(
                        EngineeringStream,
                        blank=True,
                        null=True,
                        on_delete=models.DO_NOTHING)
    semester = models.IntegerField()

    def __str__(self):
        return str(self.semester) + ' - ' + str(self.stream)


class EngineeringSubject(models.Model):
    name = models.CharField(max_length=150)
    subject_slug = models.SlugField(max_length=150, unique=True)
    code = models.CharField(max_length=250)
    book = models.ManyToManyField(EngineeringBook, blank=True)
    stream = models.ForeignKey(
                                EngineeringStream,
                                blank=True,
                                null=True,
                                on_delete=models.DO_NOTHING)
    semester = ChainedForeignKey(
                                EngineeringSemester,
                                chained_field="stream",
                                chained_model_field="stream",
                                on_delete=models.DO_NOTHING,
                                blank=True, null=True
                                )

    def __str__(self):
        return self.code + " - " + self.name


class EngineeringExam(models.Model):
    name = models.CharField(max_length=50, unique=True)
    exam_slug = models.SlugField(max_length=150, unique=True)
    code = models.CharField(max_length=50)
    exam_start_date = models. DateField()
    exam_end_date = models. DateField()

    def __str__(self):
        return self.name


class EngineeringOutcome(models.Model):

    class Meta:
        verbose_name = 'Exam Result'
        # verbose_name_plural = 'Engineering Students Result'

    GRADE_CHOICES = (
        ('O', 'O'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('P', 'P'),
        ('F', 'F'),
    )
    EXAM_CHOICES = (
        ('R', 'Reguler'),
        ('K', 'KT'),
    )

    user = models.ForeignKey(CusetomUser, on_delete=models.CASCADE)
    exam = models.ForeignKey(EngineeringExam, on_delete=models.DO_NOTHING)
    stream = models.ForeignKey(
                                EngineeringStream,
                                null=True,
                                blank=True,
                                on_delete=models.DO_NOTHING
                            )
    semester = ChainedForeignKey(
                                EngineeringSemester,
                                chained_field="stream",
                                chained_model_field="stream",
                                on_delete=models.DO_NOTHING,
                                blank=True,
                                null=True
                                )
    subject = ChainedForeignKey(
                                EngineeringSubject,
                                chained_field="semester",
                                chained_model_field="semester",
                                on_delete=models.DO_NOTHING
                                )
    exam_type = models.CharField(
                            max_length=1,
                            choices=EXAM_CHOICES,
                            null=True,
                            blank=True)
    internal_assessment = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(20), MinValueValidator(0)],
        help_text='Marks obtained out of 20'
    )
    internal_assessment_grade = models.CharField(
        max_length=1,
        choices=GRADE_CHOICES,
        null=True,
        blank=True,
        help_text="")
    term_work = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(25), MinValueValidator(0)],
        help_text='Marks obtained out of 25'
    )
    term_work_grade = models.CharField(
        max_length=1,
        choices=GRADE_CHOICES,
        null=True,
        blank=True,
        help_text=""
    )
    oral = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(25), MinValueValidator(0)],
        help_text='Marks obtained out of 25'
    )
    oral_grade = models.CharField(
        max_length=1,
        choices=GRADE_CHOICES,
        null=True,
        blank=True,
        help_text=""
    )
    oral_and_practical = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(25), MinValueValidator(0)],
        help_text='Marks obtained out of 25'
    )
    oral_and_practical_grade = models.CharField(
        max_length=1,
        choices=GRADE_CHOICES,
        null=True,
        blank=True,
        help_text=""
    )
    end_sem_exam = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(80), MinValueValidator(0)],
        help_text='Marks obtained out of 80'
    )
    end_sem_exam_grade = models.CharField(
        max_length=1,
        choices=GRADE_CHOICES,
        null=True,
        blank=True,
        help_text="""('O', 'M>=80'),('A', '75>=M<80'),('B', '70>=M<75'),
                    ('C', '60>=M<70'),('D', '50>=M<60'),('E', '45>=M<50'),
                    ('P', '40>=M<45'),('F', 'M<40')"""
    )

    def __str__(self):
        return self.user.username

    def e_s_exam(self):

        if(self.end_sem_exam < 30):
            return format_html(
                    '<span style="color: #FF0000;">{}</span>',
                    self.end_sem_exam,)
        elif(self.end_sem_exam > 75):
            return format_html(
                    '<span style="color: #00FF00;">{}</span>',
                    self.end_sem_exam,)
        else:
            return self.end_sem_exam

    def o_p_exam(self):

        if(self.oral_and_practical < 10):
            return format_html(
                    '<span style="color: #FF0000;">{}</span>',
                    self.oral_and_practical,)
        elif(self.oral_and_practical > 20):
            return format_html(
                    '<span style="color: #00FF00;">{}</span>',
                    self.oral_and_practical,)
        else:
            return self.oral_and_practical

    def o_exam(self):

        if(self.oral < 10):
            return format_html(
                    '<span style="color: #FF0000;">{}</span>',
                    self.oral,)
        elif(self.oral > 20):
            return format_html(
                    '<span style="color: #00FF00;">{}</span>',
                    self.oral,)
        else:
            return self.oral

    def t_work(self):

        if(self.term_work < 10):
            return format_html(
                    '<span style="color: #FF0000;">{}</span>',
                    self.term_work,)
        elif(self.term_work > 20):
            return format_html(
                    '<span style="color: #00FF00;">{}</span>',
                    self.term_work,)
        else:
            return self.term_work

    def i_assessment(self):

        if(self.internal_assessment < 8):
            return format_html(
                    '<span style="color: #FF0000;">{}</span>',
                    self.internal_assessment,)
        elif(self.internal_assessment > 15):
            return format_html(
                    '<span style="color: #00FF00;">{}</span>',
                    self.internal_assessment,)
        else:
            return self.internal_assessment


class EngineeringExamApplication(models.Model):
    class Meta:
        verbose_name = 'Exam Application'
        # verbose_name_plural = 'Engineering Students Result'

    EXAM_CHOICES = (
        ('R', 'Reguler'),
        ('K', 'KT'),
    )

    user = models.ForeignKey(CusetomUser, on_delete=models.CASCADE)
    exam = models.ForeignKey(EngineeringExam, on_delete=models.CASCADE)
    # stream = models.ForeignKey(
    #                             EngineeringStream,
    #                             null=True,
    #                             blank=True,
    #                             on_delete=models.DO_NOTHING
    #                         )
    # semester = models.ForeignKey(
    #                             EngineeringSemester,
    #                             null=True, blank=True,
    #                             on_delete=models.DO_NOTHING
    #                         )
    exam_type = models.CharField(
                            max_length=1,
                            choices=EXAM_CHOICES,
                            null=True,
                            blank=True)

    def __str__(self):
        return self.user + " - " + self.exam


class EngineeringExamApplicationSubject(models.Model):
    form = models.ForeignKey(
                                EngineeringExamApplication,
                                on_delete=models.CASCADE
                            )
    stream = models.ForeignKey(
                                EngineeringStream,
                                null=True,
                                blank=True,
                                on_delete=models.DO_NOTHING
                            )
    semester = ChainedForeignKey(
                                EngineeringSemester,
                                chained_field="stream",
                                chained_model_field="stream",
                                on_delete=models.DO_NOTHING,
                                blank=True,
                                null=True
                            )
    subject = ChainedForeignKey(
                            EngineeringSubject,
                            chained_field="semester",
                            chained_model_field="semester",
                            on_delete=models.DO_NOTHING
                        )

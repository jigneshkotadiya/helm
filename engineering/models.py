from django.db import models
from django.utils.text import slugify
from django.utils.html import format_html
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import CusetomUser


# Create your models here.
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


class EngineeringSubject(models.Model):
    name = models.CharField(max_length=150)
    subject_slug = models.SlugField(max_length=150, unique=True)
    code = models.CharField(max_length=250)
    book = models.ManyToManyField(EngineeringBook, blank=True)

    def __str__(self):
        return self.name + " " + self.code

class EngineeringSemester(models.Model):
    semester = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.semester)


class EngineeringStream(models.Model):
    name = models.CharField(max_length=50, unique=True)
    stream_slug = models.SlugField(max_length=150, unique=True)
    short_form = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name


class EngineeringSubjectClassification(models.Model):
    subject = models.ManyToManyField(EngineeringSubject, blank=True)
    stream = models.ForeignKey(EngineeringStream, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(
        EngineeringSemester,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return str(self.stream) + " " + str(self.semester)


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
        verbose_name = 'Engineering Student Result'
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

    user = models.ForeignKey(CusetomUser, on_delete=models.CASCADE)
    exam = models.ForeignKey(EngineeringExam, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(EngineeringSubject, on_delete=models.DO_NOTHING)
    stream_sem = models.ForeignKey(
        EngineeringSubjectClassification,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
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

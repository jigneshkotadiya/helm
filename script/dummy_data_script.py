import os
import datetime
import django
import random
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                os.path.pardir)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helm.settings")
django.setup()

if django:
    print("django setuped")
    from django.utils import timezone
    from django.utils.text import slugify
    from django.contrib.auth.models import User
    from engineering.models import *
    from faker import Faker
    from allauth.account.models import EmailAddress


fake = Faker()


def create_user_profile(N):

    for i in range(2, N+1):
        print("...................................")
        print(i)

        profile = fake.simple_profile()
        user_id = i
        birth_date = profile['birthdate']
        gender = profile['sex']
        address_one = fake.street_address()
        address_two = fake.street_name()
        country = random.randint(1, 247)
        state = ""
        citie = ""
        phone_number = ""

        UserProfile.objects.create(user_id=user_id, birth_date=birth_date,
                                   gender=gender,
                                   address_one=address_one,
                                   address_two=address_two,
                                   country_id=country)

# create_user_profile(200)
# print("Ya Hoooooo Profile has been created")


def create_engineering_semester(N):

    for i in range(1, N+1):
        print("...................................")
        print(i)

        EngineeringSemester.objects.create(semester=i)

# create_engineering_semester(8)
# print("Ya Hoooooo Semister has been created")


def create_engineering_stream(Stream):
    name = Stream
    stream_slug = slugify(name)
    EngineeringStream.objects.create(
                            name=name,
                            stream_slug=stream_slug)

# create_engineering_stream("Computer Engineering")
# create_engineering_stream("Mechanical Engineering")
# create_engineering_stream("Electrical Engineering")
# create_engineering_stream("Civil Engineering")
# create_engineering_stream("Chemical Engineering")
# create_engineering_stream("Information Technology Engineering")
# print("Ya Hoooooo Stream has been created")


def create_engineering_exam(N):
    year = datetime.datetime.today().year
    for y in range(2010, year+1):
        for m in range(1):

            start_date = str(y) + " May"
            end_date = str(y) + " June"

            name = "Exam " + start_date
            exam_slug = slugify(name)
            code = "DTE" + exam_slug
            exam_start_date = datetime.date(year=y, month=3, day=1)
            exam_end_date = datetime.date(year=y, month=4, day=1)

            EngineeringExam.objects.create(name=name, exam_slug=exam_slug,
                                           code=code,
                                           exam_start_date=exam_start_date,
                                           exam_end_date=exam_end_date)

            start_date = str(y) + " November"
            end_date = str(y) + " December"

            name = "Exam " + start_date
            exam_slug = slugify(name)
            exam_start_date = datetime.date(year=y, month=11, day=1)
            exam_end_date = datetime.date(year=y, month=12, day=1)
            code = "DTE" + exam_slug

            EngineeringExam.objects.create(name=name, exam_slug=exam_slug,
                                           code=code,
                                           exam_start_date=exam_start_date,
                                           exam_end_date=exam_end_date)


# create_engineering_exam(10)
# print("Ya Hoooooo Exam has been created")


def create_Student_outcomes(N):

    for i in range(1, N+1):
        print("...................................")
        print(i)
        user_id = 2
        # user_id = random.randint(2, 100)
        # dsip
        subject_id = 33  # dsip
        # subject_id = random.randint(1, 157)
        # exam_id = random.randint(1, 20)
        # exam_id = random.randint(1, 20)
        exam_id = 19

        stream_sem = 2

        # if(subject_id <= 157 and subject_id >= 148):
        #         print(",./")
        #         stream_sem = 16
        # elif(subject_id <= 147 and subject_id >= 139):
        #         print(",./")
        #         stream_sem = 15
        # elif(subject_id <= 138 and subject_id >= 129):
        #         print(",./")
        #         stream_sem = 14
        # elif(subject_id <= 128 and subject_id >= 120):
        #         print(",./")
        #         stream_sem = 13
        # elif(subject_id <= 119 and subject_id >= 110):
        #         print(",./")
        #         stream_sem = 12
        # elif(subject_id <= 109 and subject_id >= 100):
        #         print(",./")
        #         stream_sem = 11
        # elif(subject_id <= 99 and subject_id >= 85):
        #         print(",./")
        #         stream_sem = 10
        # elif(subject_id <= 84 and subject_id >= 71):
        #         stream_sem = 9
        # elif(subject_id <= 70 and subject_id >= 62):
        #         stream_sem = 8
        # elif(subject_id <= 61 and subject_id >= 53):
        #         stream_sem = 7
        # elif(subject_id <= 52 and subject_id >= 46):
        #         stream_sem = 6
        # elif(subject_id <= 45 and subject_id >= 38):
        #         stream_sem = 5
        # elif(subject_id <= 37 and subject_id >= 29):
        #         stream_sem = 4
        # elif(subject_id <= 28 and subject_id >= 20):
        #         stream_sem = 3
        # elif(subject_id <= 19 and subject_id >= 10):
        #         stream_sem = 2
        # elif(subject_id <= 9 and subject_id >= 1):
        #         stream_sem = 1
        # else:
        #         print("Error")

        print("subject id ", subject_id)
        internal_assessment = random.randint(1, 20)
        term_work = random.randint(1, 25)
        oral = 0
        oral_and_practical = random.randint(1, 25)
        end_sem_exam = random.randint(1, 80)

        print("stream_sem ", stream_sem)
        EngineeringOutcome.objects.create(
                                    user_id=user_id,
                                    subject_id=subject_id,
                                    exam_id=exam_id,
                                    internal_assessment=internal_assessment,
                                    term_work=term_work,
                                    oral_and_practical=oral_and_practical,
                                    oral=oral,
                                    end_sem_exam=end_sem_exam,
                                    stream_sem_id=stream_sem)


# create_Student_outcomes(1)
# print("Ya Hoooooo Student  Exam Marks has been entered")

def Sign_Up(N):

    for _ in range(N):
        print(N)
        profile = fake.simple_profile()
        # id = N
        password = ",./,./,./"
        # last_login = "2019-07-11 18:23:09.365054"
        # is_superuser = "0",
        username = profile['username']
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = profile['mail']
        # is_staff = "0"
        # is_active = "1"

        q1 = User.objects.filter(username=username, email=email)
        print(q1)

        # q1 = User.objects.filter(username=username)
        if (not q1):
            d = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name
                    )
            print(d)
            print(d.id)

            e = EmailAddress.objects.create(
                        user_id=d.id,
                        email=d.email,
                        verified=1,
                        primary=1
                    )
            print(e)
            u = UserProfile.objects.create(user_id=d.id, is_student=1)
            print(u)

# Sign_Up(1)
# print("Ya Hoooooo User has been created")

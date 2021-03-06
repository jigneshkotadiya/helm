# Generated by Django 2.2 on 2020-01-19 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engineering', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineeringExamApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(blank=True, choices=[('R', 'Reguler'), ('K', 'KT')], max_length=1, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineering.EngineeringExam')),
            ],
            options={
                'verbose_name': 'Exam Application',
            },
        ),
        migrations.CreateModel(
            name='EngineeringExamApplicationSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineering.EngineeringExamApplication')),
            ],
        ),
        migrations.AlterModelOptions(
            name='engineeringoutcome',
            options={'verbose_name': 'Exam Result'},
        ),
        migrations.RemoveField(
            model_name='engineeringoutcome',
            name='stream_sem',
        ),
        migrations.AddField(
            model_name='engineeringoutcome',
            name='exam_type',
            field=models.CharField(blank=True, choices=[('R', 'Reguler'), ('K', 'KT')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='engineeringoutcome',
            name='semester',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='stream', chained_model_field='stream', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringSemester'),
        ),
        migrations.AddField(
            model_name='engineeringoutcome',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringStream'),
        ),
        migrations.AddField(
            model_name='engineeringsemester',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringStream'),
        ),
        migrations.AddField(
            model_name='engineeringsubject',
            name='semester',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='stream', chained_model_field='stream', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringSemester'),
        ),
        migrations.AddField(
            model_name='engineeringsubject',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringStream'),
        ),
        migrations.AlterField(
            model_name='engineeringoutcome',
            name='subject',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='semester', chained_model_field='semester', on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringSubject'),
        ),
        migrations.AlterField(
            model_name='engineeringsemester',
            name='semester',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='EngineeringSubjectClassification',
        ),
        migrations.AddField(
            model_name='engineeringexamapplicationsubject',
            name='semester',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='stream', chained_model_field='stream', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringSemester'),
        ),
        migrations.AddField(
            model_name='engineeringexamapplicationsubject',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringStream'),
        ),
        migrations.AddField(
            model_name='engineeringexamapplicationsubject',
            name='subject',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='semester', chained_model_field='semester', on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringSubject'),
        ),
        migrations.AddField(
            model_name='engineeringexamapplication',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringSemester'),
        ),
        migrations.AddField(
            model_name='engineeringexamapplication',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='engineering.EngineeringStream'),
        ),
        migrations.AddField(
            model_name='engineeringexamapplication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

from celery import shared_task
from education.models import course


@shared_task
def update_lesson(pk, model):
    if model == 'course':
        instance = course.objects.filter(pk=pk).first()

    if instance:
        count_lesson = instance.lessons.count

        if count_lesson > 0:
            print('Курс ' + instance.name + ' содержит ' + str(count_lesson) + ' уроков ')

        
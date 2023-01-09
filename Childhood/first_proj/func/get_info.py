from typing import List
from first_proj.models import Category, Event


def life_period(check_period: str):
    self_category = Category.objects.filter(title=check_period)
    result=[self_category]#Первый элемент - категория, второй элемент - список из событий

    if result[0]:
        events=Event.objects.filter(category=self_category[0].id)
        result.append(events)

        str_res: str=f'{result[0][0].title} \n'

        if not result[1]:
            str_res+="There wasn't any events duaring this part of life"
            return str_res

        for i in result[1]:
                str_res+=f"id: {i.id}, title: {i.title}, description: {i.description} \n"

        return str_res

    else: return None





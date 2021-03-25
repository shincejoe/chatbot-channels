from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from mocker.models import Clicks, Users

'''
API for fetching the total number of click for a user
'''


def click_count(request):
    result = []
    context = {}

    user_list = Users.objects.all()
    for user in user_list:
        click_obj = Clicks.objects.filter(user=user).first()
        if click_obj is not None:
            fat_count = 0
            stupid_count = 0
            dumb_count = 0
            user_data = {'username': user.username, 'id': user.id}
            fat_count_obj = Clicks.objects.filter(user=user, type=1).first()
            if fat_count_obj is not None:
                fat_count = fat_count_obj.count
            user_data['fat'] = fat_count
            stupid_count_obj = Clicks.objects.filter(user=user, type=2).first()
            if stupid_count_obj is not None:
                stupid_count = stupid_count_obj.count
            user_data['stupid'] = stupid_count
            dumb_count_obj = Clicks.objects.filter(user=user, type=3).first()
            if dumb_count_obj is not None:
                dumb_count = dumb_count_obj.count
            user_data['dumb'] = dumb_count
            result.append(user_data)
        else:

            user_data = {'username': user.username, 'id': user.id, 'fat':0, 'stupid':0, 'dumb': 0}
            result.append(user_data)
    context['entry_list'] = result
    print(context)
    return render(request, template_name='table_listing.html', context=context)


def get_users(request):
    result_data = []
    users = Users.objects.values().all()
    for user in users:
        user_data = {
            'id': user['id'],
            'username': user['username']
        }
        result_data.append(user_data)
    context = {'users': result_data}
    print(context)
    return JsonResponse(context)

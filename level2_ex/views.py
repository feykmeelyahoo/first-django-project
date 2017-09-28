from django.shortcuts import render
from level2_ex.models import Users


def index(req):

	user_list = Users.objects.order_by("name")
	user_dict = {'user_records': user_list, 'dnm': 2}

	return render(req, 'level2_ex/index.html', context=user_dict)


def index2(req):

	user_list = Users.objects.order_by("last_name")
	user_dict = {'user_records': user_list, 'dnm': 2}

	return render(req, 'level2_ex/index.html', context=user_dict)

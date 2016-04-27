from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, Http404
import random, string
# Create your views here.
class ReactPollView(View):
    def get(self, request, *args, **kwargs):
        data = [
            {'id': 1, 'author': self._create_random_data(), 'comment': self._create_random_data()},
            {'id': 2, 'author': self._create_random_data(), 'comment': self._create_random_data()},
            {'id': 3, 'author': self._create_random_data(), 'comment': self._create_random_data()}
        ]
        return JsonResponse(data, safe=False)

    def _create_random_data(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

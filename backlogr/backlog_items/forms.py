from models import BacklogItem
from django import forms


class BacklogItemForm(forms.ModelForm):
    class Meta:
        model = BacklogItem
        fields = ['user', 'backlog', 'backlog_item_type', 'who', 'what', 'why', 'acceptance_criteria', 'notes', 'story_points', 'business_value']

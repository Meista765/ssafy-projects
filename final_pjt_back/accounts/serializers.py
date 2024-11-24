from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import DefaultAccountAdapter
from finances.models import DepositProducts, InstallmentProducts
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = User
        fields = '__all__'


# custom한 user 모델을 위해서 registerSerializer custom

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=User.GENDER_CHOICES, required=True)
    birth_date = serializers.DateField(required=True, allow_null=True)
    age = serializers.IntegerField(required=False)
    investment_style = serializers.ChoiceField(choices=User.INVESTMENT_STYLE_CHOICES, required=True)
    annual_income = serializers.ChoiceField(choices=User.INCOME_CHOICES, required=False)
    savings_goal = serializers.ChoiceField(choices=User.SAVINGS_GOALS_CHOICES, required=False)

    #  # 만약 password1, password2 필드가 이미 정의되어 있지 않다면 정의합니다.
    # password1 = serializers.CharField(write_only=True)
    # password2 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        data['gender'] = self.validated_data.get('gender', '')
        data['birth_date'] = self.validated_data.get('birth_date', None)
        data['age'] = self.validated_data.get('age', None)
        data['investment_style'] = self.validated_data.get('investment_style', '')
        data['annual_income'] = self.validated_data.get('annual_income', '')
        data['savings_goal'] = self.validated_data.get('savings_goal', None)
        return data
    
    def save(self, request):

        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.gender = self.cleaned_data.get('gender')
        user.birth_date = self.cleaned_data.get('birth_date')
        user.age = self.cleaned_data.get('age')
        user.investment_style = self.cleaned_data.get('investment_style')
        user.annual_income = self.cleaned_data.get('annual_income')
        user.savings_goal = self.cleaned_data.get('savings_goal')
        user.save()
        return user

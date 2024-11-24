# from allauth.account.adapter import DefaultAccountAdapter
# from datetime import date

# class CustomAccountAdapter(DefaultAccountAdapter):
#     def save_user(self, request, user, form, commit=True):
#         user = super().save_user(request, user, form, commit=False)
        
#         # 추가 필드 설정
#         user.first_name = form.cleaned_data.get('first_name')
#         user.last_name = form.cleaned_data.get('last_name')
#         user.gender = form.cleaned_data.get('gender')
#         user.birth_date = form.cleaned_data.get('birth_date')
#         user.age = form.cleaned_data.get('age')
#         user.investment_style = form.cleaned_data.get('investment_style')
#         user.annual_income = form.cleaned_data.get('annual_income')
#         user.savings_goal = form.cleaned_data.get('savings_goal')
    
        
#         if commit:
#             user.save()
#             # ManyToMany 필드는 save 후에 추가
#             if 'deposit_products' in form.cleaned_data:
#                 user.deposit_products.set(form.cleaned_data.get('deposit_products'))
#             if 'savings_products' in form.cleaned_data:
#                 user.savings_products.set(form.cleaned_data.get('savings_products'))
        
#         return user
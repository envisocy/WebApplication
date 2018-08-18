from django.shortcuts import render
from django.contrib.auth import authenticate, login    # 认证库，登陆函数
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q

from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdFrom
from django.contrib.auth.hashers import make_password   # 对明文进行密码加密
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		try:
			user = UserProfile.objects.get(Q(username=username)|Q(email=username))
			if user.check_password(password):
				return user
		except Exception as e:
			return None


class LoginView(View):
	# 继承后，get,post等函数可以直接使用，通过as_view()方法被urls引用
	def get(self, request):
		login_form = LoginForm()
		return render(request, "login.html", {"login_form": login_form})
	
	def post(self, request):
		login_form = LoginForm(request.POST)        # 表单校验，html名称与form的名称一致
		if login_form.is_valid():                   # 检查是否为error
			user_name = request.POST.get("username", "")
			pass_word = request.POST.get("password", "")
			user = authenticate(username=user_name, password=pass_word)
			# 如果验证成功user是个对象，如果失败则为None
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, "index.html")
				else:
					return render(request, "login.html", {"msg": "用户未激活！", "login_form": login_form})
			else:
				return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})   # 数据库验证不通过
		else:
			return render(request, "login.html", {"login_form": login_form})    # 登陆不成功
			# 通过这样的方式，将login_form输出到前端，通过前端对login_form.errors的遍历循环，取出key和error

class RegisterView(View):
	def get(self, request):
		register_form = RegisterForm()
		return render(request, "register.html", {'register_form': register_form})
	
	def post(self, request):
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			user_name = request.POST.get("email", "")
			pass_word = request.POST.get("password", "")
			if not UserProfile.objects.get(email = user_name):
				user_profile = UserProfile()
				user_profile.username = user_name
				user_profile.email = user_name
				user_profile.password = make_password(pass_word)
				user_profile.is_active = False
				user_profile.save()
				# 发送邮件
				send_register_email(user_name, "register")
				# 返回login界面
				return render(request, "login.html")
			else:
				return render(request, "register.html", {'msg':"用户已存在！", 'register_form': register_form})
		else:
			return render(request, "register.html", {'register_form': register_form})


class ActiveUserView(View):
	def get(self, request, active_code):
		all_records = EmailVerifyRecord.objects.filter(code=active_code)
		# active_form = ActiveForm(request.GET)
		if all_records:
			for record in all_records:
				email = record.email
				user = UserProfile.objects.get(email=email)
				user.is_active = True
				user.save()
				return render(request, "login.html")
		else:
			return render(request, "register.html", {"msg": "您的激活链接无效"})


class ForgetPwdView(View):
	def get(self, request):
		forget_form = ForgetForm
		return render(request, "forgetpwd.html", {"forget_form": forget_form})
	
	def post(self, request):
		forget_form = ForgetForm(request.POST)
		if forget_form.is_valid():
			email = request.POST.get("email", "")
			send_register_email(email, "forget")
			return render(request, "send_success.html")
		else:
			return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetView(View):
	def get(self, request, active_code):
		all_records = EmailVerifyRecord.objects.filter(code=active_code)
		if all_records:
			for record in all_records:
				email = record.email
				return render(request, "password_reset.html", {"email": email}) # 需要传送email值，待下个页面传回
		else:
			return render(request, "forgetpwd.html", {"msg": "您的激活链接无效"})
		
		
class ModifyPwdView(View):
	def post(self, request):
		modifypwd_form = ModifyPwdFrom(request.POST)
		if modifypwd_form.is_valid():
			pwd1 = request.POST.get("password1", "")
			pwd2 = request.POST.get("password2", "")
			email = request.POST.get("email", "")
			if pwd1 != pwd2:
				return render(request, "password_reset.html", {"email": email, "msg": "两次输入密码不一致"})
			user = UserProfile.objects.get(email=email)
			user.password = make_password(pwd2)
			user.save()
			return render(request, "login.html", {"msg": "密码修改成功，请登录"})
		else:
			email = request.POST.get("email", "")
			return render(request, "password_reset.html", {"email": email, "modifypwd_form": modifypwd_form})
		
# Create your views here.

# def user_login(request):
# 	if request.method == "POST":
# 		user_name = request.POST.get("username", "")
# 		pass_word = request.POST.get("password", "")
# 		user = authenticate(username=user_name, password=pass_word)
# 		# 如果验证成功user是个对象，如果失败则为None
# 		if user is not None:
# 			login(request, user)    # 登陆
# 			return render(request, "index.html")        # 判断
# 		else:
# 			return render(request, "login.html", {"msg": "账号或密码错误！"})    # 登陆不成功
# 	elif request.method == "GET":
# 		return render(request, "login.html", {})
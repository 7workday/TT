from django.http import JsonResponse
from django.core.cache import cache

from libs.http import render_json
from user.models import User
from user.models import Profile
from user.forms import UserForm
from user.forms import ProfileForm
from user import logics
from common import stat


def get_vcode(request):
    '''用户获取验证码'''
    phonenum = request.GET.get('phonenum')
    success = logics.send_sms(phonenum)
    if success:
        return render_json()
    else:
        raise stat.SmsErr


def submit_vcode(request):
    '''检查短信验证码，同时进行登陆或者注册'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    key = 'Vcode-%s' % phonenum
    cached_vcode = cache.get(key)
    if vcode and vcode == cached_vcode:
        try:
            user = User.objects.get(phonenum=phonenum)  # 获取用户
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)  # 创建新用户

        # 记录用户登陆状态
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        raise stat.VCODE_ERR


def get_profile(request):
    '''获取用户配置'''
    profile, _ = Profile.objects.get_or_create(id=request.uid)
    return render_json(profile.to_dict(), code=stat.OK)


def set_profile(request):
    '''修改用户信息，及用户配置'''
    user_form = UserForm(request.POST)
    profile_form = ProfileForm(request.POST)

    # 验证user表单数据
    if not user_form.is_valid():
        raise stat.UserFormErr(user_form.errors)
    # 验证profile表单数据
    if not profile_form.is_valid():
        raise stat.ProfileFormErr(profile_form.errors)

    # 验修改用户数据
    # update user set nickname='xx', gender='male' where id=uid;
    User.objects.filetr(id=request.uid).update(**user_form.cleaned_data)

    # 修改 profile 数据
    Profile.objects.update_or_create(id=request.uid, defaults=profile_form.cleaned_data)

    return render_json()


def upload_avatar(request):
    return JsonResponse({})

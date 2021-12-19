from django.shortcuts import render, redirect
from Do_an_01.models import Category, Story, Contact
from customers_hdg.forms import *
from customers_hdg.models import *
from Do_an_01.my_module import *
from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Biến toàn cục
story_list = Story.objects.order_by('-public_day')
# Thể loại
list_category = Category.objects.all()
# Slide
story_newest_14 = story_list[0:6]

# Lọc hiển thị nội dung footer
story_newest_3 = story_list[0:5]
def login(request):
    session_status = check_session(request, 'sessionNguoiDung')
    if session_status:
        return redirect('customers_hdg:my_account')

    # Đăng ký
    form = FormDangKy()
    result_regiter = ''
    if request.POST.get('btnDangKy'):
        form = FormDangKy(request.POST, Customer)

        # Kiểm tra email tồn tại hay chưa?
        email = request.POST.get('email')
        nguoi_dung = Customer.objects.filter(email=email)
        if nguoi_dung.count() > 0:
            result_regiter = '''
                <div class="alert alert-warning alert-dismissible fade show" role="alert">
                    Email đã tồn tại. Vui lòng kiểm tra lại.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                '''
        else:
            if form.is_valid() and form.cleaned_data['mat_khau'] == form.cleaned_data['xac_nhan_mat_khau']:
                # hasher = Argon2PasswordHasher()  # salt: 8 bytes
                hasher = PBKDF2PasswordHasher()  # salt: 1 bytes
                request.POST._mutable = True
                post = form.save(commit=False)
                post.ho = form.cleaned_data['ho']
                post.ten = form.cleaned_data['ten']
                post.email = form.cleaned_data['email']
                post.mat_khau = hasher.encode(form.cleaned_data['mat_khau'], '123')
                post.dien_thoai = form.cleaned_data['dien_thoai']
                post.dia_chi = form.cleaned_data['dia_chi']
                post.save()
                result_regiter = '''
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    Đăng ký thông tin thành công.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                '''
    # Đăng nhập
    result_login = ''
    if request.POST.get('btnDangNhap'):
        # Gán biến
        email = request.POST.get('email')
        mat_khau = request.POST.get('mat_khau')
        hasher = PBKDF2PasswordHasher()
        encoded = hasher.encode(mat_khau, '123')

        # Đọc dữ liệu từ DB
        nguoi_dung = Customer.objects.filter(email=email, mat_khau=encoded)
        if nguoi_dung.count() > 0:
            request.session['sessionNguoiDung'] = nguoi_dung.values()[0]
            return redirect('Do_an_01:index')
        else:
            result_login = '''
                <div class="alert alert-danger alert-dismissible fade show" role="alert">
                    Đăng nhập thất bại.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                '''
    return render(request, 'Do_an_01/login.html', {
        'form': form,
        'result_regiter': result_regiter,
        'list_category': list_category,
        'story_newest_3': story_newest_3,
        'result_login': result_login,
    })


def my_account(request):
    update_msg = ''
    doimk_msg = ''
    # Kiểm tra trạng thái đăng nhập của người dùng
    session_status = check_session(request, 'sessionNguoiDung')
    session_info = ''
    if session_status:
        session_info = request.session.get('sessionNguoiDung')
    else:
        return redirect('customers_hdg:login')

    customer = Customer.objects.get(id=request.session['sessionNguoiDung']['id'])
    form = FormThongTin(instance=customer)
    form_mk = FormDoiMatKhau()
    if request.POST.get('btnCapNhat'):
        form = FormThongTin(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            update_msg = '''
                <div class="alert alert-success alert-dismissible fade show" id="myAlert" role="alert">
                    Cập nhật thông tin thành công.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            '''
    if request.POST.get('btnMk'):
        form_mk = FormDoiMatKhau(request.POST)
        if form_mk.is_valid():
            hasher = PBKDF2PasswordHasher()
            mat_khau = hasher.encode(form_mk.cleaned_data['mat_khau'], '123')
            if mat_khau == request.session['sessionNguoiDung']['mat_khau']:
                if form_mk.cleaned_data['mat_khau_moi'] == form_mk.cleaned_data['xac_nhan_mat_khau']:
                    nguoi_dung = Customer.objects.get(email=request.session['sessionNguoiDung']['email'])

                    nguoi_dung.mat_khau = hasher.encode(form_mk.cleaned_data['mat_khau_moi'], '123')
                    nguoi_dung.save()
                    nguoi_dung_dict = nguoi_dung.__dict__
                    del(nguoi_dung_dict['_state'])
                    request.session['sessionNguoiDung'] = nguoi_dung_dict
                    doimk_msg = '''
                        <div class="alert alert-success alert-dismissible fade show" id="myAlert" role="alert">
                            Đổi mật khẩu thành công.
                            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                    '''

    return render(request, 'Do_an_01/my_account.html', {
        'form': form,
        'form_mk': form_mk,
        'update_msg': update_msg,
        'doimk_msg': doimk_msg,
        'customer': customer,
        'list_category': list_category,
        'story_newest_3': story_newest_3,
        'session_info': session_info,
        'session_status': session_status,
    })

def logout(request):
    if request.session.get('sessionNguoiDung'):
        del request.session['sessionNguoiDung']
    return redirect('customers_hdg:login')

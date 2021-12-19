from django.shortcuts import render, redirect
from Do_an_01.models import Category, Story, Book
import re
from Do_an_01.forms import FormContact
from Do_an_01.my_module import *

from Do_an_ck_01.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage

# API
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from Do_an_01.serializers import StorySerializer

# Phân trang
from django.core.paginator import Paginator


def Masterbase(request):
    return render(request, 'Do_an_01/Masterbase.html', {
        'story_newest_3': story_newest_3,
    })


# Biến toàn cục
story_list = Story.objects.order_by('-public_day')

# Thể loại
list_category = Category.objects.all()

# Slide
story_newest_14 = story_list[0:6]

# Lọc hiển thị nội dung footer
story_newest_3 = story_list[0:5]

# Sách
sach_hay = Book.objects.filter(category=9).order_by('-public_day')[0:10]

# Tin tức
tin_tuc = Story.objects.filter(category=3).order_by('-public_day')[0:7]


def index(request):
    # Kiểm tra trạng thái đăng nhập của người dùng
    session_status = check_session(request, 'sessionNguoiDung')
    session_info = ''
    if session_status:
        session_info = request.session.get('sessionNguoiDung')
    story_newest_1 = story_list[0]
    story_newest_4 = story_list[1:5]
    # Nhà đất bán
    nha_dat_ban = Story.objects.filter(category=1).order_by('-public_day')[0:6]
    # Nhà đất thuê
    nha_dat_thue = Story.objects.filter(category=2).order_by('-public_day')[0:7]
    return render(request, 'Do_an_01/index.html', {
        'story_newest_1': story_newest_1,
        'story_newest_4': story_newest_4,
        'story_newest_14': story_newest_14,
        'nha_dat_ban': nha_dat_ban,
        'nha_dat_thue': nha_dat_thue,
        'tin_tuc': tin_tuc,
        'list_category': list_category,
        'story_newest_3': story_newest_3,
        'session_status': session_status,
        'session_info': session_info,
        'sach_hay': sach_hay,
    })


def category(request, pk):
    # Kiểm tra trạng thái đăng nhập của người dùng
    session_status = check_session(request, 'sessionNguoiDung')
    session_info = ''
    if session_status:
        session_info = request.session.get('sessionNguoiDung')

    # Phân trang Story
    story_list = Story.objects.filter(category=pk).order_by('-public_day')
    paginator = Paginator(story_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Phân trang Book
    book_list = Book.objects.filter(category=pk).order_by('-public_day')
    paginator = Paginator(book_list, 6)
    page_number = request.GET.get('page')
    page_obj_book = paginator.get_page(page_number)

    category_name = Category.objects.get(pk=pk)
    return render(request, 'Do_an_01/category.html', {
        'story_list': story_list,
        'category_name': category_name,
        'list_category': list_category,
        'page_obj': page_obj,
        'story_newest_3': story_newest_3,
        'session_status': session_status,
        'session_info': session_info,
        'tin_tuc': tin_tuc,
        'page_obj_book': page_obj_book,

    })


def contact_hdg(request):
    # Kiểm tra trạng thái đăng nhập của người dùng
    session_status = check_session(request, 'sessionNguoiDung')
    session_info = ''
    if session_status:
        session_info = request.session.get('sessionNguoiDung')
    else:
        return redirect('customers_hdg:login')
    # Liên hệ
    form = FormContact()
    result_contact = ''
    if request.POST.get('btnSendContact'):
        form = FormContact(request.POST)
        if form.is_valid():
            request.POST._mutable = True
            post = form.save(commit=False)
            post.name = form.cleaned_data['name']
            post.email = form.cleaned_data['email']
            post.subject = form.cleaned_data['subject']
            post.message = form.cleaned_data['message']
            post.save()
            # Gửi mail
            content = '<p>Chào bạn <b>' + post.name + '</b></p>'
            content += '<p>Chúng tôi đã nhận được thông tin của bạn thông quan Website Phú yên News với nội dung như sau:</p>'
            content += '<p>' + post.message + '</p>'
            content += '<p>Chúng tôi sẽ liên hệ bạn trong thời gian sớm nhất.</p>'
            content += '<p>Trân trọng.</p>'
            # Không có html
            # send_mail(subject, content, EMAIL_HOST_USER, [email])
            # Có định dạng html
            msg = EmailMessage(post.subject, content, EMAIL_HOST_USER, [post.email])
            msg.content_subtype = 'html'
            msg.send()
            result_contact = '''
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    Gửi thông tin thành công. Cảm ơn bạn đã liên hệ. Chúng tôi sẽ phản hồi trong thời gian sớm nhất.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                '''
        else:
            result_contact = '''
                <div class="alert alert-danger alert-dismissible fade show" role="alert">
                    Gửi thông tin thất bại.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                '''
    return render(request, 'Do_an_01/contact_hdg.html', {
        'result_contact': result_contact,
        'form': form,
        'list_category': list_category,
        'story_newest_3': story_newest_3,
        'session_status': session_status,
        'session_info': session_info,
    })


def single(request, pk):
    # Kiểm tra trạng thái đăng nhập của người dùng
    session_status = check_session(request, 'sessionNguoiDung')
    session_info = ''
    if session_status:
        session_info = request.session.get('sessionNguoiDung')
    story = Story.objects.get(pk=pk)
    return render(request, 'Do_an_01/single.html', {
        'story': story,
        'story_newest_3': story_newest_3,
        'list_category': list_category,
        'session_status': session_status,
        'session_info': session_info,
        'tin_tuc': tin_tuc,
    })


def book(request, pk):
    # Kiểm tra trạng thái đăng nhập của người dùng
    session_status = check_session(request, 'sessionNguoiDung')
    session_info = ''
    if session_status:
        session_info = request.session.get('sessionNguoiDung')
    book = Book.objects.get(pk=pk)
    return render(request, 'Do_an_01/book.html', {
        'book': book,
        'story_newest_3': story_newest_3,
        'list_category': list_category,
        'session_status': session_status,
        'session_info': session_info,
        'sach_hay': sach_hay,
    })


def search(request):
    # Kiểm tra trạng thái đăng nhập của người dùng
    session_status = check_session(request, 'sessionNguoiDung')
    session_info = ''
    if session_status:
        session_info = request.session.get('sessionNguoiDung')
    # Tìm theo Story
    story_list = []
    book_list = []
    tu_khoa = ''
    if request.GET.get('keyword'):
        # Gán biến
        tu_khoa = request.GET.get('keyword')

        # Lọc theo từ khóa và xử lý loại bỏ html
        Do_an_01 = Story.objects.all().values()
        Do_an_02 = Book.objects.all().values()
        lst_story = list(Do_an_01)
        lst_book = list(Do_an_02)
        id_list = []
        id_book= []
        for story in lst_story:
            story['content'] = re.sub('<[^<]+?>', '', story['content'])
            if tu_khoa.lower() in story['name'].lower() or tu_khoa.lower() in story['content'].lower():
                id_list.append(story['id'])

        for book in lst_book:
            book['content'] = re.sub('<[^<]+?>', '', book['content'])
            if tu_khoa.lower() in book['name'].lower() or tu_khoa.lower() in book['content'].lower():
                id_book.append(book['id'])

        # Lọc Do_an_01 theo danh sách id đã tìm.
        story_list = Story.objects.filter(id__in=id_list).order_by('-public_day')
        book_list = Book.objects.filter(id__in=id_book).order_by('-public_day')

    # Phân trang Story
    paginator = Paginator(story_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Phân trang Book
    paginator = Paginator(book_list, 6)
    page_number = request.GET.get('page')
    page_obj_book = paginator.get_page(page_number)
    return render(request, 'Do_an_01/search.html', {
        'story_list': story_list,
        'book_list': book_list,
        'keyword': tu_khoa,
        'list_category': list_category,
        'story_newest_14': story_newest_14,
        'page_obj': page_obj,
        'page_obj_book': page_obj_book,
        'session_info': session_info,
        'session_status': session_status,
    })

def storys_service(request):
    products = Story.objects.order_by('-public_day')
    result_list = list(products.values())
    return JsonResponse(result_list, safe=False)

def story_service(request, pk):
    story = Story.objects.filter(id=pk)
    result = list(story.values())[0]
    return JsonResponse(result, safe=False)


class StorytViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('-public_day')
    serializer_class = StorySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Chỉ đọc
    permission_classes = [permissions.IsAdminUser]  # Đọc / Ghi

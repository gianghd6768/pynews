from django.contrib import admin
from Do_an_01.models import Story, Subcribe, Contact, Category, Book
from customers_hdg.models import Customer

#
from datetime import datetime
from django.utils.html import format_html
#
# Biến toàn cục
story_list = Story.objects.order_by('-public_day')

# Thay đổi tiêu đề Admin
admin.site.site_header = 'Quản trị'


def change_public_day(queryset):
    queryset.update(public_day=datetime.now())


change_public_day.short_description = 'Change public_day to Today'


class StoryAmin(admin.ModelAdmin):
    exclude = ('viewed',)
    # Phân trang trong admin
    list_per_page = 15

    # Hiển thị các field trong danh sách
    list_display = ('e_id', 'e_name', 'e_image', 'e_public_day')

    # Lọc theo field
    list_filter = ('public_day',)

    # Tìm theo field
    search_fields = ('name',)

    actions = [change_public_day]

    def e_id(self, obj):
        return "%s" % obj.id
    e_id.short_description = "STT"

    def e_name(self, obj):
        return "%s" % obj.name
    e_name.short_description = "Tiêu đề"

    def e_image(self, obj):
        return format_html('<img src="%s" style="width: 45px; height: 45px">' % obj.image.url)
    e_image.short_description = "Hình ảnh"

    def e_public_day(self, obj):
        return "%s" % obj.public_day
    e_public_day.short_description = "Ngày xuất bản"

class CategoryAmin(admin.ModelAdmin):
    # Phân trang trong admin
    list_per_page = 10

    # Tìm theo field
    search_fields = ('name',)

    actions = [change_public_day]

    # Hiển thị các field trong danh sách
    list_display = ('e_id', 'e_name')

    def e_id(self, obj):
        return "%s" % obj.id
    e_id.short_description = "STT"

    def e_name(self, obj):
        return "%s" % obj.name
    e_name.short_description = "Loại tin tức"

# class ContactAmin(admin.ModelAdmin):
#     # Hiển thị các field trong danh sách
#     list_display = ('e_id', 'e_name', 'e_email')
#
#     # Phân trang trong admin
#     list_per_page = 15
#
#     # Tìm theo field
#     search_fields = ('name',)
#
#     actions = [change_public_day]
#
#     @admin.display(description='STT')
#     def e_id(self, obj):
#         return '%s' % obj.id
#
#     @admin.display(description='Họ tên')
#     def e_name(self, obj):
#         return '%s' % obj.name
#
#     @admin.display(description='Email')
#     def e_email(self, obj):
#         return '%s' % obj.email
#
#
# class CustomerAmin(admin.ModelAdmin):
#     # Hiển thị các field trong danh sách
#     list_display = ('e_id', 'e_ho', 'e_ten', 'e_email', 'e_mat_khau', 'e_dien_thoai', 'e_dia_chi')
#
#     # Tìm theo field
#     search_fields = ('name',)
#
#     actions = [change_public_day]
#
#     @admin.display(description='STT')
#     def e_id(self, obj):
#         return '%s' % obj.id
#
#     @admin.display(description='Họ')
#     def e_ho(self, obj):
#         return '%s' % obj.ho
#
#     @admin.display(description='Tên')
#     def e_ten(self, obj):
#         return '%s' % obj.ten
#
#     @admin.display(description='Email')
#     def e_email(self, obj):
#         return '%s' % obj.email
#
#     @admin.display(description='Mật Khẩu')
#     def e_mat_khau(self, obj):
#         return '%s' % obj.mat_khau
#
#     @admin.display(description='Điện thoại')
#     def e_dien_thoai(self, obj):
#         return '%s' % obj.dien_thoai
#
#     @admin.display(description='Địa chỉ')
#     def e_dia_chi(self, obj):
#         return '%s' % obj.dia_chi
#
#
class BookAmin(admin.ModelAdmin):
    exclude = ('viewed',)
    # Phân trang trong admin
    list_per_page = 15

    # Hiển thị các field trong danh sách
    list_display = ('e_id', 'e_name', 'e_image', 'e_public_day')

    # Lọc theo field
    list_filter = ('public_day',)

    # Tìm theo field
    search_fields = ('name',)

    actions = [change_public_day]


    def e_id(self, obj):
        return "%s" % obj.id
    e_id.short_description = "STT"


    def e_name(self, obj):
        return "%s" % obj.name
    e_name.short_description = "Tên sách"


    def e_image(self, obj):
        return format_html('<img src="%s" style="width: 45px; height: 45px">' % obj.image.url)
    e_image.short_description = "Hình ảnh"


    def e_public_day(self, obj):
        return "%s" % obj.public_day
    e_public_day.short_description = "Ngày xuất bản"

admin.site.register(Category, CategoryAmin)
admin.site.register(Story, StoryAmin)
admin.site.register(Book, BookAmin)
# admin.site.register(Contact, ContactAmin)
# admin.site.register(Subcribe)
# admin.site.register(Customer, CustomerAmin)

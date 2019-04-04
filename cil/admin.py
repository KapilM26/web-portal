from os import remove, rename,getcwd,mkdir
from os.path import join,isfile,exists
from django.contrib import admin
from django.conf import settings
from django.utils.html import format_html
from django.urls import path
from django.urls import reverse
from django.shortcuts import redirect
from .models import Profile, TempProfileAdd, TempProfileEdit, TempProfileDelete, Log


# Register your models here.
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'department',
        'time'
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'domain',
        'designation',
        'exp',
        'phone',
        'biodata'
    )

#    def biodata_url(self,obj):
#        return format_html('<a href={}>Biodata</a>',join(settings.MEDIA_URL, obj.biodata.url))


@admin.register(TempProfileAdd)
class TempProfileAddAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'domain',
        'designation',
        'exp',
        'phone',
        'biodata',
        'approve_or_discard'
    )

#    def biodata_url(self,obj):
#        path=join(settings.MEDIA_URL,obj.biodata.url)
#        return format_html('<a href={}>Biodata</a>',path)

    def approve_or_discard(self, obj):
        return format_html(
            '<a class="button" href="{}">Approve</a>&nbsp;<a class="button" href="{}">Discard</a>',
            reverse('admin:profile-approve-add', args=[obj.pk]),
            reverse('admin:profile-delete-add', args=[obj.pk], )

        )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:pro>/approveadd', self.admin_site.admin_view(self.process_approve),
                name='profile-approve-add',
            ),
            path(
                '?<int:pro>/deleteadd/', self.admin_site.admin_view(self.process_delete),
                name='profile-delete-add',
            ),
        ]
        return custom_urls + urls

    def process_approve(self, request, pro):
        new = Profile()
        temp = TempProfileAdd.objects.get(pk=pro)
        new.create(name=temp.name, exp=temp.exp, domain=temp.domain,
                   phone=temp.phone, email=temp.email, designation=temp.designation)
        new.biodata = temp.biodata
        new.save()
        temp.delete()

        #shift temp file to profile
        #name_split = temp.biodata.url.rsplit('/',1)[1]
        #name_split = name_split.split('.')
        #old_path='TempAdd/'+str(temp.id)+'.'+name_split[1]
        #new_path='Profile/'+str(new.id)+'.'+name_split[1]
        #root=settings.MEDIA_ROOT
        #try:
        #    mkdir(root+'\\Profile')
        #except FileExistsError:
        #    pass
        #rename(join(root,old_path),join(root,new_path))

        #new.file_url=new_path
        #new.save()
        #temp.delete()
        return redirect('admin:cil_tempprofileadd_changelist')

    def process_delete(self, request, pro):
        temp = TempProfileAdd.objects.get(pk=pro)
        #path=temp.file_url.replace('/','\\')
        #delete file uploaded by user
        #remove(join(settings.MEDIA_ROOT, path))
        temp.delete()
        return redirect('admin:cil_tempprofileadd_changelist')


@admin.register(TempProfileEdit)
class TempProfileEditAdmin(admin.ModelAdmin):
    list_display = (
        'old_name',
        'old_email',
        'old_domain',
        'old_exp',
        'old_phone',
        'old_biodata',
        'name',
        'email',
        'domain',
        'designation',
        'exp',
        'phone',
        'biodata',
        'approve_or_discard'
    )

    #def biodata_url(self,obj):
    #    return format_html('<a href={}>Biodata</a>',join(settings.MEDIA_URL, biodata.url))

    def approve_or_discard(self, obj):
        return format_html(
            '<a class="button" href="{}">Approve</a>&nbsp;<a class="button" href="{}">Discard</a>',
            reverse('admin:profile-approve-edit', args=[obj.pk]),
            reverse('admin:profile-delete-edit', args=[obj.pk], )

        )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:pro>/approveedit/', self.admin_site.admin_view(self.process_approve),
                name='profile-approve-edit',
            ),
            path(
                '?<int:pro>/deleteedit/', self.admin_site.admin_view(self.process_delete),
                name='profile-delete-edit',
            ),
        ]
        return custom_urls + urls

    def process_approve(self, request, pro):
        temp = TempProfileEdit.objects.get(pk=pro)
        edit = Profile.objects.get(pk=temp.profile.pk)
        edit.name = temp.name
        edit.domain = temp.domain
        edit.designation = temp.designation
        edit.email = temp.email
        edit.phone = temp.phone
        edit.exp = temp.exp
        try:
            path = edit.biodata.url[1:]
            remove(join(settings.BASE_DIR, path))
        except (FileNotFoundError, ValueError) as e:
            pass
        edit.biodata = temp.biodata
        edit.save()
        temp.delete()
        return redirect('admin:cil_tempprofileedit_changelist')

    def process_delete(self, request, pro):
        temp = TempProfileEdit.objects.get(pk=pro)
        #prof = Profile.objects.get(pk=temp.profile.pk)
        #delete file uploaded by user
        try:
            path = temp.biodata.url[1:]
            remove(join(settings.BASE_DIR, path))
        except (FileNotFoundError, ValueError) as e:
            pass
        temp.delete()
        return redirect('admin:cil_tempprofileedit_changelist')

    def old_name(self, obj):
        return obj.profile.name

    def old_domain(self, obj):
        return obj.profile.domain

    def old_email(self, obj):
        return obj.profile.email

    def old_exp(self, obj):
        return obj.profile.exp

    def old_phone(self, obj):
        return obj.profile.phone

    def old_biodata(self, obj):
        if obj.profile.biodata:
            return format_html('<a href={}>Biodata</a>', join(settings.MEDIA_URL, obj.profile.biodata.url))
        return None

@admin.register(TempProfileDelete)
class TempProfileDeleteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'domain',
        'designation',
        'exp',
        'phone',
        'biodata',
        'approve_or_discard'
    )

#    def biodata_url(self,obj):
#        return format_html('<a href={}>Biodata</a>',join(settings.MEDIA_URL, obj.profile.biodata.url))

    def approve_or_discard(self, obj):
        return format_html(
            '<a class="button" href="{}">Approve</a>&nbsp;<a class="button" href="{}">Discard</a>',
            reverse('admin:profile-approve-del', args=[obj.pk]),
            reverse('admin:profile-delete-del', args=[obj.pk], )

        )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:pro>/approvedel', self.admin_site.admin_view(self.process_approve),
                name='profile-approve-del',
            ),
            path(
                '?<int:pro>/deletedel/', self.admin_site.admin_view(self.process_delete),
                name='profile-delete-del',
            ),
        ]
        return custom_urls + urls

    def process_approve(self, request, pro):
        temp = TempProfileDelete.objects.get(pk=pro)
        delet = Profile.objects.get(pk=temp.profile.pk)
        try:
            path = delet.biodata.url[1:]
            remove(join(settings.BASE_DIR, path))
        except (FileNotFoundError, ValueError) as e:
            pass
        delet.delete()
        return redirect('admin:cil_tempprofiledelete_changelist')

    def process_delete(self, request, pro):
        temp = TempProfileDelete.objects.get(pk=pro)
        temp.delete()
        return redirect('admin:cil_tempprofiledelete_changelist')

    def name(self, obj):
        return obj.profile.name

    def domain(self, obj):
        return obj.profile.domain

    def email(self, obj):
        return obj.profile.email

    def exp(self, obj):
        return obj.profile.exp

    def phone(self, obj):
        return obj.profile.phone

    def designation(self, obj):
        return obj.profile.designation

    def biodata(self, obj):
        if obj.profile.biodata:
            return format_html('<a href={}>Biodata</a>',join(settings.MEDIA_URL, obj.profile.biodata.url))
        return None
from django.core.management.base import BaseCommand, CommandError
from cil.models import Profile
import pandas as pd


class Command(BaseCommand):
    help = "Transfer list to database."

    def handle(self, *args, **options):
        data = pd.read_excel('/home/kapil/list.xlsx')
        tempdomain = data['Domain']
        name = data['Name']
        email = data['Email id']
        phone = data['Phone']
        domain2 = [str(dom).replace('and', ',') for dom in tempdomain]
        domain = [str(dom).replace('/', ',') for dom in domain2]
        index = 0
        for n in name:
            if ',' in domain[index]:
                domain_ls = domain[index].split(',')
                for i in range(len(domain_ls)):
                    domain_add = domain_ls[i].strip()
                    domain_add = domain_add.upper()
                    try:
                        obj = Profile(name=name[index], email=email[index], phone=phone[index],domain=domain_add)
                        obj.save()
                    except:
                        pass
            else:
                try:
                    obj = Profile(name=name[index], email=email[index], phone=phone[index],domain=domain_add)
                    obj.save()
                except:
                    pass
            index += 1

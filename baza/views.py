from unicodedata import name
from django.shortcuts import render


# from .forms import TableForm
from .models import Detail
import re




class Parse:
    def __init__(self):
        self.list_parse = [self.gost_22002_1_82, self.gost_22002_2_76, self.gost_22002_3_76, self.gost_22002_4_76,
                           self.gost_22002_5_76, self.gost_22002_6_82, self.gost_22002_7_76, self.gost_22002_8_76,
                           self.gost_22002_9_76, self.gost_22002_10_76, self.gost_22002_11_76, self.gost_22002_12_76,]
        self.answer_construct = {'name': '', 'cover': False, 'cost_result_in_cover':'','cost_result_without_cover':'', 'request':''}

    def search(self, text):
        text = text.strip()
        if text:
            for func in self.list_parse:
                answer_func = func(text)
                if answer_func['name']:
                    return answer_func
                else:
                    continue
        return self.answer_construct

    def gost_22002_1_82(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.1-82'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[0-9]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.1\-82)+"  # 2
        cover = False
        if not re.search(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[0-9]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        text = re.search(pattern_request, text)[0]
        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()

        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_2_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.2-76'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[0-9]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.2\-76)+"  # 2
        cover = False
        if not re.search(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[0-9]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        text = re.search(pattern_request, text)[0]
        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_3_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.3-76'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[0-9]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.3\-76)+"  # 2
        cover = False
        if not re.search(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[0-9]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        text = re.search(pattern_request, text)[0]
        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_4_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.4-76'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[0-9]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.4\-76)+"  # 2
        cover = False
        if not re.search(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[0-9]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        text = re.search(pattern_request, text)[0]
        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_5_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.5-76'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-(К|Д)+[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.5\-76)+"  # 2
        cover = False
        if not re.search(pattern_request, text):
            return self.answer_construct
        pattern_mark = r"[0-9\,\.]+\-[К|Д]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        text = re.search(pattern_request, text)[0]
        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_6_82(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.6-82'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-(К|Д)+[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.5\-76)+"  # 2
        cover = False
        if not re.search(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[К|Д]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        text = re.search(pattern_request, text)[0]
        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_7_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.7-76'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[0-9]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.7\-76)+"  # 2
        cover = False
        if not re.search(pattern_request, text):
            return self.answer_construct
        pattern_mark = r"[0-9\,\.]+\-[0-9]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        text = re.search(pattern_request, text)[0]
        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_8_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.8-76'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[0-9]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.8\-76)+"  # 2
        cover = False
        if not re.search(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[0-9]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        text = re.search(pattern_request, text)[0]
        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''

        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3

        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_9_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.9-76'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[0-9]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.9\-76)+"  # 2
        cover = False
        if not re.findall(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[0-9]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_10_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.1-82'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[0-9]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.10\-76)+"  # 2
        cover = False
        if not re.findall(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[0-9]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_11_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.11-76'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[0-9]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.11\-76)+"  # 2
        cover = False
        if not re.findall(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[0-9]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_12_76(self, text):
        request=text
        text=text.upper()
        gost = 'ГОСТ 22002.12-76'  # 1
        pattern_request = \
            r"[0-9\,\.]+\-[А-я\-]*(ЛТ|М)+[\-]*[0-9]*.*(ГОСТ)+.*(22002\.12\-76)+"  # 2
        cover = False
        if not re.findall(pattern_request, text):
            return self.answer_construct

        pattern_mark = r"[0-9\,\.]+\-[К|Д]+\-"
        pattern_material = r"(ЛТ|М)+"
        pattern_cover = r"(ЛТ|М)+(\-[0-9]+)+"
        pattern_zero = r"([\,\.]+(0)+)+\-"
        pattern_point = r"\,"

        mark_temp = re.sub(pattern_zero, '-', re.findall(pattern_mark, text)[-1])
        mark_temp = re.sub(pattern_point, '.', mark_temp)
        material_temp = re.findall(pattern_material, text)[0]
        have_cover = re.findall(pattern_cover, text)

        if have_cover and have_cover[-1][-1] != '-00':
            cover_temp = have_cover[-1][-1]
            cover = True
        else:
            cover_temp = ''
        answer = self.answer_construct.copy()
        full_name = f'{"Наконечник"} {mark_temp}{material_temp} {gost}'  # 3
        answer['name'] = full_name
        answer['cover'] = cover
        answer['request'] = request
        return answer

    def gost_22002_13_76(self, text):
        return self.answer_construct

    
def index(request):
    return render(request, 'baza/base.html')

def get_list(request_text_area):
    search_query = request_text_area.GET.get('search',)
    details = []
    if search_query:
        positions = search_query.split('\r\n')
        parse = Parse()
        for pos in positions:
            request = parse.search(pos.strip())
            try:
                detail = Detail.objects.get(name=request['name'])
            except:
                continue
            if request['name']:
                if request['cover']:
                    detail.cost = detail.cost_result_in_cover
                else:
                    detail.cost = detail.cost_result_without_cover
                detail.name=request['request']
                details.append(detail)

    return render(request_text_area, 'baza/search_results.html', {'details': details})
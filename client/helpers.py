from api.views import *


TYPE_CHOICES = {
    'D': 'Drink',
    'F': 'Food'
}
  
def render_items(items_response, sections_response):
    try:
        items = items_response.data
        sections = sections_response.data
        for i in range(len(items)):
            item = items[i]
            section_idx = [idx for idx in range(len(sections)) if sections[idx]['id'] == item['type']][0]
            if 'data' not in sections[section_idx]:
                sections[section_idx]['data'] = [item]
            else:
                sections[section_idx]['data'].append(item)
        return sections         
    except Exception as e:
        return None
    
def render_sections(sections):
    output = {
        TYPE_CHOICES['D']: [],
        TYPE_CHOICES['F']: []
    }
    
    try:
        for i in range(len(sections)):
            if sections[i]['type'] == 'D':
                output[TYPE_CHOICES['D']].append(sections[i])
            else:
                output[TYPE_CHOICES['F']].append(sections[i])
        return output
    except Exception as e:
        return None

def menu_data(request):
    try:
        items_response = items_view(request)
        sections_response = sections_view(request)
        items_by_sections = render_items(items_response, sections_response)
        sections_types = render_sections(items_by_sections)
        return sections_types
    except Exception as e:
        return None
    
def events_data(request):
    try:
        events_response = events_view(request)
        return events_response.data
    except Exception as e:
        return None
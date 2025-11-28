import sys
import json
import re
from tinydb import TinyDB, Query

db = TinyDB('templates_data.json', encoding='utf-8')
templates = db.table('_default')

def run():
    if len(sys.argv) < 2 or sys.argv[1] != 'find':
        print("Usage: python processor.py find --field=value --field2=value2")
        return

    fields = {}
    for arg in sys.argv[2:]:
        if arg.startswith('--') and '=' in arg:
            key, val = arg[2:].split('=', 1)
            fields[key] = val

    if not fields:
        print("Error: no fields provided")
        return

    field_types = {k: detect_field_type(v) for k, v in fields.items()}
    best_match = None
    top_score = 0
    
    for template in templates.all():
        template_title = template['title']
        template_spec = {k: v for k, v in template.items() if k != 'title'}
        
        matches = sum(
            1 for field, f_type in template_spec.items()
            if field in field_types and field_types[field] == f_type
        )
        
        if matches == len(template_spec):
            print(json.dumps({"template": template_title}, indent=2, ensure_ascii=False))
            return
        
        if matches > top_score:
            top_score = matches
            best_match = template_title

    if best_match and top_score > 0:
        print(json.dumps({"template": best_match}, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"field_types": field_types}, indent=2, ensure_ascii=False))

def detect_field_type(value):
    if not isinstance(value, str):
        return 'string'
    
    if re.fullmatch(r'^[\w.+-]+@[\w-]+\.[\w.-]+$', value):
        return 'email'
    
    if re.fullmatch(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
        return 'phone'
    
    if (re.fullmatch(r'^\d{2}/\d{2}/\d{4}$', value) or 
        re.fullmatch(r'^\d{4}-\d{2}-\d{2}$', value)):
        return 'date'
    
    return 'string'

if __name__ == "__main__":
    run()

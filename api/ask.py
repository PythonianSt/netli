import json
from fuzzywuzzy import fuzz
from flask import jsonify

# Load FAQ data
with open('faq.json', 'r', encoding='utf-8') as f:
    faq_data = json.load(f)

def handler(request):
    data = request.json
    question = data.get('question', '')

    # Find best match
    best_score = 0
    best_answer = "ขออภัย ไม่พบคำตอบที่ตรงกับคำถามของคุณ"

    for q, a in faq_data.items():
        score = fuzz.token_set_ratio(question, q)
        if score > best_score:
            best_score = score
            best_answer = a

    return jsonify({'answer': best_answer})

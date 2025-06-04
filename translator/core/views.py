from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import MarianMTModel, MarianTokenizer

# Cache models for reuse
loaded_models = {}

def get_model(src_lang, tgt_lang):
    lang_code_map = {
        ('en', 'hi'): 'Helsinki-NLP/opus-mt-en-hi',
        ('en', 'ru'): 'Helsinki-NLP/opus-mt-en-ru',
        ('en', 'de'): 'Helsinki-NLP/opus-mt-en-de',
        ('en', 'fr'): 'Helsinki-NLP/opus-mt-en-fr',
        ('en', 'es'): 'Helsinki-NLP/opus-mt-en-es',
        ('en', 'it'): 'Helsinki-NLP/opus-mt-en-it',
        ('hi', 'en'): 'Helsinki-NLP/opus-mt-hi-en',
        ('ru', 'en'): 'Helsinki-NLP/opus-mt-ru-en',
        ('ru', 'fr'): 'Helsinki-NLP/opus-mt-ru-fr',
        ('ru', 'es'): 'Helsinki-NLP/opus-mt-ru-es',
        ('de', 'en'): 'Helsinki-NLP/opus-mt-de-en',
        ('de', 'fr'): 'Helsinki-NLP/opus-mt-de-fr',
        ('de', 'es'): 'Helsinki-NLP/opus-mt-de-es',
        ('de', 'it'): 'Helsinki-NLP/opus-mt-de-it',
        ('fr', 'en'): 'Helsinki-NLP/opus-mt-fr-en',
        ('fr', 'de'): 'Helsinki-NLP/opus-mt-fr-de',
        ('fr', 'ru'): 'Helsinki-NLP/opus-mt-fr-ru',
        ('fr', 'es'): 'Helsinki-NLP/opus-mt-fr-es',
        ('es', 'en'): 'Helsinki-NLP/opus-mt-es-en',
        ('es', 'ru'): 'Helsinki-NLP/opus-mt-es-ru',
        ('es', 'fr'): 'Helsinki-NLP/opus-mt-es-fr',
        ('es', 'de'): 'Helsinki-NLP/opus-mt-es-de',
        ('es', 'it'): 'Helsinki-NLP/opus-mt-es-it',
        ('it', 'en'): 'Helsinki-NLP/opus-mt-it-en',
        ('it', 'de'): 'Helsinki-NLP/opus-mt-it-de',
        ('it', 'fr'): 'Helsinki-NLP/opus-mt-it-fr',
        ('it', 'es'): 'Helsinki-NLP/opus-mt-it-es',
        # Add more pairs as needed
    }

    key = (src_lang, tgt_lang)
    if key not in lang_code_map:
        return None, None

    model_name = lang_code_map[key]
    if model_name not in loaded_models:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        loaded_models[model_name] = (tokenizer, model)

    return loaded_models[model_name]

@csrf_exempt
def translate(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get("text")
        src = data.get("src")
        tgt = data.get("tgt")

        tokenizer, model = get_model(src, tgt)
        if not tokenizer:
            return JsonResponse({"error": "Language pair not supported"}, status=400)

        input_tokens = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt", truncation=True)
        translated_tokens = model.generate(**input_tokens)
        translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

        return JsonResponse({"translated_text": translated_text})

    return JsonResponse({"error": "POST request required"}, status=400)

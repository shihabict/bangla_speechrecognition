import googletrans

# text = "মেদহীন ঝরঝরে মাশরাফী, ফিরলেন অনুশীলনে; তারুণ্যের রহস্য কী"
text = "মেহেদির ঝরঝরে শরীর মাশরাফি ফিরেছেন অনুশীলনী তারুণ্যের রহস্য কি"
from googletrans import Translator

translator = Translator()

trans_to_eng = translator.translate(text,src='bn',dest='en')
print(trans_to_eng.text)
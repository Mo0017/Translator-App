import speech_recognition as sr
from translate import Translator
import PySimpleGUI as sg

# List of languages supported
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}

sg.theme('DarkTeal6')
# Define the layout of the UI
gui = [
    [sg.Text("Welcome to my translator app!")],
    [sg.Text("Choose Language"),sg.Combo(list(LANGUAGES.values()), key='language')],
    [sg.Text("Say something!"), sg.Button('Record', key='record')],
    [sg.Multiline(size=(50, 5), key='original')],
    [sg.Multiline(size=(50, 5), key='translation')],
    [sg.Button('Translate', key='translate', disabled=True)]
]

# Create the window 
win = sg.Window('Speech Translator', gui, resizable=True, element_justification='c')

# Event loop
while True:
    event, values = win.read()

    # If the user closes the window or clicks on the exit button, break the loop
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # If the user clicks on the recrod button, prompt for speech input
    if event == 'record':
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            win['original'].update('Say something!')
            audio = recognizer.listen(source)

        try:
            original = recognizer.recognize_google(audio)
            win['original'].update(original)
            win['translate'].update(disabled=False)

        except sr.UnknownValueError:
            win['original'].update('Sorry, I didnt catch that. Please try again.')
            win['translate'].update(disabled=True)

    # If the user clicks on the Translate button, translate the speech input
    if event == 'translate':
        original_text = values['original']
        language_name = values['language']
        language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(language_name)]
        translator = Translator(to_lang = language_code)
        translation = translator.translate(original_text)
        win['translation'].update(translation)


win.close()

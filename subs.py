def import_or_install(package):
    try:
        __import__(package)
        
    except ImportError:
    	#print("[WAIT FOR REQUIRED LIBRARY INSTALLATION]")
        main(['install', '-I', '-q', '--user', package])
        import_or_install(package)

list_lang='afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu', 'Filipino', 'Hebrew'

if __name__ == "__main__" :

    from pip import main
    from sys import exit
    from requests import get

    try:
        if get('https://www.google.com').ok:
            print("[CONNECTION OK]")
            print("###############################################")
    except:
        exit("[YOU NEED A PROPER INTERNET CONNECTION]")

    for i in 'pysubs2','googletrans':
        import_or_install(i)

    from pysubs2 import load
    from googletrans import Translator

    filename=input("enterthe FULL PATH an FILE of the sub:")
    print("###############################################")

    loadedsub = load(filename, encoding="utf-8")

    print(list_lang)
    print("###############################################")
    lan=input("which language do you want to translate(select from list):")
    print("###############################################")
    
    count=1
    for line in loadedsub:
        print(count)
        print(line.text)
        translations = Translator().translate(line.text, dest=lan)
        line.text=translations.text
        print(line.text)
        print("")
        count+=1
    gg=filename+'_edited'
    loadedsub.save(gg+".srt")

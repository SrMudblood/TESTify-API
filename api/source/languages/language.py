import random

class Language:
    def __init__(self) -> None:
        self.languages = [
        "English", "Mandarin Chinese", "Spanish", "Hindi", "French", "Standard Arabic", "Bengali", "Russian",
        "Portuguese", "Indonesian", "Urdu", "German", "Japanese", "Swahili", "Marathi", "Telugu",
        "Turkish", "Korean", "Tamil", "Vietnamese", "Yue Chinese", "Javanese", "Italian", "Thai",
        "Gujarati", "Jin Chinese", "Southern Min", "Persian", "Polish", "Pashto", "Kannada", 
        "Xiang Chinese", "Malayalam", "Sundanese", "Hausa", "Burmese", "Oriya", "Hakka Chinese",
        "Ukrainian", "Bhojpuri", "Tagalog", "Yoruba", "Maithili", "Uzbek", "Sindhi", "Amharic",
        "Fula", "Romanian", "Oromo", "Igbo", "Azerbaijani", "Awadhi", "Gan Chinese", "Cebuano",
        "Dutch", "Kurdish", "Serbo-Croatian", "Malagasy", "Saraiki", "Nepali", "Sinhalese", "Chittagonian",
        "Zhuang", "Khmer", "Turkmen", "Assamese", "Madurese", "Somali", "Marwari", "Magahi",
        "Haryanvi", "Hungarian", "Chhattisgarhi", "Greek", "Chewa", "Deccan", "Akan", "Kazakh",
        "Northern Min", "Sylheti", "Zulu", "Czech", "Kinyarwanda", "Dhundhari", "Haitian Creole", "Eastern Min",
        "Ilocano", "Quechua", "Kirundi", "Swedish", "Hmong", "Shona", "Uyghur", "Hiligaynon",
        "Mossi", "Xhosa", "Belarusian", "Balochi", "Konkani", "Hebrew", "Albanian", "Macedonian",
        "Serbian", "Croatian", "Slovenian", "Bosnian", "Bulgarian", "Ukrainian", "Belarusian", "Romanian",
        "Latvian", "Polish", "Czech", "Estonian", "Dutch", "Hungarian", "Swedish", "Danish",
        "Norwegian", "Icelandic", "Greek", "Welsh", "Irish", "Scots Gaelic", "Manx", "Galician",
        "Catalan", "Basque", "French", "Spanish", "Portuguese", "Italian", "Romanian", "Latin",
        "Corsican", "Sardinian", "Neapolitan", "Sicilian", "Venetian", "Lombard", "Friulian", "Ligurian",
        "Piedmontese", "Emilian-Romagnol", "Calabrian"
    ]
        
    def getRandomLanguages(self, cant: int):
        languageList = random.sample(self.languages, cant)
        return languageList
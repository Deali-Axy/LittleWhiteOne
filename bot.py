from core import ChatBot
from core import config

config.is_need_download_nltk_data = False
config.set_nltk_data_path('.nltk_data')

little_white = ChatBot(
    'LittleWhite',
    storage_adapter='core.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3',
    logic_adapters=[
        "core.logic.MathematicalEvaluation",
        # "core.logic.TimeLogicAdapter",
        {
            'import_path': 'core.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            # 置信度适配器
            'maximum_similarity_threshold': 0.50
        }
    ],
    preprocessors=[
        'core.preprocessors.clean_whitespace'
    ]
)

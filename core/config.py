from nltk import data


def set_nltk_data_path(data_path: str):
    data.path.append(data_path)


is_need_download_nltk_data = False

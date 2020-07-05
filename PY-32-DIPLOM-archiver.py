
class Cloud_archiver:
    PREPARE_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'  # Базовая ссылка как константа

    def __init__(self, token: str, file_path: str, file_name: str):  # передаю параметры отдельно чтобы было понятно
        self.headers = {'Accept': 'application/json', 'Authorization': token}  # Заголовки обновляем токен
        self.params = {'path': f'/{file_name}', 'overwrite': 'true'}  # path - путь у файлу на ЯДиске, overwrite - я разрешаю переписать файл
        self.file_path = file_path
        self.file_name = file_name

    #1. Получать информацию по всем папкам в Я.Диске.
    def cloud_tree(self):
        pass

    #2. Искать среди них самый тяжёлый.
    def get_max_size(self):
        pass

    #3. Скачивать файл на компьютер, где запущена программа.
    def download(self):
        pass

    #4. Архивировать файл.
    def archive_file(self):
        pass

    #5. Загружать его обратно в ту же папку, откуда он был скачен.
    def upload(self):
        response = requests.get(self.PREPARE_UPLOAD_URL, params=self.params, headers=self.headers)
        put_url = response.json().get('href')

        files = {'file': open(self.file_path + self.file_name, 'rb')}
        response = requests.put(put_url, files=files)
        return response.text

    # 6. Записывать информацию по измененному файлу в json-файл
    def stat_json(self):
        pass


if __name__ == '__main__':
    token = 'AgAAAAAy_UpkAADLW4DINWqLNUrUml_SsYrvX7U'  # Укажите свой токен
    #token = input('Введите свой токен аутентификации')
    my_file_path = 'c:/'  # Путь к файлу на Вашем диске
    my_file_name = '9.txt'  # Название файла
    uploader = Cloud_archiver(token, my_file_path, my_file_name)  # Создаю экземпляр класса
    uploader.upload()  # Вызываю нужный метод

    # Нужно написать программу, которая будет:
    # 1. Получать информацию по всем папкам в Я.Диске.
    # 2. Искать среди них самый тяжёлый.
    # 3. Скачивать файл на компьютер, где запущена программа.
    # 4. Архивировать файл.
    # 5. Загружать его обратно в ту же папку, откуда он был скачен.
    # 6. Записывать информацию по измененному файлу в json - файл.




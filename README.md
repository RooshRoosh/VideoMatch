# VideoMatch
Анализируем пригодность видео для поисковой выдачи по запросам "How to..."

- в translate.py содержится функциональность для перевода запросов (пока только через translate.google.com)
- в youtube.py содержится функциональность для выполнения поисковых запросов к YouTube Data API, и получение детальной информации по найденым видео
- application.py выполняет тестовый запуск для запроса "Как сделать красиво?" сохраняя полученные данные в out.json

>Для запуска необходимо создать/определить в файле settings_api.py DEVELOPER_KEY = "API KEY"

приложение работает под python3 все зависимости собраны в requirements.txt

Для установки
> pip install -r requirements.txt

import webbrowser  # Импортируем (делаем доступным для этой программы) весь код из модуля стандартной библиотеки, который называется webbrowser.
import json  # Импортируем весь код из модуля стандартной библиотеки, который называется json.
from urllib.request import urlopen  # Импортируем только функцию urlopen из модуля стандартной библиотеки urllib.request.

print("Программа для поиска архивированных web-страниц с использованием ресурса Wayback Machine (http://archive.org/")  # Выводим на экран приветственный текст нашей программы.
site = input("Введите URL-адрес интересующей Вас web-страницы: ")  # Выводим на экран вопрос об URL, считываем пользовательский ввод и сохраняем это в переменной с именем site.
era = input("Введите интересующую Вас дату в ормате год, месяц, день(образец:20071207) : ")  # Выводим на экран еще один вопрос и на этот раз считываем год, месяц и день, а затем сохраняем их в переменной с именем  era.
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)  # Создаем строковую переменную с именем url, чтобы сайт Wayback Machine искал копию требуемого сайта по дате.
response = urlopen(url)  # Соединяемся с сервером, расположенным по этому адресу, и запрашиваем определенный веб-сервис
contents = response.read()  # Получаем ответ и присваиваем его переменной contents.
text = contents.decode("utf-8")  # Дешифруем содержимое переменной contents в текстовую строку формата JSON и приписываем ее переменной text.
data = json.loads(text)  # Преобразуем переменную text в data — структуру данных языка Python, предназначенную для работы с видео.
try:  # Проверяем на ошибки: помещаем следующие четыре строки в блок try и, если находим ошибку, запускаем последнюю строку программы (она идет после ключевого слова except).
    old_site = data["archived_snapshots"]["closest"]["url"]  # Получив совпадение по сайту и дате, извлекаем нужное значение из трехуровневого словаря Python. Обратите внимание на то, что в этой и двух последующих строках используются отступы — тем самым Python легче понять, что данные строки находятся в блоке try.
    print("Найдена копия web-страницы: ", old_site)  # Выводим на экран полученный URL.
    print("Она должна открыться на вашем PC в web-браузере")  # Сообщаем о том, что случится, когда выполнится следующая строка.
    webbrowser.open(old_site)  # Отображаем полученный URL в браузере.
except:  # # Если во время выполнения предыдущих строк что-то пошло не так, Python перейдет сюда.
    print("Извините, но в архиве ресурса Wayback Machne (http://archive.org/) не найдена web-страница: ", site)  # Если программа дала сбой, выводим сообщение и имя сайта, который мы искали. Эта строка также имеет отступ, поскольку должна выполняться только в том случае, если выполняется строка except.

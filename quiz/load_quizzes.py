# import os
# import django
# import export
# from dotenv import load_dotenv
#
# #
# from quiz.models import Quiz, Question, Answer
#
# #
# # Load environment variables from .env file (if necessary)
# load_dotenv()
#
# # Set the DJANGO_SETTINGS_MODULE environment variable
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduConnect.settings')
#
# # Initialize Django
# django.setup()


#
# def create_quiz(title, grade, subject, description, questions_data):
#     # Create the quiz object but don't save it yet
#     quiz = Quiz(
#         title=title,
#         subject=subject,
#         grade=grade,
#         description=description
#     )
#
#     # Save the quiz object to the database to generate a primary key
#     quiz.save()
#
#     questions_to_create = []
#     answers_to_create = []
#
#     for question_data in questions_data:
#         # Create a Question instance with a foreign key to the saved quiz
#         question = Question(
#             quiz=quiz,
#             text=question_data['question'],
#             question_type='MCQ'
#         )
#         questions_to_create.append(question)
#
#         for answer_data in question_data['answers']:
#             # Create Answer instances for each question
#             answer = Answer(
#                 question=question,
#                 text=answer_data['text'],
#                 is_correct=answer_data['is_correct']
#             )
#             answers_to_create.append(answer)
#
#     # Use bulk_create to save multiple Question and Answer instances at once
#     Question.objects.bulk_create(questions_to_create)
#     Answer.objects.bulk_create(answers_to_create)
#
#
# # """8 КЛАС """
#
# # Литература 8 клас
# questions_lit_8 = [
#     {'question': "Кой е авторът на „Илиада“?",
#      'answers': [{'text': "Омир", 'is_correct': True}, {'text': "Сафо", 'is_correct': False},
#                  {'text': "Платон", 'is_correct': False}, {'text': "Хомер", 'is_correct': False}]},
#     {'question': "Какъв е основният конфликт в „Антигона“?",
#      'answers': [{'text': "Конфликт между личните ценности и обществения закон", 'is_correct': True},
#                  {'text': "Конфликт между боговете", 'is_correct': False},
#                  {'text': "Социален конфликт", 'is_correct': False}, {'text': "Борба за власт", 'is_correct': False}]},
#     {'question': "Коя е основната идея на поемата „Любов“ от Сафо?",
#      'answers': [{'text': "Любовта и страстта", 'is_correct': True}, {'text': "Силата на времето", 'is_correct': False},
#                  {'text': "Живота и смъртта", 'is_correct': False},
#                  {'text': "Философски размисли", 'is_correct': False}]},
#     {'question': "Какъв тип литература е „Декамерон“ на Джовани Бокачо?",
#      'answers': [{'text': "Ренесансова литература", 'is_correct': True},
#                  {'text': "Антична литература", 'is_correct': False},
#                  {'text': "Средновековна литература", 'is_correct': False},
#                  {'text': "Модерна литература", 'is_correct': False}]},
#     {'question': "Какъв е стилът на писане на Уилям Шекспир в „Хамлет“?",
#      'answers': [{'text': "Ренесанс", 'is_correct': True}, {'text': "Барок", 'is_correct': False},
#                  {'text': "Реализъм", 'is_correct': False}, {'text': "Класицизъм", 'is_correct': False}]},
#     {'question': "Коя е основната тема в произведението „За буквите“ на Черноризец Храбър?",
#      'answers': [{'text': "Значението на буквите за българската писменост", 'is_correct': True},
#                  {'text': "Религиозната символика", 'is_correct': False},
#                  {'text': "Философски размисли", 'is_correct': False},
#                  {'text': "Любовта към отечеството", 'is_correct': False}]},
#     {'question': "Какъв е стилът на Сафо в поезията?",
#      'answers': [{'text': "Лирика", 'is_correct': True}, {'text': "Епика", 'is_correct': False},
#                  {'text': "Драма", 'is_correct': False}, {'text': "Философия", 'is_correct': False}]},
#     {'question': "Какъв е конфликтът в „Илиада“ на Омир?",
#      'answers': [{'text': "Конфликт между гърците и троянците", 'is_correct': True},
#                  {'text': "Конфликт между хората и боговете", 'is_correct': False},
#                  {'text': "Лична трагедия", 'is_correct': False}, {'text': "Семейни конфликти", 'is_correct': False}]},
#     {'question': "Коя е главната героиня в „Антигона“?",
#      'answers': [{'text': "Антигона", 'is_correct': True}, {'text': "Креон", 'is_correct': False},
#                  {'text': "Едип", 'is_correct': False}, {'text': "Ифигения", 'is_correct': False}]},
#     {'question': "Какъв тип произведение е „Сонетите“ на Уилям Шекспир?",
#      'answers': [{'text': "Поезия", 'is_correct': True}, {'text': "Проза", 'is_correct': False},
#                  {'text': "Драма", 'is_correct': False}, {'text': "Есе", 'is_correct': False}]},
# ]
#
#
#
# # Математика 8 клас
# questions_math_8 = [
#     {'question': "Какъв е резултатът от израза 2x + 3 = 7?",
#      'answers': [{'text': "x = 2", 'is_correct': True}, {'text': "x = 1", 'is_correct': False},
#                  {'text': "x = 3", 'is_correct': False}, {'text': "x = 4", 'is_correct': False}]},
#     {'question': "Какво е периметър на правоъгълник с дължина 5 см и ширина 3 см?",
#      'answers': [{'text': "16 см", 'is_correct': True}, {'text': "15 см", 'is_correct': False},
#                  {'text': "18 см", 'is_correct': False}, {'text': "14 см", 'is_correct': False}]},
#     {'question': "Какво е обемът на куб със страна 4 см?",
#      'answers': [{'text': "64 см³", 'is_correct': True}, {'text': "16 см³", 'is_correct': False},
#                  {'text': "8 см³", 'is_correct': False}, {'text': "4 см³", 'is_correct': False}]},
#     {'question': "Каква е площта на триъгълник с база 6 см и височина 4 см?",
#      'answers': [{'text': "12 см²", 'is_correct': True}, {'text': "24 см²", 'is_correct': False},
#                  {'text': "10 см²", 'is_correct': False}, {'text': "14 см²", 'is_correct': False}]},
#     {'question': "Как се нарича математическата операция, при която се събират числа?",
#      'answers': [{'text': "Събиране", 'is_correct': True}, {'text': "Изваждане", 'is_correct': False},
#                  {'text': "Умножение", 'is_correct': False}, {'text': "Деление", 'is_correct': False}]},
#     {'question': "Какъв е коренът на числото 25?",
#      'answers': [{'text': "5", 'is_correct': True}, {'text': "4", 'is_correct': False},
#                  {'text': "6", 'is_correct': False}, {'text': "3", 'is_correct': False}]},
#     {'question': "Какво е разстоянието между точките A(2, 3) и B(5, 7)?",
#      'answers': [{'text': "5", 'is_correct': True}, {'text': "4", 'is_correct': False},
#                  {'text': "6", 'is_correct': False}, {'text': "7", 'is_correct': False}]},
#     {'question': "Какъв е ъгълът между две перпендикулярни прави?",
#      'answers': [{'text': "90°", 'is_correct': True}, {'text': "45°", 'is_correct': False},
#                  {'text': "60°", 'is_correct': False}, {'text': "180°", 'is_correct': False}]},
#     {'question': "Какво представлява система от линейни уравнения?",
#      'answers': [{'text': "Набор от уравнения с две или повече неизвестни", 'is_correct': True},
#                  {'text': "Набор от уравнения с една неизвестна", 'is_correct': False},
#                  {'text': "Система от нелинейни уравнения", 'is_correct': False},
#                  {'text': "Набор от равенства", 'is_correct': False}]},
#     {'question': "Какво е основното свойство на прави, които се пресичат под ъгъл от 90°?",
#      'answers': [{'text': "Те са перпендикулярни", 'is_correct': True},
#                  {'text': "Те са успоредни", 'is_correct': False}, {'text': "Те са равни", 'is_correct': False},
#                  {'text': "Те образуват равностранен триъгълник", 'is_correct': False}]}
# ]
#
#
#
# # Биология 8 клас
# questions_biology_8 = [
#     {'question': "Какво представлява клетката?",
#      'answers': [{'text': "Основната единица на живота", 'is_correct': True},
#                  {'text': "Най-голямата част от организма", 'is_correct': False},
#                  {'text': "Молекула, от която се състоят живите организми", 'is_correct': False},
#                  {'text': "Образувание от различни органи", 'is_correct': False}]},
#     {'question': "Какво е функцията на хлоропластите?",
#      'answers': [{'text': "Събиране на светлинна енергия и синтез на храна", 'is_correct': True},
#                  {'text': "Транспорт на кислород в клетката", 'is_correct': False},
#                  {'text': "Размножаване на клетките", 'is_correct': False},
#                  {'text': "Поддържане на клетъчната структура", 'is_correct': False}]},
#     {'question': "Как се нарича процесът, при който растенията произвеждат храна?",
#      'answers': [{'text': "Фотосинтеза", 'is_correct': True}, {'text': "Дишане", 'is_correct': False},
#                  {'text': "Транспирация", 'is_correct': False}, {'text': "Репродукция", 'is_correct': False}]},
#     {'question': "Какво съдържа клетъчната мембрана?", 'answers': [{'text': "Липиди и протеини", 'is_correct': True},
#                                                                    {'text': "Вода и въглеродни съединения",
#                                                                     'is_correct': False},
#                                                                    {'text': "ДНК и РНК", 'is_correct': False},
#                                                                    {'text': "Митохондрии", 'is_correct': False}]},
#     {'question': "Какво е хомеостаза?",
#      'answers': [{'text': "Поддържане на стабилни условия в организма", 'is_correct': True},
#                  {'text': "Размножаване на клетките", 'is_correct': False},
#                  {'text': "Преработка на храна", 'is_correct': False},
#                  {'text': "Преработка на кислород", 'is_correct': False}]},
#     {'question': "Какво представлява процесът на митоза?",
#      'answers': [{'text': "Разделяне на една клетка на две идентични клетки", 'is_correct': True},
#                  {'text': "Процес на производство на енергия", 'is_correct': False},
#                  {'text': "Превръщане на клетката в орган", 'is_correct': False},
#                  {'text': "Транспорт на вещества в клетката", 'is_correct': False}]},
#     {'question': "Какво е основната цел на дишането в клетките?",
#      'answers': [{'text': "Производство на енергия", 'is_correct': True},
#                  {'text': "Освобождаване на кислород", 'is_correct': False},
#                  {'text': "Преработка на храна", 'is_correct': False},
#                  {'text': "Съхранение на вода", 'is_correct': False}]},
#     {'question': "Какви са основните елементи в състава на ДНК?",
#      'answers': [{'text': "Аденин, тимин, гуанин, цитозин", 'is_correct': True},
#                  {'text': "Натрий, калий, магнезий", 'is_correct': False},
#                  {'text': "Протеини и въглехидрати", 'is_correct': False},
#                  {'text': "Глюкоза и кислород", 'is_correct': False}]},
#     {'question': "Как се нарича процесът, при който клетките произвеждат нови клетки?",
#      'answers': [{'text': "Митоза", 'is_correct': True}, {'text': "Мейоза", 'is_correct': False},
#                  {'text': "Репликация", 'is_correct': False}, {'text': "Фотосинтеза", 'is_correct': False}]},
#     {'question': "Какво е основната функция на сърцето?",
#      'answers': [{'text': "Транспортиране на кръв в тялото", 'is_correct': True},
#                  {'text': "Пробуждане на клетките", 'is_correct': False},
#                  {'text': "Разпределение на хранителни вещества", 'is_correct': False},
#                  {'text': "Продукция на хормони", 'is_correct': False}]}
# ]
#
#
#
# questions_geo_8 = [
#     {'question': "Какво е географска ширина?",
#      'answers': [{'text': "Разстоянието на дадена точка от екватора", 'is_correct': True},
#                  {'text': "Разстоянието на дадена точка от меридиан", 'is_correct': False},
#                  {'text': "Височината на дадена точка", 'is_correct': False},
#                  {'text': "Разстоянието на дадена точка от северния полюс", 'is_correct': False}]},
#     {'question': "Какво е географска дължина?",
#      'answers': [{'text': "Разстоянието на дадена точка от нулевия меридиан", 'is_correct': True},
#                  {'text': "Разстоянието на дадена точка от екватора", 'is_correct': False},
#                  {'text': "Височината на дадена точка", 'is_correct': False},
#                  {'text': "Разстоянието на дадена точка от полюсите", 'is_correct': False}]},
#     {'question': "Какво означава терминът 'атмосферно налягане'?",
#      'answers': [{'text': "Теглото на въздушната маса, действаща върху земната повърхност", 'is_correct': True},
#                  {'text': "Силата на вятъра", 'is_correct': False},
#                  {'text': "Температурата на въздуха", 'is_correct': False},
#                  {'text': "Обемът на въздушната маса", 'is_correct': False}]},
#     {'question': "Какво е климат?",
#      'answers': [{'text': "Средните метеорологични условия за дълъг период", 'is_correct': True},
#                  {'text': "Промените на времето за кратък период", 'is_correct': False},
#                  {'text': "Състоянието на атмосферата в даден момент", 'is_correct': False},
#                  {'text': "Температури и вятър", 'is_correct': False}]},
#     {'question': "Какви са основните географски фактори?",
#      'answers': [{'text': "Климат, релеф, растителност, води", 'is_correct': True},
#                  {'text': "Население и технологии", 'is_correct': False},
#                  {'text': "Топография и география", 'is_correct': False},
#                  {'text': "Фауна и флора", 'is_correct': False}]},
#     {'question': "Как се нарича най-дългата река в света?",
#      'answers': [{'text': "Амазонка", 'is_correct': True}, {'text': "Нил", 'is_correct': False},
#                  {'text': "Мисисипи", 'is_correct': False}, {'text': "Ганг", 'is_correct': False}]},
#     {'question': "Какво е континент?",
#      'answers': [{'text': "Голяма маса суша, обикновено отделена от океани", 'is_correct': True},
#                  {'text': "Малка част суша", 'is_correct': False}, {'text': "Остров в океан", 'is_correct': False},
#                  {'text': "Елемент в природата", 'is_correct': False}]},
#     {'question': "Каква е основната причина за сезонните промени?",
#      'answers': [{'text': "Наклонът на земната ос и орбитата около Слънцето", 'is_correct': True},
#                  {'text': "Въздухът в атмосферата", 'is_correct': False},
#                  {'text': "Промените в географската ширина", 'is_correct': False},
#                  {'text': "Водата в океаните", 'is_correct': False}]},
#     {'question': "Какво е териториална морска зона?",
#      'answers': [{'text': "Част от морето, която принадлежи на определена държава", 'is_correct': True},
#                  {'text': "Най-близката част от океана до земята", 'is_correct': False},
#                  {'text': "Географски район", 'is_correct': False}, {'text': "Морски проход", 'is_correct': False}]},
#     {'question': "Какво е основно в изучаването на география?",
#      'answers': [{'text': "Взаимодействието на природните и човешките фактори", 'is_correct': True},
#                  {'text': "Само физическите явления", 'is_correct': False},
#                  {'text': "Само човешките фактори", 'is_correct': False},
#                  {'text': "Технологиите в географията", 'is_correct': False}]},
# ]
# questions_philosophy_8 = [
#     {'question': "Коя философска школа поставя акцент на разума като път към познанието?",
#      'answers': [{'text': "Рационализъм", 'is_correct': True}, {'text': "Емпиризъм", 'is_correct': False},
#                  {'text': "Скептицизъм", 'is_correct': False}, {'text': "Позитивизъм", 'is_correct': False}]},
#     {'question': "Какво означава терминът 'екзистенциализъм'?",
#      'answers': [{'text': "Философия, която се занимава с човешкото съществуване", 'is_correct': True},
#                  {'text': "Течност в изкуствата", 'is_correct': False},
#                  {'text': "Философия на религията", 'is_correct': False},
#                  {'text': "Учение за морала", 'is_correct': False}]},
#     {'question': "Какво означава терминът 'софизъм'?",
#      'answers': [{'text': "Изкуство на лъжливо, манипулативно разсъждение", 'is_correct': True},
#                  {'text': "Философия на битието", 'is_correct': False},
#                  {'text': "Идея за истината", 'is_correct': False},
#                  {'text': "Погрешен начин на мислене", 'is_correct': False}]},
#     {'question': "Какъв е основният въпрос за философията на Древна Гърция?",
#      'answers': [{'text': "Какво е съществуването?", 'is_correct': True},
#                  {'text': "Какъв е правилният начин на живот?", 'is_correct': False},
#                  {'text': "Какви са природните сили?", 'is_correct': False},
#                  {'text': "Какво е справедливостта?", 'is_correct': False}]},
#     {'question': "Какво е прагматизъм?",
#      'answers': [{'text': "Философия, която се фокусира върху практическите резултати", 'is_correct': True},
#                  {'text': "Философия на интуицията", 'is_correct': False},
#                  {'text': "Учение за абстрактните идеи", 'is_correct': False},
#                  {'text': "Философия на моралните задължения", 'is_correct': False}]},
#     {'question': "Кой философ е основател на стоицизма?",
#      'answers': [{'text': "Зенон от Китий", 'is_correct': True}, {'text': "Платон", 'is_correct': False},
#                  {'text': "Аристотел", 'is_correct': False}, {'text': "Сократ", 'is_correct': False}]},
#     {'question': "Какво е основното учение на Платон?",
#      'answers': [{'text': "Идеите са реалността", 'is_correct': True},
#                  {'text': "Материалният свят е единственото, което съществува", 'is_correct': False},
#                  {'text': "Човекът е създаден за щастие", 'is_correct': False},
#                  {'text': "Знанието е вродено", 'is_correct': False}]},
#     {'question': "Кой философ е основател на философията на перипатетиците?",
#      'answers': [{'text': "Аристотел", 'is_correct': True}, {'text': "Платон", 'is_correct': False},
#                  {'text': "Сократ", 'is_correct': False}, {'text': "Пифагор", 'is_correct': False}]},
#     {'question': "Какво е скептицизъм?", 'answers': [
#         {'text': "Философски подход, който поставя под съмнение истинността на всички твърдения", 'is_correct': True},
#         {'text': "Позитивно философско учение", 'is_correct': False},
#         {'text': "Философия на съществуването", 'is_correct': False},
#         {'text': "Течение в моралната философия", 'is_correct': False}]},
#     {'question': "Какъв е философският въпрос за нещата?",
#      'answers': [{'text': "Какво представлява същността на нещата?", 'is_correct': True},
#                  {'text': "Как да постигнем успех?", 'is_correct': False},
#                  {'text': "Какви са нормите на доброто?", 'is_correct': False},
#                  {'text': "Какво представлява знанието?", 'is_correct': False}]},
# ]
#
# questions_bg_8 = [
#     {'question': "Какво е синоним?", 'answers': [{'text': "Думи с близко значение", 'is_correct': True},
#                                                  {'text': "Думи с противоположно значение", 'is_correct': False},
#                                                  {'text': "Думи с различно значение", 'is_correct': False},
#                                                  {'text': "Думи, които звучат еднакво", 'is_correct': False}]},
#     {'question': "Какво е антоним?", 'answers': [{'text': "Думи с противоположно значение", 'is_correct': True},
#                                                  {'text': "Думи с близко значение", 'is_correct': False},
#                                                  {'text': "Думи със същото значение", 'is_correct': False},
#                                                  {'text': "Думи с различно значение", 'is_correct': False}]},
#     {'question': "Каква е основната роля на членуването в българския език?", 'answers': [
#         {'text': "Определя начина на отношение между членуваните съществителни имена и други части на изречението",
#          'is_correct': True}, {'text': "Показва кога да се използва глагол", 'is_correct': False},
#         {'text': "Изразява времето на действието", 'is_correct': False},
#         {'text': "Отделя частите на изречението", 'is_correct': False}]},
#     {'question': "Какво е въпросителното изречение?",
#      'answers': [{'text': "Изречение, което поставя въпрос", 'is_correct': True},
#                  {'text': "Изречение, което съдържа уточняваща информация", 'is_correct': False},
#                  {'text': "Изречение, което изразява твърдение", 'is_correct': False},
#                  {'text': "Изречение, което изразява състояние", 'is_correct': False}]},
#     {'question': "Какво е съществително?",
#      'answers': [{'text': "Част на речта, която назовава предмети, явления, хора", 'is_correct': True},
#                  {'text': "Част на речта, която показва действие", 'is_correct': False},
#                  {'text': "Част на речта, която описва обект", 'is_correct': False},
#                  {'text': "Част на речта, която замества съществително име", 'is_correct': False}]},
#     {'question': "Какво е глагол?", 'answers': [{'text': "Част на речта, която изразява действие", 'is_correct': True},
#                                                 {'text': "Част на речта, която назовава състояние",
#                                                  'is_correct': False},
#                                                 {'text': "Част на речта, която показва отношение", 'is_correct': False},
#                                                 {'text': "Част на речта, която означава съществуване",
#                                                  'is_correct': False}]},
#     {'question': "Какво е личната форма на глагола?",
#      'answers': [{'text': "Глагол, който се променя според лице и число", 'is_correct': True},
#                  {'text': "Глагол, който не променя форма", 'is_correct': False},
#                  {'text': "Глагол, който се използва само в минало време", 'is_correct': False},
#                  {'text': "Глагол, който се използва в бъдеще време", 'is_correct': False}]},
#     {'question': "Какво е метафора?",
#      'answers': [{'text': "Риторичен израз, при който дума се употребява в преносно значение", 'is_correct': True},
#                  {'text': "Фигура на изречението, при която се използва въпрос", 'is_correct': False},
#                  {'text': "Риторичен израз, при който се съпоставят два противоположни образа", 'is_correct': False},
#                  {'text': "Литературно средство за описване на движение", 'is_correct': False}]},
#     {'question': "Какво означава терминът 'епитет'?",
#      'answers': [{'text': "Прилагателно име, което характеризира предмета", 'is_correct': True},
#                  {'text': "Съществително, което се използва за подчертаване на състояние", 'is_correct': False},
#                  {'text': "Част от речта, която назовава действия", 'is_correct': False},
#                  {'text': "Глагол, който определя действия", 'is_correct': False}]},
#     {'question': "Какво е основно в стихотворението?",
#      'answers': [{'text': "Тема, която се разглежда в литературната творба", 'is_correct': True},
#                  {'text': "Част от речта", 'is_correct': False}, {'text': "Действие", 'is_correct': False},
#                  {'text': "Ритъм", 'is_correct': False}]}
# ]
# questions_chemistry_8 = [
#     {'question': "Какво е атом?",
#      'answers': [{'text': "Основна частица на веществото, състояща се от ядро и електрони", 'is_correct': True},
#                  {'text': "Частица, която не може да се раздели", 'is_correct': False},
#                  {'text': "Молекула на елемент", 'is_correct': False},
#                  {'text': "Молекула на съединение", 'is_correct': False}]},
#     {'question': "Какво е молекула?", 'answers': [{'text': "Съединение от два или повече атома", 'is_correct': True},
#                                                   {'text': "Частица на елемента", 'is_correct': False},
#                                                   {'text': "Съединение от два атома на различни елементи",
#                                                    'is_correct': False},
#                                                   {'text': "Атом с електронно облако", 'is_correct': False}]},
#     {'question': "Как се нарича процесът на преминаване от твърдо състояние в течно?",
#      'answers': [{'text': "Топене", 'is_correct': True}, {'text': "Замръзване", 'is_correct': False},
#                  {'text': "Изпаряване", 'is_correct': False}, {'text': "Кристализация", 'is_correct': False}]},
#     {'question': "Какво е химична реакция?",
#      'answers': [{'text': "Процес на превръщане на вещества в нови вещества", 'is_correct': True},
#                  {'text': "Съединяване на атоми", 'is_correct': False},
#                  {'text': "Процес на отделяне на енергия", 'is_correct': False},
#                  {'text': "Процес на преминаване на вещество от едно състояние в друго", 'is_correct': False}]},
#     {'question': "Какво е елемент?",
#      'answers': [{'text': "Вещество, което не може да се разложи на по-прости вещества", 'is_correct': True},
#                  {'text': "Комбинация от различни елементи", 'is_correct': False},
#                  {'text': "Процес на химична реакция", 'is_correct': False},
#                  {'text': "Атом със специфична структура", 'is_correct': False}]},
#     {'question': "Как се нарича химичната връзка между атомите в молекулата на вода?",
#      'answers': [{'text': "Ковалентна връзка", 'is_correct': True}, {'text': "Йонна връзка", 'is_correct': False},
#                  {'text': "Метална връзка", 'is_correct': False}, {'text': "Хидрогенна връзка", 'is_correct': False}]},
#     {'question': "Какво представлява pH стойността?",
#      'answers': [{'text': "Мярка за киселинността или алкалността на разтвор", 'is_correct': True},
#                  {'text': "Мярка за концентрацията на водородни йони", 'is_correct': False},
#                  {'text': "Силата на химичните реакции", 'is_correct': False},
#                  {'text': "Концентрация на кислородни молекули", 'is_correct': False}]},
#     {'question': "Какво е катализатор?",
#      'answers': [{'text': "Вещества, които ускоряват химичните реакции, без да се променят трайно", 'is_correct': True},
#                  {'text': "Елемент, който участва в химичните реакции", 'is_correct': False},
#                  {'text': "Съединение, което забавя реакцията", 'is_correct': False},
#                  {'text': "Реагент в химична реакция", 'is_correct': False}]},
#     {'question': "Какво е химична формула?",
#      'answers': [{'text': "Представяне на съединение с помощта на символи на елементите", 'is_correct': True},
#                  {'text': "Експериментално доказателство на реакция", 'is_correct': False},
#                  {'text': "Математическо уравнение на химична реакция", 'is_correct': False},
#                  {'text': "Техника на лабораторни изследвания", 'is_correct': False}]},
#     {'question': "Какво е окисление?",
#      'answers': [{'text': "Процес на отдаване на електрони от атоми", 'is_correct': True},
#                  {'text': "Процес на приемане на електрони от атоми", 'is_correct': False},
#                  {'text': "Процес на образуване на молекули", 'is_correct': False},
#                  {'text': "Процес на преминаване от течност в газ", 'is_correct': False}]}
# ]
# questions_history_8 = [
#     {'question': "Кой е основател на Българската държава?",
#      'answers': [{'text': "Асен и Петър", 'is_correct': False}, {'text': "Кан Аспарух", 'is_correct': True},
#                  {'text': "Цар Самуил", 'is_correct': False}, {'text': "Св. Методий", 'is_correct': False}]},
#     {'question': "Кога се създава Българската държава?",
#      'answers': [{'text': "680 г.", 'is_correct': True}, {'text': "681 г.", 'is_correct': False},
#                  {'text': "800 г.", 'is_correct': False}, {'text': "600 г.", 'is_correct': False}]},
#     {'question': "Какво е Велика България?", 'answers': [{'text': "Древно българско царство", 'is_correct': True},
#                                                          {'text': "Древен тракийски съюз", 'is_correct': False},
#                                                          {'text': "Държава на славяните", 'is_correct': False},
#                                                          {'text': "Нова българска държава", 'is_correct': False}]},
#     {'question': "Кой е бил цар по време на българското средновековие, когато България била най-голяма?",
#      'answers': [{'text': "Цар Самуил", 'is_correct': True}, {'text': "Цар Симеон", 'is_correct': False},
#                  {'text': "Цар Борис I", 'is_correct': False}, {'text': "Цар Иван Асен II", 'is_correct': False}]},
#     {'question': "Какво е християнизация?",
#      'answers': [{'text': "Превръщането на България в християнска държава", 'is_correct': True},
#                  {'text': "Процес на разпространение на християнството в Европа", 'is_correct': False},
#                  {'text': "Разделение на християнството на източна и западна църква", 'is_correct': False},
#                  {'text': "Процес на приемане на исляма", 'is_correct': False}]},
#     {'question': "Какво е Преображение?",
#      'answers': [{'text': "Събитие, свързано с религиозния празник на християнството", 'is_correct': True},
#                  {'text': "Период на българска литература", 'is_correct': False},
#                  {'text': "Период на царуване на Цар Симеон", 'is_correct': False},
#                  {'text': "Разделяне на България на два региона", 'is_correct': False}]},
#     {'question': "Какъв е основният резултат от победата на българите при Ахелой?",
#      'answers': [{'text': "Запазване на независимостта на България", 'is_correct': True},
#                  {'text': "Разширяване на териториите на България", 'is_correct': False},
#                  {'text': "Започване на разпад на България", 'is_correct': False},
#                  {'text': "Решаваща победа за Римската империя", 'is_correct': False}]},
#     {'question': "Как се нарича българската азбука?",
#      'answers': [{'text': "Глаголица", 'is_correct': True}, {'text': "Кирилица", 'is_correct': False},
#                  {'text': "Латиница", 'is_correct': False}, {'text': "Славянска азбука", 'is_correct': False}]},
#     {'question': "Кой е известен български владетел, наречен 'българския Сократ'?",
#      'answers': [{'text': "Цар Симеон", 'is_correct': True}, {'text': "Цар Борис I", 'is_correct': False},
#                  {'text': "Цар Иван Асен II", 'is_correct': False}, {'text': "Цар Самуил", 'is_correct': False}]},
#     {'question': "Какво е основното постижение на Кирил и Методий?",
#      'answers': [{'text': "Създаване на българската азбука", 'is_correct': True},
#                  {'text': "Превод на Библията на български език", 'is_correct': False},
#                  {'text': "Превод на Гръцката Библия на старобългарски", 'is_correct': False},
#                  {'text': "Създаване на славянски език", 'is_correct': False}]}
# ]
# questions_physics_8 = [
#     {'question': "Какво е ускорение?", 'answers': [{'text': "Промяна на скоростта с времето", 'is_correct': True},
#                                                    {'text': "Промяна на позицията с времето", 'is_correct': False},
#                                                    {'text': "Сила, която действа върху обект", 'is_correct': False},
#                                                    {'text': "Мярка за скоростта на обекта", 'is_correct': False}]},
#     {'question': "Какво е закон на Нютон?",
#      'answers': [{'text': "Закон, който описва движението на обектите", 'is_correct': True},
#                  {'text': "Закон за енергията", 'is_correct': False},
#                  {'text': "Закон за сила и мощност", 'is_correct': False},
#                  {'text': "Закон за електрическото поле", 'is_correct': False}]},
#     {'question': "Какво е гравитация?",
#      'answers': [{'text': "Сила, която привлича обектите към центъра на Земята", 'is_correct': True},
#                  {'text': "Сила, която изтласква обектите", 'is_correct': False},
#                  {'text': "Процес на повишаване на температурата", 'is_correct': False},
#                  {'text': "Промяна на масата на обектите", 'is_correct': False}]},
#     {'question': "Какво е движение?",
#      'answers': [{'text': "Промяна на местоположението на обект с времето", 'is_correct': True},
#                  {'text': "Промяна на формата на обект", 'is_correct': False},
#                  {'text': "Силата, която действа на обекта", 'is_correct': False},
#                  {'text': "Състоянието на обекта, когато не се движи", 'is_correct': False}]},
#     {'question': "Каква е единицата за сила в Международната система?",
#      'answers': [{'text': "Нютон", 'is_correct': True}, {'text': "Джаул", 'is_correct': False},
#                  {'text': "Ват", 'is_correct': False}, {'text': "Ампер", 'is_correct': False}]},
#     {'question': "Какво е работа в физика?",
#      'answers': [{'text': "Сила, умножена по изминатото разстояние", 'is_correct': True},
#                  {'text': "Сила, умножена по време", 'is_correct': False},
#                  {'text': "Енергия, която се преобразува", 'is_correct': False},
#                  {'text': "Температура, която се увеличава", 'is_correct': False}]},
#     {'question': "Какво е кинетична енергия?",
#      'answers': [{'text': "Енергията на движението на обект", 'is_correct': True},
#                  {'text': "Енергията на потенциалното състояние на обект", 'is_correct': False},
#                  {'text': "Енергията, която се освобождава при химични реакции", 'is_correct': False},
#                  {'text': "Енергията на звука", 'is_correct': False}]},
#     {'question': "Какво е електрическа енергия?",
#      'answers': [{'text': "Енергия, свързана с движението на електрически заряди", 'is_correct': True},
#                  {'text': "Енергия, получена от химични реакции", 'is_correct': False},
#                  {'text': "Енергия, свързана с температурата на обект", 'is_correct': False},
#                  {'text': "Енергия, която не може да се използва", 'is_correct': False}]},
#     {'question': "Какво е закон за запазване на енергията?", 'answers': [
#         {'text': "Енергията не може да бъде създадена или унищожена, а само преобразувана", 'is_correct': True},
#         {'text': "Енергията може да се създава и унищожава", 'is_correct': False},
#         {'text': "Енергията е постоянна във всяка система", 'is_correct': False},
#         {'text': "Енергията се увеличава при всяко движение", 'is_correct': False}]},
#     {'question': "Какво е топлина?",
#      'answers': [{'text': "Енергия, която се пренася от по-топло тяло към по-студено", 'is_correct': True},
#                  {'text': "Енергия, която се генерира при механична работа", 'is_correct': False},
#                  {'text': "Енергия, свързана с електрически заряд", 'is_correct': False},
#                  {'text': "Енергия, която се освобождава при химични реакции", 'is_correct': False}]}
# ]
# questions_it_8 = [
#     {'question': "Какво е алгоритъм?",
#      'answers': [{'text': "Стъпков план за решаване на даден проблем", 'is_correct': True},
#                  {'text': "Компютърна програма", 'is_correct': False},
#                  {'text': "Компютърна мрежа", 'is_correct': False},
#                  {'text': "Математическа операция", 'is_correct': False}]},
#     {'question': "Какво е операционна система?",
#      'answers': [{'text': "Програма, която управлява компютърните ресурси", 'is_correct': True},
#                  {'text': "Компютърна програма за съхранение на данни", 'is_correct': False},
#                  {'text': "Процес за управление на мрежа", 'is_correct': False},
#                  {'text': "Програма за работа с интернет", 'is_correct': False}]},
#     {'question': "Какво е HTML?", 'answers': [{'text': "Език за създаване на уеб страници", 'is_correct': True},
#                                               {'text': "Компютърна програма", 'is_correct': False},
#                                               {'text': "Алгоритъм за обработка на данни", 'is_correct': False},
#                                               {'text': "Електронна таблица", 'is_correct': False}]},
#     {'question': "Какво е програмиране?",
#      'answers': [{'text': "Процес на писане на компютърни програми", 'is_correct': True},
#                  {'text': "Процес на създаване на алгоритми", 'is_correct': False},
#                  {'text': "Процес на управление на компютърна мрежа", 'is_correct': False},
#                  {'text': "Процес на съхранение на данни", 'is_correct': False}]},
#     {'question': "Какво е компютърна мрежа?",
#      'answers': [{'text': "Система от свързани компютри, които обменят информация", 'is_correct': True},
#                  {'text': "Програма за управление на данни", 'is_correct': False},
#                  {'text': "Програма за обработка на текст", 'is_correct': False},
#                  {'text': "Тип операционна система", 'is_correct': False}]},
#     {'question': "Какво е интернет?", 'answers': [{'text': "Глобална мрежа за обмен на данни", 'is_correct': True},
#                                                   {'text': "Програма за работа с текст", 'is_correct': False},
#                                                   {'text': "Компютърна програма за съхранение на информация",
#                                                    'is_correct': False},
#                                                   {'text': "Местна компютърна мрежа", 'is_correct': False}]},
#     {'question': "Какво представлява софтуер?",
#      'answers': [{'text': "Програми, които управляват компютърната система", 'is_correct': True},
#                  {'text': "Хардуерни компоненти на компютър", 'is_correct': False},
#                  {'text': "Процес на обработка на данни", 'is_correct': False},
#                  {'text': "Системи за комуникация между компютри", 'is_correct': False}]},
#     {'question': "Какво е електронна таблица?",
#      'answers': [{'text': "Програма за работа с числови данни", 'is_correct': True},
#                  {'text': "Програма за обработка на изображения", 'is_correct': False},
#                  {'text': "Програма за създаване на уеб страници", 'is_correct': False},
#                  {'text': "Мрежова платформа", 'is_correct': False}]},
#     {'question': "Какво е база данни?",
#      'answers': [{'text': "Система за съхранение и управление на данни", 'is_correct': True},
#                  {'text': "Програма за работа с текстови документи", 'is_correct': False},
#                  {'text': "Програма за обработка на изображения", 'is_correct': False},
#                  {'text': "Програма за създаване на интернет страници", 'is_correct': False}]},
#     {'question': "Какво е изкуствен интелект?",
#      'answers': [{'text': "Системи, които имитират човешки интелект", 'is_correct': True},
#                  {'text': "Програма за анализ на текстови данни", 'is_correct': False},
#                  {'text': "Процес за обучение на компютърни мрежи", 'is_correct': False},
#                  {'text': "Процес на оптимизация на алгоритми", 'is_correct': False}]}
# ]
# questions_english_8 = [
#     {'question': "What is the past tense of 'go'?",
#      'answers': [{'text': "Went", 'is_correct': True}, {'text': "Gone", 'is_correct': False},
#                  {'text': "Going", 'is_correct': False}, {'text': "Goes", 'is_correct': False}]},
#     {'question': "Which of the following is an irregular verb?",
#      'answers': [{'text': "Fly", 'is_correct': True}, {'text': "Play", 'is_correct': False},
#                  {'text': "Talk", 'is_correct': False}, {'text': "Work", 'is_correct': False}]},
#     {'question': "What is the future tense of 'eat'?",
#      'answers': [{'text': "Will eat", 'is_correct': True}, {'text': "Eating", 'is_correct': False},
#                  {'text': "Ate", 'is_correct': False}, {'text': "Eats", 'is_correct': False}]},
#     {'question': "Which of the following is a correct sentence?",
#      'answers': [{'text': "She can swim very well", 'is_correct': True},
#                  {'text': "She can swimming very well", 'is_correct': False},
#                  {'text': "She swim can very well", 'is_correct': False},
#                  {'text': "She well can swimming very", 'is_correct': False}]},
#     {'question': "What is the synonym of 'happy'?",
#      'answers': [{'text': "Joyful", 'is_correct': True}, {'text': "Sad", 'is_correct': False},
#                  {'text': "Angry", 'is_correct': False}, {'text': "Tired", 'is_correct': False}]},
#     {'question': "Which word is a preposition?",
#      'answers': [{'text': "Under", 'is_correct': True}, {'text': "Jump", 'is_correct': False},
#                  {'text': "Run", 'is_correct': False}, {'text': "Sing", 'is_correct': False}]},
#     {'question': "What is the past participle of 'eat'?",
#      'answers': [{'text': "Eaten", 'is_correct': True}, {'text': "Ate", 'is_correct': False},
#                  {'text': "Eats", 'is_correct': False}, {'text': "Eating", 'is_correct': False}]},
#     {'question': "Which sentence is in the present continuous tense?",
#      'answers': [{'text': "She is reading a book", 'is_correct': True},
#                  {'text': "She reads a book", 'is_correct': False}, {'text': "She read a book", 'is_correct': False},
#                  {'text': "She will read a book", 'is_correct': False}]},
#     {'question': "Which of these sentences is a question?",
#      'answers': [{'text': "Is he coming to the party?", 'is_correct': True},
#                  {'text': "He is coming to the party", 'is_correct': False},
#                  {'text': "He came to the party", 'is_correct': False},
#                  {'text': "He will come to the party", 'is_correct': False}]},
#     {'question': "What is the plural form of 'child'?",
#      'answers': [{'text': "Children", 'is_correct': True}, {'text': "Childs", 'is_correct': False},
#                  {'text': "Childrens", 'is_correct': False}, {'text': "Childer", 'is_correct': False}]}
# ]
#
# # 9 клас - Литература
# # questions_lit_9 = [
# #     {'question': "Какъв е основният мотив в „Пътешествията на Гъливер“?", 'answers': [{'text': "Критика на човешката природа", 'is_correct': True}, {'text': "Похвала на човешката доброта", 'is_correct': False}, {'text': "История за един човек", 'is_correct': False}, {'text': "Отношение към науката", 'is_correct': False}]},
# #     {'question': "Какъв е основният въпрос в „Дон Жуан“ на Байрон?", 'answers': [{'text': "Нравственото падение на човека", 'is_correct': True}, {'text': "Личната свобода", 'is_correct': False}, {'text': "Личността и обществото", 'is_correct': False}, {'text': "Любовта и свободата", 'is_correct': False}]},
# #     {'question': "Какво разглежда „Евгений Онегин“?", 'answers': [{'text': "Модернизма в Русия", 'is_correct': False}, {'text': "Социалния живот и личните трагедии", 'is_correct': True}, {'text': "Непокорството на героите", 'is_correct': False}, {'text': "История на революцията", 'is_correct': False}]},
# #     {'question': "Кой автор е написал „Дядо Горио“?", 'answers': [{'text': "Оноре дьо Балзак", 'is_correct': True}, {'text': "Гюстав Флобер", 'is_correct': False}, {'text': "Шарл Бодлер", 'is_correct': False}, {'text': "Алфред дьо Мюсе", 'is_correct': False}]},
# #     {'question': "Каква е основната тема в „Мадам Бовари“?", 'answers': [{'text': "Бедността в провинцията", 'is_correct': False}, {'text': "Социалните конфликти", 'is_correct': False}, {'text': "Разочарованията на героинята", 'is_correct': True}, {'text': "Мечтите за по-добър живот", 'is_correct': False}]},
# #     {'question': "Кой автор е написал стихотворението „Сплин“?", 'answers': [{'text': "Шарл Бодлер", 'is_correct': True}, {'text': "Пейо Яворов", 'is_correct': False}, {'text': "Албер Камю", 'is_correct': False}, {'text': "Пол Верлен", 'is_correct': False}]},
# #     {'question': "Какво изразява стихотворението „Есенна песен“ на Верлен?", 'answers': [{'text': "Тъга и меланхолия", 'is_correct': True}, {'text': "Радост и споделеност", 'is_correct': False}, {'text': "Надежда за бъдещето", 'is_correct': False}, {'text': "Вяра в любовта", 'is_correct': False}]},
# #     {'question': "Какъв е основният въпрос в „История славянобългарска“ на Паисий Хилендарски?", 'answers': [{'text': "История на българите и тяхната свобода", 'is_correct': True}, {'text': "Какво означава християнството", 'is_correct': False}, {'text': "Значението на българската литература", 'is_correct': False}, {'text': "Възходът на българския народ", 'is_correct': False}]},
# #     {'question': "Какъв е въпросът в стихотворението „Изворът на белоногата“ на Петко Славейков?", 'answers': [{'text': "Любов и природата", 'is_correct': True}, {'text': "Отношенията между народите", 'is_correct': False}, {'text': "Борба за свобода", 'is_correct': False}, {'text': "Промяна на обществото", 'is_correct': False}]},
# #     {'question': "Какъв е мотивът в стихотворението „Обесването на Васил Левски“ на Христо Ботев?", 'answers': [{'text': "Жертва за свободата", 'is_correct': True}, {'text': "Радост от победата", 'is_correct': False}, {'text': "Борба за власт", 'is_correct': False}, {'text': "Мъка за родината", 'is_correct': False}]},
# # ]
# #
# # create_quiz("Литература 9 клас", "9", "Литература", "Куиз за литература 9 клас", questions_lit_9)
# #
# # # 10 клас - Литература
# # questions_lit_10 = [
# #     {'question': "Какъв е основният мотив в „Епопея на забравените“?", 'answers': [{'text': "Почит към героите", 'is_correct': True}, {'text': "Тема за любовта", 'is_correct': False}, {'text': "Борба за власт", 'is_correct': False}, {'text': "Човешки слабости", 'is_correct': False}]},
# #     {'question': "Какъв е мотивът в „Под игото“ на Иван Вазов?", 'answers': [{'text': "Борба за независимост", 'is_correct': True}, {'text': "Конфликт с чуждестранни сили", 'is_correct': False}, {'text': "Драма за личната съдба", 'is_correct': False}, {'text': "Нравствени дилеми", 'is_correct': False}]},
# #     {'question': "Какво описва „Гераците“ на Елин Пелин?", 'answers': [{'text': "Феодалните отношения в България", 'is_correct': False}, {'text': "Семейни конфликти", 'is_correct': True}, {'text': "Социалната изолация", 'is_correct': False}, {'text': "История на България", 'is_correct': False}]},
# #     {'question': "Какво разглежда стихотворението „Арменци“ на Пейо Яворов?", 'answers': [{'text': "Тема за войната", 'is_correct': True}, {'text': "Тема за любовта", 'is_correct': False}, {'text': "Проблеми в семейството", 'is_correct': False}, {'text': "Социални конфликти", 'is_correct': False}]},
# #     {'question': "Каква е основната тема на „Тютюн“ от Димитър Димов?", 'answers': [{'text': "Герои в социални мрежи", 'is_correct': False}, {'text': "Живот и съвременни проблеми", 'is_correct': True}, {'text': "Политическа борба", 'is_correct': False}, {'text': "Проблеми на социализма", 'is_correct': False}]},
# #     {'question': "Какъв е стилът в „Индже“ на Йордан Йовков?", 'answers': [{'text': "Реализъм", 'is_correct': True}, {'text': "Романтизъм", 'is_correct': False}, {'text': "Модернизъм", 'is_correct': False}, {'text': "Импресионизъм", 'is_correct': False}]},
# #     {'question': "Какъв е мотивът в стихотворението „Зимни вечери“ на Христо Смирненски?", 'answers': [{'text': "Природата и самотата", 'is_correct': True}, {'text': "Семейни отношения", 'is_correct': False}, {'text': "Тема за войната", 'is_correct': False}, {'text': "Образът на революцията", 'is_correct': False}]},
# #     {'question': "Какво е общото между „Железният светилник“ и „Под игото“?", 'answers': [{'text': "Борбата за независимост", 'is_correct': True}, {'text': "История на личността", 'is_correct': False}, {'text': "Темата за социалната несправедливост", 'is_correct': False}, {'text': "Семейни проблеми", 'is_correct': False}]},
# #     {'question': "Какъв е основният конфликт в „Странник“ на Христо Ботев?", 'answers': [{'text': "Конфликт между личността и обществото", 'is_correct': True}, {'text': "Конфликт в семейството", 'is_correct': False}, {'text': "Тема за революцията", 'is_correct': False}, {'text': "Борба със социализма", 'is_correct': False}]},
# #     {'question': "Какъв е темата в разказите на Йордан Йовков?", 'answers': [{'text': "Състояния на отчаяние и самота", 'is_correct': False}, {'text': "Социалните дилеми на обикновения човек", 'is_correct': True}, {'text': "Революция и война", 'is_correct': False}, {'text': "Духовните терзания на героите", 'is_correct': False}]},
# # ]
# #
# # create_quiz("Литература 10 клас", "10", "Литература", "Куиз за литература 10 клас", questions_lit_10)
# #
# # # Добав
# #
# #
# # # 11 клас - Литература
# # questions_lit_11 = [
# #     {'question': "Какво е основното послание на „На прощаване“ от Гео Милев?", 'answers': [{'text': "Поглед върху миналото и съжаление", 'is_correct': False}, {'text': "Темата за социалната революция", 'is_correct': True}, {'text': "Отношенията между хората", 'is_correct': False}, {'text': "Философски разсъждения за живота", 'is_correct': False}]},
# #     {'question': "Каква е основната тема в „Поетът“ от Пейо Яворов?", 'answers': [{'text': "Саможертвата на поета", 'is_correct': True}, {'text': "Тема за революцията", 'is_correct': False}, {'text': "Трудностите в обществото", 'is_correct': False}, {'text': "Любовта към родината", 'is_correct': False}]},
# #     {'question': "Какво представлява стилът на Атанас Далчев?", 'answers': [{'text': "Символизъм и абсурдизъм", 'is_correct': False}, {'text': "Модернизъм и експресионизъм", 'is_correct': True}, {'text': "Класически реализъм", 'is_correct': False}, {'text': "Социален реализъм", 'is_correct': False}]},
# #     {'question': "Какъв е основният въпрос в „Слепи” на Гео Милев?", 'answers': [{'text': "Тема за човешката слепота и несправедливостта", 'is_correct': True}, {'text': "Тема за любовта", 'is_correct': False}, {'text': "Тема за човешката изолация", 'is_correct': False}, {'text': "Възход на обществото", 'is_correct': False}]},
# #     {'question': "Какво означава терминът „автобиография”?", 'answers': [{'text': "История на историята", 'is_correct': False}, {'text': "Автобиографичен разказ за автора", 'is_correct': True}, {'text': "Разказ за други личности", 'is_correct': False}, {'text': "Митологично предание", 'is_correct': False}]},
# #     {'question': "Какъв е мотивът в стихотворението „Заточеници“ на Гео Милев?", 'answers': [{'text': "Тема за саможертвата и борбата", 'is_correct': True}, {'text': "Тема за победата", 'is_correct': False}, {'text': "Радостта от живота", 'is_correct': False}, {'text': "История на личността", 'is_correct': False}]},
# #     {'question': "Какво разглеждат „Белите гълъби“ на Гео Милев?", 'answers': [{'text': "Нравствени конфликти", 'is_correct': False}, {'text': "Тема за любовта", 'is_correct': False}, {'text': "Социални проблеми", 'is_correct': True}, {'text': "Проблеми в обществото", 'is_correct': False}]},
# #     {'question': "Какъв е основният конфликт в произведенията на Елин Пелин?", 'answers': [{'text': "Социални конфликти", 'is_correct': True}, {'text': "Борба за любов", 'is_correct': False}, {'text': "Тема за семейния живот", 'is_correct': False}, {'text': "Социална изолация", 'is_correct': False}]},
# #     {'question': "Какво представлява поезията на Христо Ботев?", 'answers': [{'text': "Възхвала на народните герои", 'is_correct': False}, {'text': "Борба за социални и политически права", 'is_correct': True}, {'text': "Тема за личната трагедия", 'is_correct': False}, {'text': "Реализъм и обикновените хора", 'is_correct': False}]},
# #     {'question': "Какво е основното послание на „Бай Ганьо“ от Алеко Константинов?", 'answers': [{'text': "Критика към обществените нагласи", 'is_correct': True}, {'text': "Героизмът на българския народ", 'is_correct': False}, {'text': "Тема за личността", 'is_correct': False}, {'text': "Възхвала на демокрацията", 'is_correct': False}]},
# # ]
# #
# # create_quiz("Литература 11 клас", "11", "Литература", "Куиз за литература 11 клас", questions_lit_11)
# #
# # # 12 клас - Литература
# # questions_lit_12 = [
# #     {'question': "Какъв е основният мотив в стихотворението „Осъдени души“ на Гео Милев?", 'answers': [{'text': "Революционен дух", 'is_correct': True}, {'text': "Природата и човешката изолация", 'is_correct': False}, {'text': "Мечти за бъдещето", 'is_correct': False}, {'text': "Героизма на народа", 'is_correct': False}]},
# #     {'question': "Какво описва романът „Под игото“?", 'answers': [{'text': "Революционния дух на българите", 'is_correct': True}, {'text': "Образът на роба", 'is_correct': False}, {'text': "Герой и революционер", 'is_correct': False}, {'text': "Мисия за освобождение", 'is_correct': False}]},
# #     {'question': "Какъв е основният конфликт в романа „Железният светилник“?", 'answers': [{'text': "Конфликт между личността и обществото", 'is_correct': True}, {'text': "Конфликт между вярата и съмнението", 'is_correct': False}, {'text': "Конфликт между култури", 'is_correct': False}, {'text': "Любовен конфликт", 'is_correct': False}]},
# #     {'question': "Какво е централно в стихотворението „Аз съм българче“?", 'answers': [{'text': "Любовта към Родината", 'is_correct': True}, {'text': "Семейни отношения", 'is_correct': False}, {'text': "Песимизмът и бъдещето", 'is_correct': False}, {'text': "Тема за личната трагедия", 'is_correct': False}]},
# #     {'question': "Какво разглежда поезията на Димчо Дебелянов?", 'answers': [{'text': "Човешката самота и отчаяние", 'is_correct': True}, {'text': "Тема за любовта", 'is_correct': False}, {'text': "Философски разсъждения", 'is_correct': False}, {'text': "Героизмът и революцията", 'is_correct': False}]},
# #     {'question': "Какво разглежда разказът „Няма място за него“ от Елин Пелин?", 'answers': [{'text': "Живота на селянина", 'is_correct': True}, {'text': "Социалната несправедливост", 'is_correct': False}, {'text': "Борба за власт", 'is_correct': False}, {'text': "Взаимопомощта между хората", 'is_correct': False}]},
# #     {'question': "Какъв е мотивът в стихотворението „Заточеници“?", 'answers': [{'text': "Жертвата за родината", 'is_correct': True}, {'text': "Борба за любовта", 'is_correct': False}, {'text': "Радостта от живота", 'is_correct': False}, {'text': "Образът на революцията", 'is_correct': False}]},
# #     {'question': "Какво изразява философията в стихотворението „Сънят на моето детство“?", 'answers': [{'text': "Вярата в бъдещето", 'is_correct': True}, {'text': "Самотата на човека", 'is_correct': False}, {'text': "Борбата със социалните проблеми", 'is_correct': False}, {'text': "Тема за любовта", 'is_correct': False}]},
# #     {'question': "Какво е основното послание на „Бай Ганьо“?", 'answers': [{'text': "Критика на моралните проблеми на българите", 'is_correct': True}, {'text': "Героизма на народа", 'is_correct': False}, {'text': "Възхвала на личността", 'is_correct': False}, {'text': "Тема за социализма", 'is_correct': False}]},
# #     {'question': "Каква е символиката на образа на Левски в „Бай Ганьо“?", 'answers': [{'text': "Неговият героизъм и жертва", 'is_correct': True}, {'text': "Съпротивата срещу чуждото влияние", 'is_correct': False}, {'text': "Борба за личната свобода", 'is_correct': False}, {'text': "Разочарование от революцията", 'is_correct': False}]},
# # ]
# #
# # create_quiz("Литература 12 клас", "12", "Литература", "Куиз за литература 12 клас", questions_lit_12)

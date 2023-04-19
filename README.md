# Задание

**FHIR** - стандарт, описывающий объекты в области медицины в виде ресурсов. В задаче будут использованы 3 типа:

- **Bundle** - служебный ресурс для обмена коллекциями ресурсов http://hl7.org/fhir/R4/bundle.html
- **Patient** - содержит информацию о пациенте (http://hl7.org/fhir/patient.html);
- **Appointment** - определяет запись пациента на прием к врачу (http://hl7.org/fhir/appointment.html);

Необходимо реализовать endpoint, который принимал бы на вход ресурс `Bundle`, в котором
в поле `Bundle.entry` находился бы список ресурсов `Appointment`. Для примера можно использовать результаты выдачи
https://hapi.fhir.org/baseR4/Appointment?_count=10

Для каждого `Appointment` в `Bundle`, для каждого участника (`Appointment.participant[].actor`)
если заполнен атрибут `reference` и он ссылается на пациента (начинается на `Patient/`) сделать GET
(адрес должен быть конфигурируемым), и  получить этого пациента (для тестирования можно использовать
https://hapi.fhir.org/baseR4).

Используя полученного пациента актуализировать значение `display` в `Appointment.participant[].actor`
приведя его к виду "Фамилия И".

По результатам обработки всех `Bundle.entry`, endpoint должен вернуть модифицированный `Bundle` в ответе.

Считается, что все входные данные являются валидными с точки зрения FHIR, но не все поля могут быть заполнены.

Предпочтительный стэк технологий: `cherrypy`, `requests`.


## Инструкция

#### Шаг 1. Клонировать репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/FHIR.git
```
#### Шаг 2. Установить все зависимости
```bash
   pip install -r requirements.txt   
```
#### Шаг 3. Запустить app.py 
```bash
   python app.py
```
## Примеры
Для формирования запросов и ответов использована программа [Postman](https://www.postman.com/).

### Делаем запрос 
```json
    POST http://127.0.0.1:8080/
```
# Body(json) ставим данные из [https://hapi.fhir.org](https://hapi.fhir.org/baseR4/Appointment?_count=10)

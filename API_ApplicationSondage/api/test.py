from Models import *
import requests, random, math, json, concurrent.futures, time
import threading


""" def alea() -> dict:
    query = requests.get("http://127.0.0.1:8000/getfood_groups")
    foods_groupes = query.json()
    group_name_fr = [foods_groupes["data"][i]["group_name_fr"] for i in range(len(foods_groupes["data"]))]
    random.shuffle(group_name_fr)
    pourcentages: dict = dict(zip(group_name_fr, ["" for _ in range(len(foods_groupes["data"]))]))
    pourcentages[list(pourcentages.keys())[0]] = random.randint(0, 100)
    pourcentages[list(pourcentages.keys())[1]] = random.randint(0, 100-pourcentages[list(pourcentages.keys())[0]])
    pourcentages[list(pourcentages.keys())[2]] = random.randint(0, 100-pourcentages[list(pourcentages.keys())[0]]-pourcentages[list(pourcentages.keys())[1]])
    pourcentages[list(pourcentages.keys())[3]] = random.randint(0, 100-pourcentages[list(pourcentages.keys())[0]]-pourcentages[list(pourcentages.keys())[1]]-pourcentages[list(pourcentages.keys())[2]])
    pourcentages[list(pourcentages.keys())[4]] = 100-pourcentages[list(pourcentages.keys())[0]]-pourcentages[list(pourcentages.keys())[1]]-pourcentages[list(pourcentages.keys())[2]]-pourcentages[list(pourcentages.keys())[3]]
    return pourcentages """


foods_groupes = requests.get("http://127.0.0.1:8000/getfood_groups").json()["data"]
group_name_fr = [foods_groupes[i]["group_name_fr"] for i in range(len(foods_groupes))]

req = lambda grpCode: requests.get(f"http://127.0.0.1:8000/getfoods?groupeCode={grpCode}").json()["data"]
keepOnlyAlimCode = lambda foodsByGroup: [foodsByGroup[i]["food_code"] for i in range(len(foodsByGroup))]
alimCodeByGroup = lambda grpCode: keepOnlyAlimCode(req(grpCode))
alimCodeByGroupDict = {}

def alea(group_name_fr: list) -> dict:
    random.shuffle(group_name_fr)
    n = len(group_name_fr)
    pourcentages = {group_name_fr[i]: 0 for i in range(n)}
    for i in range(n - 1):
        pourcentages[group_name_fr[i]] = random.randint(0, 100//n)
    pourcentages[group_name_fr[n - 1]] = 100 - sum(pourcentages.values())
    return pourcentages

def sort_dict(d: dict) -> dict:
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

def to_quantities(pourcentages: dict) -> dict:
    total_percentage = sum(pourcentages.values())
    total_quantity = 10
    quantities = {group: math.floor((percentage * total_quantity) / total_percentage) for group, percentage in pourcentages.items()}
    remaining_quantity = total_quantity - sum(quantities.values())
    sorted_groups = sorted(pourcentages, key=lambda x: pourcentages[x], reverse=True)
    for i in range(remaining_quantity):
        quantities[sorted_groups[i]] += 1
    return quantities

def to_foods(quantities: dict) -> dict:
    for group, quantity in quantities.items():
        group_code = [foods_groupes[i]["group_code"] for i in range(len(foods_groupes)) if foods_groupes[i]["group_name_fr"] == group][0]
        if group_code not in alimCodeByGroupDict:
            alimCodeByGroupDict[group_code] = alimCodeByGroup(group_code)
        random.shuffle(alimCodeByGroupDict[group_code])
        quantities[group] = alimCodeByGroupDict[group_code][:quantity]
    return quantities

def to_list(foods: dict) -> list:
    # Return a list of foods
    return [foods[group][i] for group in foods for i in range(len(foods[group]))]

#print(len(to_list(to_foods(to_quantities(sort_dict(alea(group_name_fr)))))))

def generate_survey(n: int) -> list:
    request: str = f"https://randomuser.me/api/?nat=fr&inc=name,location,dob,cell&results={n}"
    query: requests.Response = requests.get(request)
    data: dict = query.json()
    donnees_generees_survey: list = []
    for i in range(n):
        constituent: dict = {
                    "last_name": data["results"][i]["name"]["last"].upper(), 
                    "first_name": data["results"][i]["name"]["first"],
                    # reverse date to mysql format yyyy-mm-dd ex: 1993-07-14
                    "birth": "-".join("-".join(data["results"][i]["dob"]["date"].split("T")[0].split("-")[::-1]).split("-")[::-1]),
                    "address": f'{data["results"][i]["location"]["street"]["number"]}, {data["results"][i]["location"]["street"]["name"]}',
                    "codePostal": data["results"][i]["location"]["postcode"], 
                    "city": data["results"][i]["location"]["city"].upper(), 
                    "tel": "".join(data["results"][i]["cell"].split("-")),}
        donnees_generees_survey.append(constituent)
    return donnees_generees_survey


def register_constituent(constituent):
    constituent = json.dumps(constituent)
    query = requests.post("http://127.0.0.1:8000/registerconstituent", data=constituent)
    return query.json()["id"]

def registerconstituentsurveyToDB(survey: list) -> list[int]:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_constituent = {executor.submit(register_constituent, constituent): constituent for constituent in survey}
        for future in concurrent.futures.as_completed(future_to_constituent):
            try:
                constituent = future_to_constituent[future]
            except Exception as exc:
                print(f'{constituent} generated an exception: {exc}')

""" survey = generate_survey(5000)
survey2 = generate_survey(5000)
survey3 = generate_survey(5000)
survey4 = generate_survey(4990)
survey_list = [survey, survey2, survey3, survey4] """

#print(registerconstituentsurveyToDB(survey))

# Register multiple surveys to DB using threads concurrent 
# the function should take a list of surveys in parameter
def registersurveysToDBMultiple(survey_list: list) -> list[int]:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_survey = {executor.submit(registerconstituentsurveyToDB, survey): survey for survey in survey_list}
        for future in concurrent.futures.as_completed(future_to_survey):
            try:
                survey = future_to_survey[future]
            except Exception as exc:
                print(f'{survey} generated an exception: {exc}')

# Compute the time performance to register 20000 constituents to DB
""" start = time.time()
registersurveysToDBMultiple(survey_list)
end = time.time()
print(end - start) """

# Register survey answers to DB 
def register_answer(i, survey_answer):
    survey_answer = json.dumps(survey_answer)
    query = requests.post(f"http://127.0.0.1:8000/answersurvey?constituentId={i}", data=survey_answer)
    return query

def register_answers_to_db(begin, end):
    survey_answers = [to_list(to_foods(to_quantities(sort_dict(alea(group_name_fr))))) for _ in range(begin, end)]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # constituent ids start at 1
        future_to_survey_answer = {executor.submit(register_answer, i, survey_answer): survey_answer for i, survey_answer in zip(range(begin, end), survey_answers)}
        for future in concurrent.futures.as_completed(future_to_survey_answer):
            try:
                survey_answer = future_to_survey_answer[future]
            except Exception as exc:
                print(f'{survey_answer} generated an exception: {exc}')

print(register_answers_to_db(30_000, 30_001))
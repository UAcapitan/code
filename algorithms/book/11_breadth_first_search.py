from collections import deque

friends = {
    "you": ["Andry", "Peter", "Mike"],
    "Andry": [],
    "Peter": ["Nick", "Olga", "Semen"],
    "Mike": ["Andrey", "Yan"],
    "Nick": ["Yan"],
    "Olga": ["Ira"],
    "Semen": [],
    "Andrey": ["Vladislav"],
    "Ira": ["Yan"],
    "Vladislav": ["Yan"],
    "Yan": ["Mike", "Nick","Vladislav"],
}

def is_it_needed_person(name):
    if len(name) >= 7:
        return True
    return False

social = deque()
social += friends["you"]
checked = []

def breadth_first_search():
    global social, friends
    while social:
        name = social.popleft()
        if name not in checked:
            if is_it_needed_person(name):
                print(f"{name} is that person.")
                return True
            else:
                checked.append(name)
                social += friends[name]
    print("There is no needed person")
    return False

breadth_first_search()


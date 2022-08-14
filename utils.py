import json


def load_candidates(file_):
    '''Загружает данные из файла, возвращает список кандидатов'''
    with open(file_, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_candidate(candidate_id, candidates_list):
    '''Возвращает кандидата по pk'''
    for candidate in candidates_list:
        if candidate["id"] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidate_name, candidates_list):
    '''Возвращает кандидатов по имени'''
    suitable_candidates = []
    for candidate in candidates_list:
        if candidate_name.lower() in candidate["name"].lower():
            suitable_candidates.append(candidate)
    return suitable_candidates


def get_by_skill(skill_name, candidates_list):
    '''Возвращает кандидатов по навыку'''
    suitable_candidates = []
    for candidate in candidates_list:
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            suitable_candidates.append(candidate)
    return suitable_candidates

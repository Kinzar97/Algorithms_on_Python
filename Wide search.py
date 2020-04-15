from collections import deque #deque - функция для создания двусторонней очереди (дека)
def search(name): #поиск в ширину Сложность O(V+E), где V - кол-во вершин, E - кол-во ребер
    search_queue = deque()
    search_queue += graph[name]
    searched = [] #список используется для остлеживания уже проверенных людей
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(person): #проверка на продавца манго
    if person[0] == 'M':
        return True

graph = {} #реализация структуры графа
graph['You'] = ['Nikita', 'Ilya', 'Aleksey']
graph['Nikita'] = ['Alexandr', 'Vlada']
graph['Ilya'] = ['Dasha', 'Masha']
graph['Aleksey'] = []
graph['Alexandr'] = []
graph['Vlada'] = []
graph['Dasha'] = []
graph['Masha'] = []

search('You')

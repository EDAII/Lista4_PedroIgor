import copy
all_max_heap = []
def build_max_heap(lista):
    i = 1
    change = False
    while i < len(lista):
        pos = i-1
        if i*2 < len(lista) and (i*2)-1<len(lista):
            #print('comp: pai = '+str(lista[pos])+'filhos: '+str(lista[i*2])+' e '+str(lista[(i*2)-1]))
            if lista[pos] < lista[i*2] or lista[pos] < lista[(i*2)-1]:
                change = True
                if lista[i*2] > lista[(i*2)-1]:
                    lista[i*2], lista[pos] = lista[pos], lista[i*2]
                else:
                    lista[(i*2)-1], lista[pos] = lista[pos], lista[(i*2)-1]
        elif (i*2)-1<len(lista):
            #print('comp: pai = '+str(lista[pos])+'filho: '+str(lista[(i*2)-1]))
            if lista[(i*2)-1] > lista[pos]:
                change = True
                lista[(i*2)-1], lista[pos] = lista[pos], lista[(i*2)-1]

        i+=1
    if change:
        if lista not in all_max_heap:
            all_max_heap.append(copy.copy(lista))
        return build_max_heap(lista)

    return lista

def heap_sort(heap, s_lista, all_s_lista):
    heap = build_max_heap(heap)
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    s_lista = [heap[len(heap)-1]]+s_lista
    heap.remove(heap[len(heap)-1])
    if len(heap) == 1:
        s_lista = [heap[0]]+s_lista
        return s_lista, all_max_heap, all_s_lista
    all_s_lista.append(copy.copy(s_lista))
    return heap_sort(heap, s_lista, all_s_lista)
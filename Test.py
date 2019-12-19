from timeit import default_timer as timer
from InsertionSort import insertion_sort
from GenerateLists import copy_list
from GenerateLists import random_list
from MergeSort import Merge_Sort



def test(n):
    print "Tempi ordinamento vettore di" , n , "elementi random :"

    #CASO MEDIO (ARRAY RANDOM)

    list1 = random_list(n)
    list2 = copy_list(list1)

    #print "Vettore random da ordinare : ",list1

    start = timer()
    insertion_sort(list1)
    end = timer()
    print " - Tempo impiegato da InsertionSort :" , (end - start) , " secondi"

    start = timer()
    Merge_Sort(list2,0,n-1)
    end = timer()
    print " - Tempo impiegato da MergeSort     :" , (end - start) , " secondi"

    #CASO MIGLIORE (ARRAY ORDINATO)
    print "Tempi ordinamento vettore ordinato :"

    start = timer()
    insertion_sort(list1)
    end = timer()
    print " - InsertionSort :" , (end - start) , " secondi"

    start = timer()
    Merge_Sort(list2,0,n-1)
    end = timer()
    print " - MergeSort     :" , (end - start) , " secondi"

    #CASO PEGGIORE (ARRAY ORDINATO AL CONTRARIO)
    print "Tempi ordinamento vettore ordinato al contrario :"

    list1.reverse()
    list4 = copy_list(list1)

    start = timer()
    insertion_sort(list1)
    end = timer()
    print " - InsertionSort :", (end - start) , " secondi"

    start = timer()
    Merge_Sort(list4,0,n-1)
    end = timer()
    print " - MergeSort     :" , (end - start) , " secondi"


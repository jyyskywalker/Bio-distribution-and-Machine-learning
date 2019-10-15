import numpy.matlib
import numpy as np
import pandas
import pandas as pd
from math import pow
seq1 = "AACCGTC"
seq2 = "AACGTTC"
seq_matrix = np.matlib.zeros((len(seq1)+1,len(seq2)+1))

def print_seq_matrix():
    index_list=list(map(lambda x:str(x+1)+"-"+seq1[x], range(0,len(seq1))))
    columns_list=list(map(lambda x:str(x+1)+"-"+seq2[x], range(0,len(seq2))))
    index_list.insert(0,"-")
    columns_list.insert(0,"-")
    seq_frame = pandas.DataFrame(seq_matrix,index=index_list, columns=columns_list)
    display(seq_frame)

print_seq_matrix()

for  i in range(0,len(seq1)+1):
    seq_matrix[i,0] = -i
for  j in range(0,len(seq2)+1):
    seq_matrix[0,j] = -j

print_seq_matrix()
mark_matrix = np.matlib.zeros((len(seq1),len(seq2)))

#使用递归改写的计算值的版本，但是这个运行起来会比循环版本慢许多
def matrix_cal(n,m):
    if(n!=0 and m!=0):
        if seq1[n-1]==seq2[m-1]:
            count=np.array([matrix_cal(n-1, m)-1, matrix_cal(n-1, m-1)+1, matrix_cal(n, m-1)-1])
            seq_matrix[n,m] = count.max()
            count=(count==seq_matrix[n,m]).astype(int)
            for i in range(0,3):
                mark_matrix[n-1,m-1]+=count[i]*2**i
            return seq_matrix[n,m]
        else:
            count=[matrix_cal(n-1, j)-1, matrix_cal(n-1, m-1)-1, matrix_cal(n, m-1)-1]
            seq_matrix[n,m] = max(count)
            return seq_matrix[n,m]
    else:
        return seq_matrix[n,m]

matrix_cal(len(seq1),len(seq2))
print_seq_matrix()

#解析函数，将mark_matrix中的数解析为方向，同时可以实现多种结果
aligned_seqs = ["", ""]
arr_i, arr_j = len(seq1)-1, len(seq2)-1

def print_seq(n,m):
    if n==arr_i and m==arr_j:    
        print(aligned_seqs[0])
        print(aligned_seqs[1])


def print_matrix(n,m):
    if n>0 and m>0:
        
        print_seq(n,m)
    else:
        return 
        


def line(n,m):
    if n>=1 and m>=1:
        arr0=line(n-1,m-1)
        arr1=line(n,m-1)
        arr2=line(n-1,m)
    elif n==0 and m>=1:
        arr0=["",""]
        arr1=line(n,m-1)
        arr2=["",""]
    else:
        arr0=["",""]
        arr1=["",""]
        arr2=line(n-1,m)
    
    if ori_matrix[n,m] == 0:
        aligned_seqs[0] = arr0[0]+seq1[n]
        aligned_seqs[1] = arr0[1]+seq2[m]
    elif ori_matrix[n,m] == 1:
        aligned_seqs[0] = arr1[0]+"-"
        aligned_seqs[1] = arr1[1]+seq2[m]
    else:
        aligned_seqs[0] = arr2[0]+seq1[n]
        aligned_seqs[1] = arr2[1]+"-"
    return aligned_seqs

line(arr_i,arr_j)

print(aligned_seqs[0])
print(aligned_seqs[1])
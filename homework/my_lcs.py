import numpy.matlib
import numpy as np
import pandas
import pandas as pd
from math import pow
seq1 = "AACCGTC"
seq2 = "AACGTTC"
seq_matrix = np.matlib.zeros((len(seq1)+1,len(seq2)+1))
mark_matrix = np.matlib.zeros((len(seq1),len(seq2)))

def print_seq_matrix():
    index_list=list(map(lambda x:str(x+1)+"-"+seq1[x], range(0,len(seq1))))
    columns_list=list(map(lambda x:str(x+1)+"-"+seq2[x], range(0,len(seq2))))
    index_list.insert(0,"-")
    columns_list.insert(0,"-")
    seq_frame = pandas.DataFrame(seq_matrix,index=index_list, columns=columns_list)
    display(seq_frame)

print_seq_matrix()

def print_mark_matrix():
    index_list=list(map(lambda x:str(x)+"-"+seq1[x], range(0,len(seq1))))
    columns_list=list(map(lambda x:str(x)+"-"+seq2[x], range(0,len(seq2))))
    ori_frame = pandas.DataFrame(mark_matrix,index=index_list, columns=columns_list)
    display(ori_frame)

for  i in range(0,len(seq1)+1):
    seq_matrix[i,0] = -i
for  j in range(0,len(seq2)+1):
    seq_matrix[0,j] = -j

print_seq_matrix()

#使用递归改写的计算矩阵值的版本，但是这个运行起来会比循环版本慢许多
def matrix_cal(n,m):
    if(n!=0 and m!=0):
        if seq1[n-1]==seq2[m-1]:
            count=np.array([matrix_cal(n-1, m)-1, matrix_cal(n-1, m-1)+1, matrix_cal(n, m-1)-1])
            seq_matrix[n,m] = count.max()
            count=(count==seq_matrix[n,m]).astype(int)
            if mark_matrix[n-1,m-1]==0:
                for i in range(0,3):
                    mark_matrix[n-1,m-1]+=count[i]*(2**i)
            return seq_matrix[n,m]
        else:
            count=np.array([matrix_cal(n-1, j)-1, matrix_cal(n-1, m-1)-1, matrix_cal(n, m-1)-1])
            seq_matrix[n,m] = count.max()
            count=(count==seq_matrix[n,m]).astype(int)
            if mark_matrix[n-1,m-1]==0:
                for i in range(0,3):
                    mark_matrix[n-1,m-1]+=count[i]*(2**i)
            return seq_matrix[n,m]
    else:
        return seq_matrix[n,m]

matrix_cal(len(seq1),len(seq2))
print_seq_matrix()
print_mark_matrix()

#解析函数，将mark_matrix中的数解析为方向，同时可以实现多种结果
arr_i, arr_j = len(seq1)-1, len(seq2)-1

aligned_seqs=["",""]
def cal_sequence(n, m, s=["",""]):
    aligned_seqs=s
    if n>=0 or m>=0:
        if mark_matrix[n,m]==1:
            aligned_seqs[0]=seq1[n]+aligned_seqs[0]
            aligned_seqs[1]='-'+aligned_seqs[1]
            cal_sequence(n-1,m,aligned_seqs)
        elif mark_matrix[n,m]==2:
            aligned_seqs[0]=seq1[n]+aligned_seqs[0]
            aligned_seqs[1]=seq2[m]+aligned_seqs[1]
            cal_sequence(n-1, m-1, aligned_seqs)
        elif mark_matrix[n,m]==4:
            aligned_seqs[0]='-'+aligned_seqs[0]
            aligned_seqs[1]=seq2[m]+aligned_seqs[1]
            cal_sequence(n,m-1,aligned_seqs)
        elif mark_matrix[n,m]==3:
            aligned_seqs_temp=aligned_seqs
            aligned_seqs[0]=seq1[n]+aligned_seqs[0]
            aligned_seqs[1]='-'+aligned_seqs[1]
            cal_sequence(n-1,m,aligned_seqs)
            aligned_seqs_temp[0]=seq1[n]+aligned_seqs_temp[0]
            aligned_seqs_temp[1]=seq2[m]+aligned_seqs_temp[1]
            cal_sequence(n-1,m-1,aligned_seqs_temp)
        elif mark_matrix[n,m]==5:
            aligned_seqs_temp=aligned_seqs
            aligned_seqs[0]=seq1[n]+aligned_seqs[0]
            aligned_seqs[1]='-'+aligned_seqs[1]
            cal_sequence(n-1,m,aligned_seqs)
            aligned_seqs_temp[0]='-'+aligned_seqs_temp[0]
            aligned_seqs_temp[1]=seq2[m]+aligned_seqs_temp[1]
            cal_sequence(n,m-1,aligned_seqs_temp) 
        elif mark_matrix[n,m]==6:
            aligned_seqs_temp=aligned_seqs
            aligned_seqs[0]=seq1[n]+aligned_seqs[0]
            aligned_seqs[1]=seq2[m]+aligned_seqs[1]
            cal_sequence( n-1, m-1, aligned_seqs)                         
            aligned_seqs_temp[0]='-'+aligned_seqs_temp[0]
            aligned_seqs_temp[1]=seq2[m]+aligned_seqs_temp[1]
            cal_sequence(n,m-1,aligned_seqs_temp)
    else:
        print(aligned_seqs[0])
        print(aligned_seqs[1])
        print("\n")

cal_sequence(arr_i,arr_j,aligned_seqs)
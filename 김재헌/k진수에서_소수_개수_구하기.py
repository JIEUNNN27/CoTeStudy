# -*- coding: utf-8 -*-
"""K진수에서 소수 개수 구하기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQjQYSkEdUCPFeqeUPdPsDXcMPPH6WUM
"""

def isPrime(N):
    if N == 1: return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0: return False
    return True
# 출처: https://jjujju31.tistory.com/46 [현재를 가치있게 쓰자:티스토리]

def solution(n, k):
    answer = 0
    num=''
    while n>0:
        num+=str(n%k)
        n//=k
    num=num[::-1]
    for i in list(num.split('0')):
        if i!='':
            if isPrime(int(i)):
                answer+=1
    return answer
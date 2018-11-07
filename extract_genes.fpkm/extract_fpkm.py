#usr/bin/env python
#-*- coding=utf-8 -*-

with open('result.txt','w') as f2:
    with open('genes.fpkm_tracking') as f1:
        for line_1 in f1:
            l1=line_1.strip().split('\t')
            if  not l1[0]=='-':
                f2.write(l1[0])
                for i in range(9,len(l1),4):
                    f2.write('\t'+l1[i])
                f2.write('\n')
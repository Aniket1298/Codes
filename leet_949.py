import itertools
class Solution(object):
    def largestTimeFromDigits(self, A):
        l=list(itertools.permutations(A))
        h,m=-1,-1
        for x in l:
            a,b=x[0]*10+x[1],x[2]*10+x[3]
            if a<24 and b<60:
                if a>h:
                    h=a
                    m=b
                elif a==h:
                    if b>m:
                        m=b
        if h!=-1 and m!=-1:
            h,m=str(h),str(m)
            if len(h)==1:
                h='0'+h
            if len(m)==1:
                m='0'+m
            return h+":"+m
        else:
            return ""
            
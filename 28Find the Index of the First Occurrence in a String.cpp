#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    int* getNext(string ps){
        int len = ps.size();
        int* next;
        next = new int[len];

        int k = -1;
        int j = 0;
        next[0] = -1;
        while (j < len -1)
        {
            if(k == -1 || ps[j] == ps[k])
            {
                if(ps[++j] == ps[++k])
                {
                    next[j] = next[k];
                }
                else
                {
                    next[j] = k;
                }
            }
            else
            {
                k = next[k];
            }
        }
        return next;
    }

    int strStr(string haystack, string needle) {
        int hasize = haystack.size();
        int nesize = needle.size();

        if(nesize == 0)
        {
            return 0;
        }

        int* next = getNext(needle);

        int i = 0;
        int j = 0;
        while (i < hasize)
        {
            if(haystack[i] == needle[j])
            {
                if(j == nesize - 1)
                {
                    return i - nesize + 1;
                }
                j++;
                i++;
            }   
            else
            {
                j = next[j];
                if (j == -1)
                {
                    i++;
                    j++;
                }
            }
        }
        return -1;
    }

};
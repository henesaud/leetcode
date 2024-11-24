from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        #Array with index <i> and a value <c>,
        #where c is the number of papers with exact i citations,
        #except for the last position, which has >= i citations.
        papers_count =[0]*(n+1)

        #population the array
        for c in citations:
            papers_count[min(c, n)] += 1

        #Starting from the end
        h = n
        papers = papers_count[n]

        #Check the highest <h>
        while papers < h :
            h-=1
            papers += papers_count[h]

        return h

class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        def permute0(listy):
            if len(listy) == 1:
                return([[listy[0]]])
            else:
                al_listy = []
                for j_in_listy in listy:
                    n_listy = [j_in_listy]
                    listy0 = listy[:]
                    listy0.remove(j_in_listy)
                    for k_in_listyf in permute0(listy0):
                        for k_in_listy in k_in_listyf:
                            n_listy.append(k_in_listy)
                        al_listy.append(n_listy)
                        n_listy = [j_in_listy]
                return(al_listy)


        return(permute0(nums))
from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        valid_genes = set(bank)

        if startGene == endGene:
            return 0

        if endGene not in valid_genes:
            return -1

        queue = deque([(startGene, 0)])
        valid_genes.discard(startGene)

        while queue:
            current_gene, mutations = queue.popleft()

            for i in range(8):
                for letter in "ACGT":
                    if letter == current_gene[i]:
                        continue

                    next_gene = (
                        current_gene[:i] +
                        letter +
                        current_gene[i + 1:]
                    )

                    if next_gene == endGene:
                        return mutations + 1

                    if next_gene in valid_genes:
                        valid_genes.remove(next_gene)
                        queue.append((next_gene, mutations + 1))

        return -1
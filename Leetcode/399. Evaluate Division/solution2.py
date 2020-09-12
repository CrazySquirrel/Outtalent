from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        results = defaultdict(int)
        variables = defaultdict(lambda: defaultdict(list))

        for equation, value in zip(equations, values):
            results[tuple(equation)] = value
            results[tuple(equation[::-1])] = 1 / value

            variables[equation[0]][equation[1]] = [value, equation[1]]
            variables[equation[1]][equation[0]] = [1 / value, equation[0]]

        while True:
            relative_variables = defaultdict(lambda: defaultdict(list))

            for v1 in variables:
                for v2 in variables[v1]:
                    for v3 in variables[v2]:
                        if v3 == v1 or v3 in variables[v1]: continue
                        relative_variables[v1][v3] = [variables[v2][v3][0] * variables[v1][v2][0], v3]

            if not relative_variables: break

            for v1 in relative_variables:
                for v2 in relative_variables[v1]:
                    variables[v1][v2] = relative_variables[v1][v2]

        for v1 in variables:
            results[(v1, v1)] = 1

            for v2 in variables[v1]:
                results[(v1, v2)] = variables[v1][v2][0]

        return [results[tuple(query)] if tuple(query) in results else -1.0 for query in queries]

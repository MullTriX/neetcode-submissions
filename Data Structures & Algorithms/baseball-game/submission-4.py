class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for operation in operations:
            if operation == "+":
                records.append(records[-1] + records[-2])
                continue
            if operation == "C":
                records.remove(records[-1])
                continue
            if operation == "D":
                records.append(records[-1]*2)
                continue
            records.append(int(operation))
        return sum(records)

        
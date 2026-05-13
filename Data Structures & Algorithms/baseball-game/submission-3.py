class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for operation in operations:
            if operation == "+":
                records.append(records[-1] + records[-2])
            elif operation == "C":
                records.remove(records[-1])
            elif operation == "D":
                records.append(records[-1]*2)
            else:
                records.append(int(operation))
            print(records)
        return sum(records)

        
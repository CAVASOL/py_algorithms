class Solution:
    def reorderLogFiles(self, logs):
        def sorty(log):
            judge, cnt = log.split(" ", 1)
            return (0, cnt, judge) if cnt[0].isalpha() else (1,)

        l = []
        d = []

        for log in logs:
            if log.split()[1].isdigit():
                d.append(log)
            else:
                l.append(log)

        l.sort(key = sorty)

        return l + d
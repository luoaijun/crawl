# -*- coding: cp936 -*-
import re


class utils:
    def timeTrans(self, time):
        if "��" in time:
            result = int(re.findall(r"\d+\.?\d*", time)[0]) * 24 * 60 * 60
        elif "��" in time:
            result = int(re.findall(r"\d+\.?\d*", time)[0]) * 60
        else:
            result = time
        return result


if __name__ == '__main__':
    result = utils().timeTrans("1��")
    print(result)

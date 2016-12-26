#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""稍微有所改变和限制的K-SUM，要求是找到尽可能接近但不超过目标值的一个组合
而不是标准的刚好达到目标值的组合"""


class KsumSolution(object):
    """tar_val: 设定的目标值 tar_list:给予的待组合数列"""

    def __init__(self, tar_val, tar_list, limit=2):
        self.tar_val = tar_val
        self.tar_list = sorted(tar_list)
        self.limit = limit

    # 2-sum算法
    def two_sum_solution(self, two_tar, two_list):
        i = 0
        j = len(two_list) - 1
        record_list = [0]
        dif_val = two_tar - two_list[0]  # 差值记录

        while i < j:
            twosum = two_list[i] + two_list[j]
            if twosum == two_tar:
                record_list.clear()
                record_list.append(two_list[i])
                record_list.append(two_list[j])
                break
            elif twosum < two_tar:
                if dif_val > (two_tar - twosum):
                    record_list.clear()
                    record_list.append(two_list[i])
                    record_list.append(two_list[j])
                i += 1
            elif twosum > two_tar:
                j -= 1
        return record_list

    """逐个K值写法 太麻烦 就改成递归方式"""

    def three_sum_solution(self, three_tar, three_list):
        record_list = [0]
        dif_val = three_tar - three_list[0]  # 差值记录
        list_size = len(three_list)

        for index in range(list_size - 2):
            two_tar = three_tar - three_list[index]
            two_list = three_list[index + 1:]
            sub_list = self.two_sum_solution(two_tar, two_list)
            threesum = sum(sub_list, three_list[index])
            if threesum == three_tar:
                record_list.clear()
                record_list.append(three_list[index])
                record_list.extend(sub_list)
                break
            elif dif_val > (three_tar - threesum):
                dif_val = three_tar - threesum
                record_list.clear()
                record_list.append(three_list[index])
                record_list.extend(sub_list)

        return record_list

    """k >= 2时候的递归处理"""

    def k_sum_solution(self, k_tar, k_list, k_val):
        # K=2
        if k_val == 2:
            return self.two_sum_solution(k_tar, k_list)
        # K>2
        elif k_val > 2:
            record_list = [0]
            dif_val = k_tar - k_list[0]
            list_size = len(k_list)
            for i in range(list_size - k_val + 1):
                k_tmp = k_val - 1  # 下一层的K值
                sub_tar = k_tar - k_list[i]  # 下一层的目标值
                sub_match = self.k_sum_solution(sub_tar, k_list[i + 1:], k_tmp)  # 获得下一层的满足条件的组合
                tmp_sum = sum(sub_match, k_list[i])  # 获得当前层此次组合的和
                if tmp_sum == k_tar:
                    record_list.clear()
                    record_list.append(k_list[i])
                    record_list.extend(sub_match)
                    break
                elif dif_val > (k_tar - tmp_sum):
                    dif_val = k_tar - tmp_sum
                    record_list.clear()
                    record_list.append(k_list[i])
                    record_list.extend(sub_match)
            return record_list

    # 在简易判别之后 从2-SUM一直判别到K-sum,直到遇到第一个正好满足的组合
    # 或者遍历完成后取比目标值小的最接近值
    def get_match(self):
        dif_val = self.tar_val - self.tar_list[0]
        record_list = [0]
        if sum(self.tar_list) < self.tar_val:
            print(self.tar_list)
        else:
            for i in range(2,len(self.tar_list)):
                sub_match = self.k_sum_solution(self.tar_val,self.tar_list,i)
                sub_dif = self.tar_val - sum(sub_match)
                if sum(sub_match) == self.tar_val:
                    record_list.clear()
                    record_list.extend(sub_match)
                    break
                elif dif_val > sub_dif:
                    dif_val = sub_dif
                    record_list.clear()
                    record_list.extend(sub_match)
            print(record_list)



if __name__ == '__main__':
    numlist = [1, 3, 5, 7, 9, 11, 13, 15]
    tar_val = 30
    ksum = KsumSolution(tar_val, numlist)
    ksum.get_match()

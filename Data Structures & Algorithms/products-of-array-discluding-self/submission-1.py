class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        step_one = 1
        step_one_not_zero = 1
        number_zeros = 0
        result = []
        for number in nums:
            if number == 0:
                step_one *= number
                number_zeros += 1
            else:
                step_one_not_zero *= number

        for number in nums:
            if number == 0 and number_zeros == 1:
                final_number = int(step_one_not_zero)
            elif number == 0:
                final_number = int(step_one)
            elif number_zeros > 0:
                final_number = int(step_one / number)
            elif number_zeros == 0:
                final_number = int(step_one_not_zero / number)
            result.append(final_number)

        return result
def checksum(lst: list[int]) -> int:
    control_sum = 0

    for element in lst:
        control_sum+=element
        control_sum = (control_sum * 113) % 10000007
        
    return control_sum

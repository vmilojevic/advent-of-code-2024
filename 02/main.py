def load_reports(input_path):
    report_list = []
    input = open(input_path)

    for line in input:
        report = []
        split_line = line.split()
        for sl in split_line:
            report.append(int(sl))
        report_list.append(report)
    
    return report_list

def is_report_safe(report):
    if (len(report) < 2):
        return True
    
    factor = get_report_factor(report[0], report[1])
    for i in range(len(report) - 1):
        if not is_level_diff_safe(report[i], report[i + 1], factor):
            return False
    
    return True


def get_report_factor(left, right):
    if left == right:
        return 0
    else:
        return (left - right) / abs(left - right)

def is_level_diff_safe(left, right, factor):
    if (factor == 0):
        return False
    
    diff = left - right

    if (factor < 0):
        return diff < 0 and (abs(diff) >= 1 and abs(diff) <= 3)
    else:
        return diff > 0 and (abs(diff) >= 1 and abs(diff) <= 3)
    
# def is_dampened_report_safe(report):
#     if (len(report) < 2):
#         return True
    
#     dampened = False
#     factor = get_report_factor(report[0], report[1])
#     for i in range(len(report) - 1):
#         if (not is_level_diff_safe(report[i], report[i + 1], factor)):
#             if dampened:
#                 return False
#             else:
#                 dampened = True
#                 if (i + 2) >= len(report):
#                     return False
#                 else:
#                     if (not is_level_diff_safe(report[i], report[i + 2], factor)):
#                         return False
    
#     return True

if __name__ == "__main__":
    report_list = load_reports("input.txt")

    result = 0
    # result_dampened = 0
    for report in report_list:
        if (is_report_safe(report)):
            result = result + 1
        # if (is_dampened_report_safe(report)):
        #     result_dampened = result_dampened + 1
    
    print("Number of safe reports: " + str(result))
    # print("Number of safe reports with problem dampener: " + str(result_dampened))

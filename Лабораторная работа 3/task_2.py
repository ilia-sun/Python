def find_common_participants(first_group,second_group, separator=','):
    first_group = first_group.split(separator)
    second_group = second_group.split(separator)
    return sorted(set(first_group).intersection(set(second_group)))



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group, separator='|'))
# TODO Провеьте работу функции с разделителем отличным от запятой

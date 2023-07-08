from math import sqrt


# предполагается, что переданные точки образуют график функции, а не множество точек, т. е. одному значению х будет соответствовать только 1 значение у
# так же, до передачи точек в функцию, упорядочим их по возрастанию координаты х, это упростит алгоритм удаления бесполезных точек
# назовем точку b бесполезной, если она лежит на отрезке AC
def delete_useless_dots(list_of_dots):
    updated_list_of_dots = []
    updated_list_of_dots.append(list_of_dots[0])
    try:
        for i in range(1, len(list_of_dots) - 1):
            seg_i = Segment(list_of_dots[i - 1], list_of_dots[i + 1])
            if not (seg_i.is_this_dot_on_this_segment(list_of_dots[i])):
                updated_list_of_dots.append(list_of_dots[i])
    except:
        pass
    updated_list_of_dots.append(list_of_dots[-1])

    return updated_list_of_dots


def can_it_be_even(list_of_dots):
    sorted_list = sort_dots_by_x(list_of_dots)
    list_of_dots = delete_useless_dots(sorted_list)
    length = len(list_of_dots)
    middle_index = length // 2
    if length % 2 == 1:
        center = list_of_dots[middle_index]
        # print_list(list_of_dots)
        # print(center.x_cord, center.y_cord)
        new_list_of_dots = moving_the_coordinate_system(list_of_dots, center)
        return is_it_even(new_list_of_dots)
    else:
        left_center, right_center = (
            list_of_dots[middle_index - 1],
            list_of_dots[middle_index],
        )
        seg = Segment(left_center, right_center)
        true_center = seg.middle_of_this_segment()
        new_list_of_dots = moving_the_coordinate_system(list_of_dots, true_center)
        return is_it_even(new_list_of_dots)


def sort_dots_by_x(dots):
    sorted_dots = sorted(dots, key=lambda dot: dot.x_cord)
    return sorted_dots


def is_it_even(list_of_dots):
    new_list_of_dots = [
        dot for dot in list_of_dots if not (dot.x_cord == 0 and dot.y_cord == 0)
    ]

    for i in range(len(new_list_of_dots)):
        is_matching = False
        for j in range(len(new_list_of_dots)):
            if (
                new_list_of_dots[i].x_cord == -new_list_of_dots[j].x_cord
                and new_list_of_dots[i].y_cord == new_list_of_dots[j].y_cord
            ):
                is_matching = True
                break
        if not is_matching:
            return False

    return True


class Dot:
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y


def moving_the_coordinate_system(list_of_dots, dot_center: Dot):
    const_cord_of_center = (dot_center.x_cord, dot_center.y_cord)
    for i in range(len(list_of_dots)):
        list_of_dots[i].x_cord -= const_cord_of_center[0]
        list_of_dots[i].y_cord -= const_cord_of_center[1]
    return list_of_dots


class Segment:
    def __init__(self, dot_1: Dot, dot_2: Dot):
        self.begin = dot_1
        self.end = dot_2
        self.lenght_of_segment = lenght(dot_1, dot_2)

    def is_this_dot_on_this_segment(self, dot: Dot):
        lenght_1 = lenght(self.begin, dot)
        lenght_2 = lenght(self.end, dot)
        return self.lenght_of_segment == lenght_1 + lenght_2

    def is_this_segment_parallel_to_Ox(self):
        return self.begin.y_cord == self.end.y_cord

    def middle_of_this_segment(self):
        mid = Dot(0, 0)
        mid.x_cord = (self.begin.x_cord + self.end.x_cord) / 2
        mid.y_cord = (self.begin.y_cord + self.end.y_cord) / 2
        return mid


def lenght(dot_1, dot_2):
    return sqrt((dot_1.x_cord - dot_2.x_cord) ** 2 + (dot_1.y_cord - dot_2.y_cord) ** 2)


n = int(input("введиите количество точек "))
list_of_dots = []

for i in range(n):
    print(f"{i+1}-ая точка")
    x = int(input("Координата х "))
    y = int(input("Координата y "))
    list_of_dots.append(Dot(x, y))

print(can_it_be_even(list_of_dots))

def role_cube(x, pl):
    count = 0
    if pl == 1:
        for i in range(1, 32 + 1):
            for j in range(1, 32 + 1):
                for l in range(1, 32 + 1):
                    if i + j + l == x:
                        if ((i == 3)+(j == 3)+(l == 3)) >= 1:
                            count += 1
    else:
        for i in range(1, 32 + 1):
            for j in range(1, 32 + 1):
                for l in range(1, 32 + 1):
                    if i + j + l == x:
                        count += 1
    return count


print(role_cube(52, 0) - role_cube(38, 1))
# 675

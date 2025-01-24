def role_cube(x):
    count = 0
    for i in range(1, 32 + 1):
        for j in range(1, 32 + 1):
            for l in range(1, 32 + 1):
                if i + j + l == x:
                    count += 1
    return count


print(role_cube(17))
# Ответ 120

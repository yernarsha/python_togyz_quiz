import sqlite3

total = correct = 0
print("Welcome to the Togyz Kumalak Quiz!\n")

conn = sqlite3.connect('quiz.sqlite')
cursorObj = conn.cursor()
cursorObj.execute('SELECT * FROM fragen')

for row in cursorObj:
    print(f"{total+1}. {row[1]}:")
    print(f"1. {row[3]}")
    print(f"2. {row[4]}")
    print(f"3. {row[5]}")
    print(f"4. {row[6]}")

    answ = int(input())
    if answ == 0:
        break

    total += 1
    if answ == row[2]:
        correct += 1
        print(f'Correct! {correct} / {total}\n')
    else:
        print(f'Wrong... {correct} / {total}\n')


print(f'\nCorrect: {correct} / {total}')

cursorObj.close()
conn.close()

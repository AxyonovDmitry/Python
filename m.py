
def print_matr(mas):
	for j in mas:
		for i in j:
			print(i,end = " ")
		print()
def get_minor(mas,j,i):
	m = [[a for index,a in enumerate(h) if index != i - 1] for index_,h in enumerate(mas) if index_ != j - 1]
	return m
		
 
n = int(input("Введите порядок: "))
a = [[input(f"Введите a{j+1}{i+1} ") for i in range(n)]for j in range(n)]

print_matr(a)

for j in range(n):
	for i in range(n):
		m = get_minor(a,j+1,i+1)
		print(f"Минор {j+1}{i+1}: ")
		print_matr(m)
		print()

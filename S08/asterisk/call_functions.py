a = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(1, 2, 3, 4, 5, 6, 7, sep='---', end='\n\n')
kwargs = {'sep': '---', 'end': '\n\n'}
print(*a, **kwargs)

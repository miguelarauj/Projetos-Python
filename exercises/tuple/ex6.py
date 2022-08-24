words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in words:
    print(f'\nna palavra {c} temos',end=' ')
    for l in range(0,len(c)):
        if c[l] in 'bcdfghjklmnpqrstvwxyz':
            print(c[l],end=' ')

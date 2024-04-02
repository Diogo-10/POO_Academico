def quociente(a,b):
    return a//b

while True:
    x= int(input('x: '))
    y = int(input('y: '))
    q = quociente(x,y)
    try:
        print(f'{x} // {y} = {q}')
        
    except:
        print('Erro! divisão inválida')
    else:
        print('Divisão bem sucedida')
    finally:
        continuar = input('continuar (s/n)? ')
        if continuar == 'n': break

print('Até mais!')
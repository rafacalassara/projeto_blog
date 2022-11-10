from django import template

register = template.Library()

@register.filter(name='plural_comentario')
def plural_comentario(num_comentarios):
    saida = ''
    try:
        num_comentarios = int(num_comentarios)

        if num_comentarios == 0:
            saida = f'Sem comentários'
        elif num_comentarios == 1:
            saida = f'{num_comentarios} comentário'
        else:
            saida = f'{num_comentarios} comentários'
    except:
        return f'{num_comentarios} comentários(s)'
    return saida
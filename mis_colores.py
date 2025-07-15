# Clase de cores para o terminal
# Autor: Adrian C.
# Data: 14/07/2025

class Cores:
    # Reset
    RESET = '\033[0m'

    # Estilos de texto
    # NOTA: Algunos terminales no soportan todos los estilos o pueden interpretarlos diferente.
    NEGRITO = '\033[1m'      # O BRIGHT (brillante), a menudo lo mismo que negrita
    TENUE = '\033[2m'        # Dim, menos brillante
    ITALICO = '\033[3m'      # Itálico (no ampliamente soportado)
    SUBRAYADO = '\033[4m'    # Subrayado
    PARPADEO = '\033[5m'     # Blinking (molesto, a menudo no se usa)
    INVERTIR = '\033[7m'     # Invierte foreground y background
    OCULTO = '\033[8m'       # Hidden (invisible)
    TACHADO = '\033[9m'      # Strikethrough (no ampliamente soportado)

    # Restablecer estilos específicos (útil si solo quieres quitar uno)
    RESET_NEGRITO_TENUE = '\033[22m'
    RESET_ITALICO = '\033[23m'
    RESET_SUBRAYADO = '\033[24m'
    RESET_PARPADEO = '\033[25m'
    RESET_INVERTIR = '\033[27m'
    RESET_OCULTO = '\033[28m'
    RESET_TACHADO = '\033[29m'


    # Colores de texto (foreground) - Estándar / Oscuros
    PRETO = '\033[30m'       # Negro
    VERMELHO = '\033[31m'    # Rojo
    VERDE = '\033[32m'       # Verde
    AMARELO = '\033[33m'     # Amarillo
    AZUL = '\033[34m'        # Azul
    MAGENTA = '\033[35m'     # Magenta
    CIANO = '\033[36m'       # Ciano
    BRANCO = '\033[37m'      # Blanco
    
    # Restablecer color de texto (vuelve al color por defecto del terminal)
    RESET_FG = '\033[39m'


    # Colores de fondo (background) - Estándar / Oscuros
    FUNDO_PRETO = '\033[40m'       # Fondo negro
    FUNDO_VERMELHO = '\033[41m'    # Fondo rojo
    FUNDO_VERDE = '\033[42m'       # Fondo verde
    FUNDO_AMARELO = '\033[43m'     # Fondo amarillo
    FUNDO_AZUL = '\033[44m'        # Fondo azul
    FUNDO_MAGENTA = '\033[45m'     # Fondo magenta
    FUNDO_CIANO = '\033[46m'       # Fondo ciano
    FUNDO_BRANCO = '\033[47m'      # Fondo blanco

    # Restablecer color de fondo (vuelve al fondo por defecto del terminal)
    RESET_BG = '\033[49m'


    # Colores de texto (foreground) - Alta intensidad (Bright)
    VERMELHO_BRILHANTE = '\033[91m'  # Este es el que tenías como VERMELHO originalmente
    VERDE_BRILHANTE = '\033[92m'     # Este es el que tenías como VERDE originalmente
    AMARELO_BRILHANTE = '\033[93m'   # Este es el que tenías como AMARELO originalmente
    AZUL_BRILHANTE = '\033[94m'      # Este es el que tenías como AZUL originalmente
    MAGENTA_BRILHANTE = '\033[95m'   # Este es el que tenías como MAGENTA originalmente
    CIANO_BRILHANTE = '\033[96m'     # Este es el que tenías como CIANO originalmente
    BRANCO_BRILHANTE = '\033[97m'    # Este es el que tenías como BRANCO originalmente
    # Nota: También existen códigos para negro brillante (90m) pero a menudo es gris oscuro.


    # Colores de fondo (background) - Alta intensidad (Bright)
    FUNDO_VERMELHO_BRILHANTE = '\033[101m'
    FUNDO_VERDE_BRILHANTE = '\033[102m'
    FUNDO_AMARELO_BRILHANTE = '\033[103m'
    FUNDO_AZUL_BRILHANTE = '\033[104m'
    FUNDO_MAGENTA_BRILHANTE = '\033[105m'
    FUNDO_CIANO_BRILHANTE = '\033[106m'
    FUNDO_BRANCO_BRILHANTE = '\033[107m'
    # Nota: También existe 100m para fondo negro brillante (gris oscuro)
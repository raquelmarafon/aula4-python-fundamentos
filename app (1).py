# ============================================
# Manipulação de Datas e Horas em Python
# Usando o módulo datetime
# ============================================

from datetime import datetime, timedelta
import locale

# Configurar locale para português (meses/dias por extenso)
# OBS: se não funcionar no Windows, use "Portuguese_Brazil.1252"
locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

# 1. PEGAR DATA E HORA ATUAIS
agora = datetime.now()
print("Data e hora atuais:", agora.strftime("%d/%m/%Y %H:%M:%S"), "\n")

# 2. CRIAR UMA DATA ESPECÍFICA
data_especifica = datetime(2025, 12, 25, 20, 30, 0)
print("Data específica (Natal):", data_especifica.strftime("%d/%m/%Y %H:%M:%S"))
print("Data específica (por extenso):", data_especifica.strftime("%d de %B de %Y, %H:%M:%S"), "\n")

# 3. FORMATAR DATA PARA STRING
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data atual formatada:", data_formatada, "\n")

# 4. CONVERTER STRING PARA DATETIME
data_str = "21/08/2025 14:30:00"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print("String original:", data_str)
print("Convertida (formato numérico):", data_convertida.strftime("%d/%m/%Y %H:%M:%S"))
print("Convertida (por extenso):", data_convertida.strftime("%d de %B de %Y, %H:%M:%S"), "\n")

# 5. CALCULAR DIFERENÇA ENTRE DUAS DATAS
diferenca = data_especifica - agora
print("Diferença até o Natal:", diferenca)      # mostra dias + horas + minutos
print("Dias até o Natal:", diferenca.days, "\n")

# 6. SOMAR E SUBTRAIR TEMPO COM timedelta
amanha = agora + timedelta(days=1)
ontem = agora - timedelta(days=1)
print("Amanhã será:", amanha.strftime("%d/%m/%Y %H:%M:%S"))
print("Ontem foi:", ontem.strftime("%d/%m/%Y %H:%M:%S"), "\n")

# 7. EXEMPLO MAIS COMPLETO DE timedelta
mais_tempo = agora + timedelta(days=7, hours=3, minutes=15)
print("Daqui a 7 dias, 3h e 15min será:", mais_tempo.strftime("%d/%m/%Y %H:%M:%S"))
print("Daqui a 7 dias, 3h e 15min (por extenso):", mais_tempo.strftime("%d de %B de %Y, %H:%M:%S"))


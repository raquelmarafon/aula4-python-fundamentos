# ============================================
# Manipulação de Datas e Horas em Python
# Usando o módulo datetime
# ============================================

from datetime import datetime, timedelta

# Função auxiliar para garantir formato brasileiro sem milissegundos
def formatar(data):
    return data.strftime("%d/%m/%Y %H:%M:%S")

# 1. PEGAR DATA E HORA ATUAIS
agora = datetime.now()
print("Data e hora atuais:", formatar(agora), "\n")

# 2. CRIAR UMA DATA ESPECÍFICA
data_especifica = datetime(2025, 12, 25, 20, 30, 0)
print("Data específica (Natal):", formatar(data_especifica), "\n")

# 3. FORMATAR DATA PARA STRING
formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data atual formatada:", formatada, "\n")

# 4. CONVERTER STRING PARA DATA
data_str = "21/08/2025 14:30:00"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print("String original:", data_str)
print("Convertida para datetime:", formatar(data_convertida), "\n")

# 5. CALCULAR DIFERENÇA ENTRE DUAS DATAS
diferenca = data_especifica - agora
print("Diferença até o Natal:", diferenca)       # mostra dias + horas + minutos
print("Dias até o Natal:", diferenca.days, "\n")

# 6. SOMAR E SUBTRAIR TEMPO COM timedelta
amanha = agora + timedelta(days=1)
ontem = agora - timedelta(days=1)
print("Amanhã será:", formatar(amanha))
print("Ontem foi:", formatar(ontem), "\n")

# 7. EXEMPLO MAIS COMPLETO DE timedelta
mais_tempo = agora + timedelta(days=7, hours=3, minutes=15)
print("Daqui a 7 dias, 3h e 15min será:", formatar(mais_tempo))

# insurance_app

![image](https://github.com/user-attachments/assets/76f5d479-21ab-42c1-94d5-ba93d48f141e)


Aplicação para cálculo do prêmio de seguro veicular.

Desenvolvida em Python, utilizando as bibliotecas pandas, numpy, scikit-learn, tkinter

**Executar o programa**:
~bash
python insurance_app.py


**Como usar**:
1. Preencha os campos:
   - Idade do condutor
   - Valor do veículo
   - Potência do motor (em cv)
   - Histórico de acidentes (0-5)
   - Cidade (1-5, onde 1 = menor risco)
   - Tipo de veículo (1-4, onde 1 = popular)

2. Clique em "Calcular Prêmio"


**Para transformar em executável**:
Instale o PyInstaller:

~bash
pyinstaller --onefile --windowed insurance_app.py



**Funcionalidades principais**:
- Interface gráfica simples
- Armazenamento local dos dados em CSV
- Modelo de machine learning (Random Forest)
- Sistema de fallback caso não haja dados suficientes
- Auto-aprendizado conforme novos dados são inseridos




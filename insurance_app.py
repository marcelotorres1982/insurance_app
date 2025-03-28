# Importação de bibliotecas
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os


class InsuranceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI de Cotação de Seguros - Carros")

        # Verificar/Criar arquivo de dados
        self.data_file = 'insurance_data.csv'
        self.create_base_dataset()

        # Carregar modelo
        self.model = self.train_model()

        # Interface Gráfica
        self.create_widgets()

    def create_base_dataset(self):
        if not os.path.exists(self.data_file):
            columns = [
                'idade', 'valor_veiculo', 'potencia_motor', 'historico_acidentes',
                'cidade', 'tipo_veiculo', 'premio'
            ]
            with open(self.data_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(columns)

    def load_data(self):
        data = pd.read_csv(self.data_file)
        return data

    def train_model(self):
        try:
            data = self.load_data()
            if len(data) < 10:
                return None

            X = data.drop('premio', axis=1)
            y = data['premio']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            model = RandomForestRegressor(n_estimators=100)
            model.fit(X_train, y_train)
            return model
        except Exception as e:
            print(f"Erro no treinamento: {e}")
            return None

    def create_widgets(self):
        # Campos de entrada
        fields = [
            ('Idade do Condutor:', 'idade'),
            ('Valor do Veículo (R$):', 'valor_veiculo'),
            ('Potência do Motor (cv):', 'potencia_motor'),
            ('Histórico de Acidentes (0-5):', 'historico_acidentes'),
            ('Cidade (1-5):', 'cidade'),
            ('Tipo de Veículo (1-4):', 'tipo_veiculo')
        ]

        self.entries = {}
        for i, (label, name) in enumerate(fields):
            lbl = ttk.Label(self.root, text=label)
            lbl.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            ent = ttk.Entry(self.root)
            ent.grid(row=i, column=1, padx=5, pady=5)
            self.entries[name] = ent

        # Botões
        btn_calcular = ttk.Button(self.root, text="Calcular Prêmio", command=self.calculate_premium)
        btn_calcular.grid(row=6, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.root, text="Prêmio Estimado: R$")
        self.result_label.grid(row=7, column=0, columnspan=2)

    def calculate_premium(self):
        try:
            input_data = {
                'idade': int(self.entries['idade'].get()),
                'valor_veiculo': float(self.entries['valor_veiculo'].get()),
                'potencia_motor': int(self.entries['potencia_motor'].get()),
                'historico_acidentes': int(self.entries['historico_acidentes'].get()),
                'cidade': int(self.entries['cidade'].get()),
                'tipo_veiculo': int(self.entries['tipo_veiculo'].get())
            }

            # Fazer previsão
            if self.model:
                premio = self.model.predict(pd.DataFrame([input_data]))[0]
            else:
                # Modelo básico se não houver dados suficientes
                premio = (input_data['valor_veiculo'] * 0.03 +
                          input_data['potencia_motor'] * 50 +
                          input_data['historico_acidentes'] * 500)

            self.result_label.config(text=f"Prêmio Estimado: R$ {premio:.2f}")

            # Salvar dados
            self.save_data(input_data, premio)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos")

    def save_data(self, input_data, premio):
        new_data = {**input_data, 'premio': premio}
        with open(self.data_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=new_data.keys())
            writer.writerow(new_data)

        # Retreinar o modelo
        self.model = self.train_model()


if __name__ == "__main__":
    root = tk.Tk()
    app = InsuranceApp(root)
    root.mainloop()
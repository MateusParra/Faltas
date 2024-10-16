import os
import tkinter as tk


class CalculaFaltas:
    def __init__(self, aulas, faltas, aulas_total):
        self._aulas_dia = aulas
        if faltas > aulas_total:
            print("Faltas maiores do que aulas, trocando valores!")
            self._total_faltas, self._total_aulas = aulas_total, faltas
        else:
            self._total_faltas, self._total_aulas = faltas, aulas_total

    def __str__(self):
        return f"\nVocê tem: {self._total_faltas} faltas -- {self._total_aulas} aulas\n"

    def calcula_porcentagem_faltas(self, total_faltas = 0, total_aulas = 0):
        def calculo(faltas, aulas):
            porcentagem_faltas = (faltas / aulas) * 100
            return porcentagem_faltas

        if not total_aulas:
            porcentagem_faltas = calculo(self._total_faltas, self._total_aulas)
            porcentagem_faltas_int = str(porcentagem_faltas)
            porcentagem_faltas_int = porcentagem_faltas_int[:porcentagem_faltas_int.find('.')]
            return f"\nVocê está com {porcentagem_faltas_int}% de faltas\n"
        else:
            porcentagem_faltas = calculo(total_faltas, total_aulas)

        return porcentagem_faltas

    def calcular_proximos_dias(self, metodo, dias, total_faltas = 0, total_aulas = 0):
        def calcula(dias, total_faltas, total_aulas):
            aulas = self._aulas_dia * dias
            faltas_temp = total_faltas + aulas
            aulas_temp = total_aulas + aulas

            if metodo == 0:
                porcentagem_faltas = self.calcula_porcentagem_faltas(faltas_temp, aulas_temp)
            else:
                porcentagem_faltas = self.calcula_porcentagem_faltas(total_faltas, aulas_temp)

            return porcentagem_faltas

        if not total_aulas:
            porcentagem = calcula(dias, self._total_faltas, self._total_aulas)
            porcentagem_int = str(porcentagem)
            porcentagem_int = porcentagem_int[:porcentagem_int.find('.')]
            porcentagem_int = int(porcentagem_int)
            return f"\nSe você {"faltar" if metodo == 0 else "for"} {dias} dias consecutivos você ira ficar com {porcentagem_int}%\n"
        else:
            porcentagem = calcula(dias, total_faltas, total_aulas)
            return porcentagem


    def dias_para(self, metodo):
        dias = 0
        porcentagem_int = 25
        while True:
            porcentagem_faltas = self.calcular_proximos_dias(metodo, dias, self._total_faltas, self._total_aulas)
            if int(porcentagem_faltas) >= porcentagem_int if metodo == 0 else int(porcentagem_faltas) < porcentagem_int:
                break
            dias += 1

        if dias == 0:
            porcentagem_faltas_int = str(porcentagem_faltas)
            porcentagem_faltas_int = porcentagem_faltas_int[:porcentagem_faltas_int.find('.')]
            porcentagem_faltas_int = int(porcentagem_faltas_int)
            return f"\nVocê já atingiu o limite de faltas! {porcentagem_faltas_int}%\n" if metodo == 0 else \
                f"\nVocê já está com presença suficiente!\n"
        else:
            return f"\nVocê ira {"reprovar" if metodo == 0 else "recuperar"} se {"faltar" if metodo == 0 else "for"} {dias} dias consecutivos!\n"


if __name__ == "__main__":
    def on_closing():
        if root.winfo_exists():
            root.quit()
            root.destroy()

    def input_to_int(texto):
        while True:
            try:
                valor = int(input(f"\n{texto}:\n"))
                return valor
            except:
                pass


    def destroy_if_exists(window):
        if window.winfo_exists():
            window.destroy()

    def title_button(root, question_title, first_button_title = None, second_button_title = None,
                     third_button_title = None, fourth_button_title = None, fifth_button_title = None):

        def temp_value(value):
            global temp
            temp = value

        def option1():
            temp_value(1)
            destroy_if_exists(second_window)

        def option2():
            temp_value(2)
            destroy_if_exists(second_window)

        def option3():
            temp_value(3)
            destroy_if_exists(second_window)

        def option4():
            temp_value(4)
            destroy_if_exists(second_window)

        def option5():
            temp_value(5)
            destroy_if_exists(second_window)

        second_window = tk.Toplevel(root)
        second_window.title('Não Interaja Com Essa Janela')
        second_window.geometry('700x500')

        second_window.withdraw()

        frame_geral = tk.Frame(root)
        frame_geral.pack()

        frame_options = tk.Frame(frame_geral)
        frame_options.pack()

        frame_title = tk.Frame(frame_options)
        frame_title.pack()

        frame_button = tk.Frame(frame_options)
        frame_button.pack()

        title = tk.Label(frame_title, text=question_title)
        title.pack(pady=10)

        if first_button_title:
            button1 = tk.Button(frame_button, text=first_button_title, command=option1)
            button1.grid(column=0, row=0)
            if second_button_title:
                button2 = tk.Button(frame_button, text=second_button_title, command=option2)
                button2.grid(column=1, row=0)
                if third_button_title:
                    button3 = tk.Button(frame_button, text=third_button_title, command=option3)
                    button3.grid(column=2, row=0)
                    if fourth_button_title:
                        button4 = tk.Button(frame_button, text=fourth_button_title, command=option4)
                        button4.grid(column=3, row=0)
                        if fifth_button_title:
                            button5 = tk.Button(frame_button, text=fifth_button_title, command=option5)
                            button5.grid(column=4, row=0)

        root.wait_window(second_window)
        destroy_if_exists(frame_geral)

        global temp

        button_temp_value = temp

        del temp

        return button_temp_value

    def entrys(root, first_entry_title = None, second_entry_title = None, third_entry_title = None, fourth_entry_title = None, fifth_entry_title = None):
        def send():
            results = []
            try:
                if first_entry_title:
                    results.append(int(first_entry.get()))
                    if second_entry_title:
                        results.append(int(second_entry.get()))
                        if third_entry_title:
                            results.append(int(third_entry.get()))
                            if fourth_entry_title:
                                results.append(int(fourth_entry.get()))
                                if fifth_entry_title:
                                    results.append(int(fifth_entry.get()))
            except:
                return
            global temp
            temp = results
            destroy_if_exists(second_window)

        second_window = tk.Toplevel(root)
        second_window.title('Não Interaja Com Esta Janela')

        second_window.withdraw()

        frame_geral = tk.Frame(root)
        frame_geral.pack()

        frame_questionnaire = tk.Frame(frame_geral)
        frame_questionnaire.pack()

        if first_entry_title:
            first_label = tk.Label(frame_questionnaire, text=first_entry_title)
            first_label.pack(pady=(20, 0))

            first_entry = tk.Entry(frame_questionnaire)
            first_entry.pack(pady=(0, 20))
            if second_entry_title:
                second_label = tk.Label(frame_questionnaire, text=second_entry_title)
                second_label.pack(pady=(20, 0))

                second_entry = tk.Entry(frame_questionnaire)
                second_entry.pack(pady=(0, 20))
                if third_entry_title:
                    third_label = tk.Label(frame_questionnaire, text=third_entry_title)
                    third_label.pack(pady=(20, 0))

                    third_entry = tk.Entry(frame_questionnaire)
                    third_entry.pack(pady=(0, 20))
                    if fourth_entry_title:
                        fourth_label = tk.Label(frame_questionnaire, text=fourth_entry_title)
                        fourth_label.pack(pady=(20, 0))

                        fourth_entry = tk.Entry(frame_questionnaire)
                        fourth_entry.pack(pady=(0, 20))
                        if fifth_entry_title:
                            fifth_label = tk.Label(frame_questionnaire, text=fifth_entry_title)
                            fifth_label.pack(pady=(20, 0))

                            fifth_entry = tk.Entry(frame_questionnaire)
                            fifth_entry.pack(pady=(0, 20))

        send_button = tk.Button(frame_questionnaire, text='Enviar', command=send)
        send_button.pack(pady=20)

        root.wait_window(second_window)
        destroy_if_exists(frame_geral)

        global temp
        results = temp
        del temp

        return results

    def view_results(root, result):

        secondary_window = tk.Toplevel(root)
        secondary_window.title('Não interaja com esta janela')
        secondary_window.withdraw()

        frame_geral = tk.Frame(root)
        frame_geral.pack()

        result_label = tk.Label(frame_geral, text=result)
        result_label.pack(pady=20)

        exit = tk.Button(frame_geral, text='Fechar', command=secondary_window.destroy)
        exit.pack()

        root.wait_window(secondary_window)
        destroy_if_exists(frame_geral)

    def main_script():
        try:
            option = title_button(root, 'Tipo de Estudo:', 'Tecnico', 'Integral')
            match option:
                case 1:
                    classes = 6
                case 2:
                    classes = 9
                case _:
                    classes = 0

            total_faults, total_classes = entrys(root, 'Total de Faltas:', 'Total de Aulas:')

            faltas = CalculaFaltas(classes, total_faults, total_classes)

            while True:
                option = title_button(root, 'Escolha a Opção:', 'Dias para Reprovar', 'Proximas Faltas',
                                      'Porcentagem')

                match option:
                    case 3:
                        view_results(root, faltas.calcula_porcentagem_faltas())
                    case 2:
                        result = entrys(root, 'Digite os dias:')
                        dias = result[0]
                        view_results(root, faltas.calcular_proximos_dias(0, dias))
                    case 1:
                        view_results(root, faltas.dias_para(0))
                    case 4:
                        result = entrys(root, 'Digite os dias:')
                        dias = result[0]
                        view_results(root, faltas.calcular_proximos_dias(1, dias))
                    case 5:
                        view_results(root, faltas.dias_para(1))
        except:
            return


    path = os.path.dirname(__file__)

    root = tk.Tk()
    root.title('Faltas')
    root.geometry('700x500')
    root.iconbitmap(f'{path}\\panico.ico')
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.after(100, main_script)

    root.mainloop()
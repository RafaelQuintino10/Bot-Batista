


import customtkinter as ctk
import threading
import asyncio
from bot_batista import main  

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

loop_bot = None
thread_bot = None

janela = ctk.CTk()
janela.title('BOT SINAIS RED')
janela.geometry("400x250")
janela.iconbitmap("bot_icon.ico")

status_label = ctk.CTkLabel(janela, text="Bot não iniciado.", text_color="white")
status_label.pack(pady=10)

def iniciar_bot():
    global loop_bot, thread_bot

    def start_bot():
        global loop_bot
        loop_bot = asyncio.new_event_loop()
        asyncio.set_event_loop(loop_bot)
        task = loop_bot.create_task(main())
        status_label.configure(text="🤖 Bot rodando...")

        try:
            loop_bot.run_forever()
        except KeyboardInterrupt:
            status_label.configure(text="⛔ Bot interrompido")
        finally:
            print("Finalizando loop do bot")
            loop_bot.close()

    if thread_bot is None or not thread_bot.is_alive():
        status_label.configure(text="🔄 Iniciando bot...")
        thread_bot = threading.Thread(target=start_bot, daemon=True)
        thread_bot.start()
    else:
        status_label.configure(text="⚠️ Bot já está em execução!")

def parar_bot():
    global loop_bot

    if loop_bot and loop_bot.is_running():
        loop_bot.call_soon_threadsafe(loop_bot.stop)
        status_label.configure(text="⛔ Bot interrompido manualmente.")
    else:
        status_label.configure(text="⚠️ Bot não está rodando.")

botao_iniciar = ctk.CTkButton(janela, text='Iniciar Bot', command=iniciar_bot)
botao_iniciar.pack(pady=10)

botao_parar = ctk.CTkButton(janela, text='Parar Bot', command=parar_bot)
botao_parar.pack(pady=10)

janela.mainloop()

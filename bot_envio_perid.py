import asyncio
from datetime import datetime
from telegram.ext import Application, ContextTypes, CommandHandler

# === CONFIGURAÇÕES ===
TOKEN = "8012171445:AAFK183HpQe5DfDOUvduPUyxqvKThQ1NFlc"  # Substitua pelo token do seu bot
ID_CHAT = -1002718214062 # Substitua pelo ID do grupo, canal ou usuário
MENSAGEM = '''
🤖 2 TIRO 🤖
🏆 COPA 🏆 

⏰ H: 23 
➡ 52

✔ Entrada: Over 3.5 

✖✖✖✖RED✖✖✖✖ 


✅152➖➖➖✖15➖➖➖A: 0
SG: 76
💰P: 61

🎯 91,02% de Acerto
'''

# === COMANDO OPCIONAL PARA INICIAR O BOT COM /start ===
async def start(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot iniciado e enviando mensagens automáticas!")

# === FUNÇÃO ASSÍNCRONA PARA ENVIO PERIÓDICO ===
async def enviar_mensagem_periodicamente(context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_message(chat_id=ID_CHAT, text=MENSAGEM)
        print(f"[{datetime.now()}] Mensagem enviada.")
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

# === FUNÇÃO PRINCIPAL ===
def main():
    app = Application.builder().token(TOKEN).build()

    # Adiciona o comando /start (opcional)
    app.add_handler(CommandHandler("start", start))

    # Agenda a tarefa periódica a cada 30 segundos
    app.job_queue.run_repeating(enviar_mensagem_periodicamente, interval=30, first=0)

    print("Bot iniciado...")
    app.run_polling()

# === EXECUÇÃO ===
if __name__ == "__main__":
    main()

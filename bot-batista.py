from datetime import datetime
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
import sqlite3

# Conecta (ou cria) o banco de dados chamado "exemplo.db"
conn = sqlite3.connect("grupos.db")

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# ==== CONFIGURAÇÕES ====
ID_GRUPO_ORIGEM = -1002490922945
ID_GRUPO_DESTINO = 7450049318
DATA_VENCIMENTO = datetime(2025, 7, 1)


async def inserir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    chat_name = update.message.chat.title
    cursor.execute("insert into grupos_sinais (nome, chat_id) values (?, ?)", (chat_name, chat_id))
    conn.commit()
    print(f'Grupo - {chat_name} inserido na tabela...')


# ==== FUNÇÃO DE MONITORAMENTO ====
async def monitorar_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    agora = datetime.now()
    if agora > DATA_VENCIMENTO:
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text="⛔ Esta versão demo expirou. Entre em contato para renovação."
        )
        return  # Ignora qualquer outra lógica após expiração

    mensagem = update.message.text
    if "RED" in mensagem.upper():
        await context.bot.send_message(
            chat_id=ID_GRUPO_DESTINO,
            text=f"🚨 Palavra 'RED' detectada!\nGrupo - {update.message.chat.title}\n\nMensagem:\n{mensagem}"
        )

# ==== FUNÇÃO PRINCIPAL ====
def main():
    app = Application.builder().token('8012171445:AAFK183HpQe5DfDOUvduPUyxqvKThQ1NFlc').build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitorar_mensagem))
    app.add_handler(CommandHandler('inserir', inserir))

    print("🤖 Bot está rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()

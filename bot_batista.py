

from datetime import datetime, timedelta
import re
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram.constants import UpdateType

# ==== CONFIGURAÇÕES ====
ID_CANAL_H3 = -1002807164349
DATA_VENCIMENTO = datetime(2025, 6, 28)


# ==== FUNÇÃO DE MONITORAMENTO ====
async def monitorar_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # agora = datetime.now()
    # if agora > DATA_VENCIMENTO:
    #     await context.bot.send_message(
    #         chat_id=update.message.chat_id,
    #         text="⛔ Esta versão demo expirou. Entre em contato para renovação."
    #     )
    #     return
    # if not update.message:
    #     return
    message = update.effective_message 
    mensagem = message.text or message.caption
    print(f"Mensagem recebida do grupo - {message.chat.title}:\n{mensagem}\n Horário: {message.edit_date - timedelta(hours=3)}\n==================")
    if re.search(r'RED', mensagem.upper()) or re.search(r'✖{10}', mensagem):
        print(f"RED: {re.search(r'RED', mensagem.upper())}")
        print(f"✖✖✖✖✖✖: {re.search(r'✖{10}', mensagem.upper())}")
        nome_autor = message.from_user.full_name or message.from_user.username or "Desconhecido"
        horario_evento = message.edit_date
        horario_brasilia = horario_evento - timedelta(hours=3)
        horario_envio = horario_brasilia.strftime("%d/%m/%Y %H:%M:%S")

        resposta = (
            f"🚨 *RED Detectado!*\n"
            # f"👤 Autor: {nome_autor}\n"
            f"📅 Horário: {horario_envio}\n"
            f"📣 Grupo: {message.chat.title}\n\n"
            f"📝 Mensagem:\n{mensagem}"
        )

        await context.bot.send_message(
            chat_id=ID_CANAL_H3,
            text=resposta,
            parse_mode="Markdown"
        )


def main():
    # app = Application.builder().token('8012171445:AAFK183HpQe5DfDOUvduPUyxqvKThQ1NFlc').build()
    # Token bot sinais red
    app = Application.builder().token('7743797024:AAF9wnhFf7fEpdzauVY5xzJOXpcsm30IEkI').build()
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, monitorar_mensagem))
    # app.add_handler(CommandHandler('inserir', inserir))
    print("🤖 Bot está rodando...")
    app.run_polling()
    

if __name__ == '__main__':
    main()


# ==== FUNÇÃO PRINCIPAL ====
# async def main():
#     # Token bot de testes
#     # app = Application.builder().token('8012171445:AAFK183HpQe5DfDOUvduPUyxqvKThQ1NFlc').build()
#     # Token bot sinais red
#     app = Application.builder().token('7743797024:AAF9wnhFf7fEpdzauVY5xzJOXpcsm30IEkI').build()
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitorar_mensagem))
#     # app.add_handler(CommandHandler('inserir', inserir))
#     print("🤖 Bot está rodando...")
#     # app.run_polling()
#     await app.initialize()
#     await app.start()
#     await app.updater.start_polling()
#     await app.updater.wait_until_closed()
#     await app.stop()
#     await app.shutdown()





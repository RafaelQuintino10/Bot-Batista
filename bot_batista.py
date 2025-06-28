

from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler


# ==== CONFIGURAÇÕES ====
ID_GRUPO_ORIGEM = -1002490922945
# ID_GRUPO_DESTINO = 7450049318
ID_GRUPO_DESTINO = -4819929041
ID_CANAL_DESTINO = -1002642790476
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

    mensagem = update.message.text
    print(mensagem.split())
    if "GREENS" in mensagem.upper():
        nome_autor = update.message.from_user.full_name or update.message.from_user.username or "Desconhecido"
        # horario_brasilia = update.message.date - timedelta(hours=3)
        horario_brasilia = (update.message.date or datetime.now()) - timedelta(hours=3)

        horario_envio = horario_brasilia.strftime("%d/%m/%Y %H:%M:%S")

        resposta = (
            f"🚨 *RED Detectado!*\n"
            f"👤 Autor: {nome_autor}\n"
            f"📅 Horário: {horario_envio}\n"
            f"📣 Grupo: {update.message.chat.title}\n\n"
            f"📝 Mensagem:\n{mensagem}"
        )

        await context.bot.send_message(
            chat_id=ID_CANAL_H3,
            text=resposta,
            parse_mode="Markdown"
        )

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



def main():
    # app = Application.builder().token('8012171445:AAFK183HpQe5DfDOUvduPUyxqvKThQ1NFlc').build()
    # Token bot sinais red
    app = Application.builder().token('7743797024:AAF9wnhFf7fEpdzauVY5xzJOXpcsm30IEkI').build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitorar_mensagem))
    # app.add_handler(CommandHandler('inserir', inserir))
    print("🤖 Bot está rodando...")
    app.run_polling()
    

if __name__ == '__main__':
    main()





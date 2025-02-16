import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# 🔹 Coloque seu TOKEN do Bot aqui
TOKEN = "7554662920:AAFrJlGRYhsGUkahRJvuqpxA5t4TQRei1n4"

# 🔹 Configuração de logs (para ver erros no terminal)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# 🔹 Inicializa o bot
app = Application.builder().token(TOKEN).build()

# 📌 Mensagem de boas-vindas com explicações sobre o produto
async def start(update: Update, context: CallbackContext) -> None:
    text = (
        "🤖 Olá! Eu sou o *NicePassbr*, seu bot de atendimento individual.\n\n"
        "🎬 O *NicePassbr* oferece um aplicativo totalmente exclusivo compatível com seu celular, televisores, aparelhos de TV Box, videogames e muito mais!\n"
        "📺 *Mais de 100.000 conteúdos disponíveis!*\n\n"
        "🔥 *Benefícios do NicePassbr:*\n"
        "- ✅ SEM FIDELIDADE\n"
        "- ✅ ASSISTA EM *2 TELAS SIMULTANEAMENTE*\n"
        "- ✅ +DE *40 MIL CONTEÚDOS*\n"
        "- ✅ CANAIS ADULTOS (opcional)\n"
        "- ✅ ASSISTA EM SMART TV, SMARTPHONES, TV BOX, COMPUTADOR\n\n"
        "💳 *Pagamento rápido e acesso imediato!*\n"
        "📩 Assim que o pagamento for confirmado, o acesso será enviado *automaticamente* para seu e-mail e WhatsApp!\n\n"
        "💰 *Garantia de 7 dias!*\n"
        "Se dentro de 7 dias, por qualquer motivo, decidir não continuar, basta enviar um e-mail e devolvemos *100% do seu dinheiro* sem burocracia!\n\n"
        "💳 Pagamentos via *Pix ou Cartão*\n"
        "👇 Escolha um dos planos abaixo e comece agora!"
    )
    
    # Criando botões de planos
    keyboard = [
        [InlineKeyboardButton("🟢 Plano Mensal - R$19,90", url="https://pay.kirvano.com/6026d4be-6c16-4869-85e7-b49181f23523?aff=84349677-e8ba-4689-95bd-346f008dce9d")],
        [InlineKeyboardButton("🔵 Plano Trimestral - R$39,90", url="https://pay.kirvano.com/17344977-6382-47de-aa1a-021740143d2d?aff=84349677-e8ba-4689-95bd-346f008dce9d")],
        [InlineKeyboardButton("🟡 Plano Semestral - R$69,90", url="https://pay.kirvano.com/391cb7e8-9744-49d2-84ae-7b4aef946081?aff=84349677-e8ba-4689-95bd-346f008dce9d")],
        [InlineKeyboardButton("🔴 Plano Anual - R$129,90", url="https://pay.kirvano.com/10c9b8cd-0202-4e77-86fe-9c63fbe0c613?aff=84349677-e8ba-4689-95bd-346f008dce9d")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")

# 📌 Comando de suporte
async def suporte(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "📞 Para suporte, entre em contato com nosso atendimento no WhatsApp: https://wa.me/seunumerodetelefone"
    )

# 🔹 Adiciona os handlers de comandos
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("suporte", suporte))

# 🔹 Mantém o bot rodando
if __name__ == "__main__":
    print("Bot está rodando...")
    app.run_polling()

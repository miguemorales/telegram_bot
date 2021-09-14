from telegram.ext import Updater, CommandHandler, ConversationHandler

IMPUT_TEXT = 0

def start(update, context):
  update.message.reply_text('Hola bienvenido, que deseas hacer?\n\nUsa /qr para generar un codigo qr')
  
def qr_command_handler(update, context):
  update.message.reply_text('Enviame el texto para que genere un qr')
  return IMPUT_TEXT
  
if __name__ == '__main__':
  updater = Updater(token='1990363639:AAEhkQXkwoTTD6wHn_e0nwWoP0MdaEZN94A', use_context = True)
  dp = updater.dispatcher
  
  # handlers
  dp.add_handler(CommandHandler('start', start))
  
  dp.addhandler(ConversationHandler(
    entry.points = [
      CommandHandler('qr', qr_command_handler)
    ],
    states={
      IMPUT_TEXT: 
    },
    fallbacks
  
  updater.start_polling()
  updater.idle()    # aqui se queda el bot en espera hasta que se le de informacion
  

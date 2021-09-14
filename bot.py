from telegram.ext import Updater, CommandHandler 

def start(update, context):
  update.message.reply_text('Hola bienvenido, que deseas hacer?\n\nUsa /qr para generar un codigo qr')
  
  
if __name__ == '__main__':
  updater = Updater(token='1990363639:AAEhkQXkwoTTD6wHn_e0nwWoP0MdaEZN94A', use_context = True)
  dp = updater.dispatcher
  
  # handlers
  dp.add_handler(CommandHandler('start', start))
  
  updater.start_polling()
  updater.idle()    # aqui se queda el bot en espera hasta que se le de informacion
  

try:
   import pika
except Exception as e:
   print("some modules missing {}".format_map(e))
class MetaClass(type):
   _instance={}
   def __call__(cls, *args, **kwargs):
         if cls not in cls._instance:
             cls._instance[cls]=super(MetaClass, cls).__call__(*args,**kwargs)
             return cls._instance[cls]
class RabbitMqServerConfigure():
    def __init__(self,host='localhost',queue='hello'):
         self.host=host
         self.queue=queue
class rabbitmqServer():
   def __init__(self, server):
        self.server=server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()
result=channel.queue_declare(queue='hello')
queue_name = result.method.queue
channel.queue_bind(exchange='logss', queue=queue_name)
def callback(ch,method,properties,body):
     print(" [x] received %r" %body)
channel.basic_consume(queue='hello',on_message_callback=callback,auto_ack=True)
print('[*] waiting for messages. To exit press CTRL+C')
channel.start_consuming()

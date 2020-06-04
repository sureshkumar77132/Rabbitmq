try:
   import pika
   import sys
except Exception as e:
   print("some modules missing {}".format_map(e))
class MetaClass(type):
   _instance={}
   def __call__(cls, *args, **kwargs):
       if cls not in cls._instance:
          cls._instance[cls]=super(MetaClass, cls).__call__(*args,**kwargs)
          return cls._instance[cls]
class RabbitmqConfigure(metaclass=MetaClass):
    def __init__(self,queue='',host='localhost',routingKey='',exchange='',type=''):
        self.queue=queue
        self.host=host
        self.routingKey=routingKey
        self.exchange=exchange
        self.type=type
class RabbitMq():
  __slots__=["server","_channel","_connection"]
  def __init__(self,server):
      self.server=server
      self._connection =
pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
      self._channel=self._connection.channel()
      self._channel.queue_declare(queue=self.server.queue)
      self._channel.exchange_declare(exchange=self.server.exchange,exchange_type=self.server.type)
  def __enter__(self):
     print("__enter__")
     return self
  def __exit__(self, exc_type, exc_val, exc_tb):
      print("__exit__")
      self._connection.close()
  def publish(self,payload={}):
      self._channel.basic_publish(exchange=self.server.exchange,routing_key=self.server.routingKey,body=str(payload))
      print("Message Published {}".format(payload))
if __name__=="__main__":
        server =RabbitmqConfigure(queue='',host='localhost',routingKey='',exchange='logss',type='fanout')
        with RabbitMq(server) as rabbitmq:
              rabbitmq.publish(payload={"Data":22,"Data2":23})


#!/usr/bin/python
from xml.dom import minidomtry:  
xmldoc = minidom.parse('/tmp/GauravShindolkar/resources.xml') 
print ("\033[1;33;40m \033[2;37;40m \n\n Resources.xml at CELL Level \033[0;37;40m \n\n")
document = xmldoc.getElementsByTagName("xmi:XMI")[0]
 #JMSProvider = document.getElementsByTagName("resources.jms:JMSProvider") factories = JMSProvider.getElementsByTagName("factories")
 for factory in factories:
    try:
      f_name=factory.attributes["name"]    
      name_factory= f_name.value    
      j_JNDIName=factory.attributes["jndiName"]    
      nameJNDIName=j_JNDIName.value    
      bQ_name=factory.attributes["baseQueueName"]    
      baseQueueName=bQ_name.value    
      h_name=factory.attributes["host"]    
      host_name=h_name.value    
      p_name=factory.attributes["port"]    
      port_name=p_name.value   
      ch_name=factory.attributes["channel"]    
      channel_name=ch_name.value    
      tr_name=factory.attributes["transportType"]    
      transport_name=tr_name.value    
      ssl_name=factory.attributes["sslType"]    
      ssltype_name=ssl_name.value    
      sslConf_name=factory.attributes["sslConfiguration"]    
      sslConf=ssl_name.value        
      print("\n \033[0;37;40m Name of factory is: " "\033[1;31;40m" +name_factory+ "\n \033[0;37;40m JNDI Name: " "\033[1;34;40m" +nameJNDIName+ " \n \033[0;37;40m HOST : " "\033[1;32;40m" +host_name+ "\033[0;37;40m" " \n \033[0;37;40m PORT : " "\033[1;32;40m" +port_name+ "\033[0;37;40m" " \n \033[0;37;40m CHANNEL : " "\033[1;32;40m" +channel_name+ "\033[0;37;40m" " \n \033[0;37;40m Transport type : " "\033[1;32;40m" +transport_name+ "\033[0;37;40m" " \n \033[0;37;40m SSL Type : " "\033[1;32;40m" +ssltype_name+ "\033[0;37;40m" " \n \033[0;37;40m SSL Configuration : " "\033[1;32;40m" +sslConf+ "\033[0;37;40m")   
      except KeyError:
        continue
 except IOError: print ('\n\n \033[1;36;40m Resources.xml file not present at Cell level \n\n')

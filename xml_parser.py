#!/usr/bin/pythonfrom xml.dom import minidom
def parse_xml(xml_file):
        xmldoc = minidom.parse(xml_file)
        document = xmldoc.getElementsByTagName("xmi:XMI")[0]
        namebindings = document.getElementsByTagName("namebindings")
        for namebinding in namebindings:                
          n_name=namebinding.attributes["name"]                
          name_namebinding= n_name.value                
          n_InNameSpace=namebinding.attributes["nameInNameSpace"]                
          nameInNameSpace=n_InNameSpace.value                
          s_name=namebinding.attributes["stringToBind"]                
          stringToBind=s_name.value                
          print("\033[0;37;40m Name of Namebinding is: " "\033[1;31;40m" +name_namebinding+ " \033[0;37;40m with NameSpace value as : " "\033[1;34;40m" +nameInNameSpace+ " \033[0;37;40m along with String to bind value as : " "\033[1;32;40m" +stringToBind)
parse_xml(r"/tmp/GauravShindolkar/dummy/namebindings.xml")
parse_xml(r"/tmp/GauravShindolkar/namebindings.xml")

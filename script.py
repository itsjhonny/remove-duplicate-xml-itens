import os
import lxml.etree as et

# LOAD XML AND XSL FILES
xml = et.parse('itens_xml.xml')
xsl = et.parse('XSLTScript.xsl')

# TRANSFORM SOURCE
transform = et.XSLT(xsl)
result = transform(xml)

# PRINT RESULT TO SCREEN
# print(result)

# SAVE RESULT TO FILE
with open('Output.xml', 'wb') as f:
    f.write(result)
    
print("Finalizado com sucesso")
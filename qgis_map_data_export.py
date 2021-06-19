# For QGIS - Prints out JavaScript that can be run in Zotero to create items for maps
from xml.etree import ElementTree as ETree

file_out = open("E:\\a_new_orgs\\crane\\large\\maps_syria.csv", "w")
file_out.write('"map_name","crs","extent","language","year","color_scheme","ruins_symbol"\n')

layers = qgis.utils.iface.mapCanvas().layers()
for layer in layers:
    layerType = layer.type()
    layerName = layer.name()
    if layerType == QgsMapLayer.RasterLayer:
          
        xml = QgsLayerDefinition.exportLayerDefinitionLayers([layer], QgsReadWriteContext()).toString()
        xml_root =  ETree.fromstring(xml)
        
        keywords = {'color_scheme': '', 'year': '', 'ruins_symbol': ''}
        for obj in xml_root.findall('./maplayers/maplayer/resourceMetadata'):
            print(obj)
            map_language = obj.find('language').text
            for keywords_obj in obj.findall('./keywords'):
                keywords[keywords_obj.attrib['vocabulary']] = keywords_obj.find('keyword').text
        print(keywords)
        print(str(layer.name()), layer.crs(), layer.extent())
        file_out.write('"' + str(layer.name()) + '","' + str(layer.crs()) + '","' + str(layer.extent()) + '","' + str(map_language) + '","' +str(keywords['year']) + '","' + keywords['color_scheme']  + '","' + keywords['ruins_symbol'] + '"\n' )

file_out.close()

print("------------- JAVASCRIPT BELOW ------------------")

for layer in layers:
    layerType = layer.type()
    layerName = layer.name()
    if layerType == QgsMapLayer.RasterLayer:
          
        xml = QgsLayerDefinition.exportLayerDefinitionLayers([layer], QgsReadWriteContext()).toString()
        xml_root =  ETree.fromstring(xml)
        
        
        
        keywords = {'color_scheme': '', 'year': '', 'ruins_symbol': ''}
        for obj in xml_root.findall('./maplayers/maplayer/resourceMetadata'):
            
            map_language = obj.find('language').text
            for keywords_obj in obj.findall('./keywords'):
                keywords[keywords_obj.attrib['vocabulary']] = keywords_obj.find('keyword').text
        #print(keywords)
        #print(str(layer.name()), layer.crs(), layer.extent())
        print("var item = new Zotero.Item('map');")
        print("item.setField('title', '"+str(layer.name())+"');")
        print("item.setField('publisher', 'Service Géographique des Forces Française Libres du Levant');")
        print("item.setField('date', '"+str(keywords['year'])+"');")
        print("item.setField('language', '"+map_language+"');")
        print("item.setField('place', 'Syria "+str(layer.crs())+" "+str(layer.extent())+"');")
        print("var itemID = await item.saveTx();")
        print("return itemID;")

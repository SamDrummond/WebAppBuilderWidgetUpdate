import shutil
import os

webAppBuilderPath = 'C:\\arcgis\\webappbuilderlocal'
widgetSourceRoot = 'C:\\arcgis\\widgets'
widgets = [
	'DrawMeasureWidget',
	'LayerListWidget',
	'LocateCoordinatesWidget',
	'PrintWidget',
	'SpatialQueryWidget',
	'WebMapSwitcherWidget'
]

def delete(source):
	try:
		shutil.rmtree(source)
	except shutil.Error as e:
		print('Directory not deleted. Error: %s' % e)
	except OSError as e:
		print('Directory not deleted. Error: %s' % e)

def copy(source, destination):
    try:
        shutil.copytree(source, destination)
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def updateWidget(widgetName):
	
	widgetSourcePath = widgetSourceRoot + '\\' + widgetName + '\\src'
	widgetDestinationPath = webAppBuilderPath + '\\client\\stemapp\\widgets\\' + widgetName;
		
	delete(widgetDestinationPath)	
	copy(widgetSourcePath, widgetDestinationPath)

def updateWidgets():
	for widget in widgets:
		print '... attempting to update: ' + widget
		updateWidget(widget)
		print '... update complete: ' + widget
		
print 'Updating widgets'
updateWidgets();
	




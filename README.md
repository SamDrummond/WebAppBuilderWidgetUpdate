# Widget Update #
A handy little python script to automate the process of copying the source code from a widget repository into the stemapp of Esri's Web AppBuilder at version 1.1.

## Configuration Parameters ##
`PYTHON
webAppBuilderPath = '' #path to the top level web application builder
widgetSourceRoot = '' #the top level path of the widget repositories
widgets = [''] #[Array of widget names - matching the name of the repo and the destination widget name]
`

## Requirements ##
- Python 2.7
- Esri Web AppBuilder 1.1
- Widget source code needs to be in the 'src' directory of the repo 

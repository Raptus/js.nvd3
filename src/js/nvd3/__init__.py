from fanstatic import Library, Resource
import js.d3

library = Library('nvd3', 'resources')

nvd3 = Resource(library, 'nv.d3.js', depends=[d3.d3], minified='nv.d3.min.js')

from fanstatic import Library, Resource
import js.d3

library = Library('nvd3', 'resources')

css = Resource(library, 'nv.d3.css')
nvd3 = Resource(library, 'nv.d3.js', depends=[js.d3.d3, css], minified='nv.d3.min.js')

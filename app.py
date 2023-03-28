import svgpathtools as svg
import os

def compress_svg(infile, outfile):
    # Load the SVG file using svgpathtools
    doc = svg.Document(infile)

    # Simplify paths using svgpathtools' simplify function
    doc.simplify(const_tol=0.01, angle_tol=0.01)

    # Compress the SVG using svgpathtools' compress function
    doc.compress()

    # Save the compressed SVG to a new file
    svg.save_paths(doc.paths(), outfile)

    # Remove the original file
    os.remove(infile)

# Usage
compress_svg('input.svg', 'output.svg')

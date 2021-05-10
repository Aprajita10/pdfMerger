import sys
import PyPDF2

inputs=sys.argv[1:]

def pdf_combiner(pdf_folder):
	merger=PyPDF2.PdfFileMerger()
	for pdf in pdf_folder:
		print(pdf)
		merger.append(pdf)
	merger.write('new.pdf')


pdf_combiner(inputs)	    



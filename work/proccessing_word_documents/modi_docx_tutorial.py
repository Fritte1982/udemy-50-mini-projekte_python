import docx
from own_packages import path_attributes

word_sources_path = path_attributes.DOCX_SOURCE
docpath1 = word_sources_path / "panda1.docx"
docpath2 = word_sources_path / "panda2.docx"

doc1 = docx.Document(docpath1)
doc2 = docx.Document(docpath2)

paragraphs = doc1.paragraphs




